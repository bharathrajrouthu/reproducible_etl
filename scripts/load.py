from logs.log import log
from sqlalchemy import create_engine, text
import pandas as pd

class Load:
    '''
    Connection to DB and data insertion
    '''
    def create_tables(self, df):
        '''
        Creates databse tables.
        Parameters:
            self: The class instance
            df: Input DataFrame.
        Returns:
            sales_dataframe: DataFrame containing sales data.
            customer_dataframe: DataFrame containing customer data.
            unique_product_df: DataFrame containing unique product data.
            transaction_dataframe: DataFrame containing transaction data.
            country_dataframe: DataFrame containing country data.
            date_dataframe: DataFrame containing date-related data.
        '''
        #  A new customer dataframe
        customer_dataframe = df[["customer_id"]].drop_duplicates().sort_values(by="customer_id")
        customer_dataframe = customer_dataframe.reset_index(drop=True)
        customer_dataframe["customer_key"] = customer_dataframe.index 

        # A new product dataframe
        product_dataframe = df[['product_id', "name", "price"]]
        unique_product_df = product_dataframe.drop_duplicates().sort_values(by=['name', 'price']).reset_index(drop=True)
        unique_product_df['product_key'] = unique_product_df.index
        unique_product_df = product_dataframe.merge(unique_product_df, on=['product_id', 'name', 'price']).sort_values(by=['name', 'price']).drop_duplicates()

        # A new transaction dataframe
        transaction_dataframe = df[["transaction_id"]].drop_duplicates().sort_values(by="transaction_id")
        transaction_dataframe = transaction_dataframe.reset_index(drop=True)
        transaction_dataframe["transaction_key"] = transaction_dataframe.index

        # # A new country dataframe
        country_dataframe = df[["country", "country_id"] ].drop_duplicates().sort_values(by="country_id")
        country_dataframe = country_dataframe.reset_index(drop=True)
        country_dataframe["country_key"] = country_dataframe.index

        # # A new date dataframe
        date_dataframe = df[["date", "week", "day_name",  "day", "month", "quarter", "year"]].drop_duplicates().sort_values(by="date")
        date_dataframe = date_dataframe.reset_index(drop=True)
        date_dataframe["date_key"] = date_dataframe.index
        
        # Aggregate the results for sales dataframe
        result = df.merge(customer_dataframe, on="customer_id")
        result = result.merge(unique_product_df, on=["product_id", "name", "price"])
        result = result.merge(transaction_dataframe, on="transaction_id")
        result = result.merge(country_dataframe, on=["country_id", "country"])
        sales_dataframe = result.merge(date_dataframe, on=["date", "week", "day_name",  "day", "month", "quarter", "year"])

        return sales_dataframe, customer_dataframe, unique_product_df, transaction_dataframe, country_dataframe, date_dataframe

    def insert_tables(self, sales_dataframe, customer_dataframe, unique_product_df, transaction_dataframe, country_dataframe, date_dataframe):
        '''
        Inserts tables with into database.
        Parameters:
            self: The class instance.
            sales_dataframe: DataFrame containing sales data.
            customer_dataframe: DataFrame containing customer data.
            unique_product_df: DataFrame containing unique product data.
            transaction_dataframe: DataFrame containing transaction data.
            country_dataframe: DataFrame containing country data.
            date_dataframe: DataFrame containing date-related data.
        Returns:
            None
        '''
        engine = create_engine("postgresql://postgres@localhost:5432/onprem_db")
        engine.connect()
        log("Connected to the Database")
        '''
        INSERTION
        '''
        # Sales Table Insertion
        sales_table = sales_dataframe[["customer_key", "transaction_key", "date_key", "product_key", "country_key", "quantity"]].sort_values(by="date_key")
        sales_table.to_sql("sales", con=engine, if_exists="replace", index=False)

        # Customer Table Insertion
        customer_table = customer_dataframe.set_index("customer_key")
        customer_table.to_sql("customer", con=engine, if_exists="replace")
        with engine.connect() as conn:
            conn.execute(text("ALTER TABLE customer ADD PRIMARY KEY (customer_key);"))

        # Product Table Insertion
        product_table = unique_product_df.set_index("product_key")
        product_table.to_sql("product", con=engine, if_exists="replace")
        with engine.connect() as conn:
            conn.execute(text("ALTER TABLE product ADD PRIMARY KEY (product_key);"))

        # Transaction Table Insertion
        transaction_table = transaction_dataframe.set_index("transaction_key")
        transaction_table.to_sql("transaction", con=engine, if_exists="replace")
        with engine.connect() as conn:
            conn.execute(text("ALTER TABLE transaction ADD PRIMARY KEY (transaction_key);"))

        # Country Table Insertion
        country_table = country_dataframe.set_index("country_key")
        country_table.to_sql("country", con=engine, if_exists="replace")
        with engine.connect() as conn:
            conn.execute(text("ALTER TABLE country ADD PRIMARY KEY (country_key);"))

       # Date Table Insertion
        date_table = date_dataframe.set_index("date_key")
        date_table['date'] = date_table['date'].dt.date
        date_table.to_sql("date", con=engine, if_exists="replace")
        with engine.connect() as conn:
            conn.execute(text("ALTER TABLE date ADD PRIMARY KEY (date_key);"))

        print("**INSERTION COMPLETED")
        log("Loaded Data into DB")