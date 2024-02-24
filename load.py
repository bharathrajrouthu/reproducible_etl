from logs.log import log
from sqlalchemy import create_engine, text
import pandas as pd

class Load:

    def __init__(self):
        pass
    '''
    connection to DB and data insertion
    '''

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

        '''
        DB schema and function queries to insert into DB
        '''
        # try:
            
        #     with engine.connect() as conn:
        #         print("**INSERTION IN PROGRESS**")
        #         conn.execute(text("""
        #         ALTER TABLE sales_fact 
        #         ADD PRIMARY KEY (customer_key, transaction_key, date_key, product_key, country_key);
        #         """))
        #         conn.execute(text("""
        #         ALTER TABLE sales_fact
        #         ADD CONSTRAINT fk_customer_dim_sales_fact
        #         FOREIGN KEY (customer_key)
        #         REFERENCES customer_dim (customer_key);
        #         """))
        #         conn.execute(text("""
        #         ALTER TABLE sales_fact
        #         ADD CONSTRAINT fk_transaction_dim_sales_fact
        #         FOREIGN KEY (transaction_key)
        #         REFERENCES transaction_dim (transaction_key);
        #         """))
        #         conn.execute(text("""
        #         ALTER TABLE sales_fact
        #         ADD CONSTRAINT fk_date_dim_sales_fact
        #         FOREIGN KEY (date_key)
        #         REFERENCES date_dim (date_key);
        #         """))
        #         conn.execute(text("""
        #         ALTER TABLE sales_fact
        #         ADD CONSTRAINT fk_product_dim_sales_fact
        #         FOREIGN KEY (product_key)
        #         REFERENCES product_dim (product_key);
        #         """))
        #         conn.execute(text("""
        #         ALTER TABLE sales_fact
        #         ADD CONSTRAINT fk_country_dim_sales_fact
        #         FOREIGN KEY (country_key)
        #         REFERENCES country_dim (country_key);
        #         """))
        #     print("**ALL THE STATEMNETS EXECUTED AND INSERTION DONE**")
        #     log("Succesfully completed data insertion into DB")
        # except Exception as e:
            # print(e)







##########################################################################################################################################################################
# def load_csv(self, path: str):
#     '''
#     Load to a csv file
#     :param path: Path to the csv file to load data into
#     '''
#     self.data.to_csv(path)

# def load_pickle(self, path):
#     '''
#     Load to an pkl file
#     :param path: Path to the pkl file to load data into
#     '''
#     self.data.to_pickle(path)
        

# def load_table(df: pd.DataFrame, table_name: str, key: str, replacement_key: str):
#     engine = create_engine("postgresql://postgres@localhost:5432/onprem_db")
#     engine.connect()

#     df_table = df[[key]].drop_duplicates().sort_values(by=key)
#     df_table = df_table.reset_index(drop=True)
#     df_table[replacement_key] = df_table.index

#     table_name= df_table.set_index(key)
#     dim_table_name = f"{table_name}_dim"
#     table_name.to_sql(dim_table_name, con=engine, if_exists="replace")
#     with engine.connect() as conn:
#         conn.execute(text(f"ALTER TABLE {dim_table_name} ADD PRIMARY KEY ({replacement_key});"))
