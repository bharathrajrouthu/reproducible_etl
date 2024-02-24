from logs.log import log
import pandas as pd

class Transform:
    '''
    To transform and clean the raw data.
    Functions for transformations
    '''
    @staticmethod
    def clean_columns(df):
        '''
        Replaces spaces with underscores in the column names of a DataFrame.
        Parameters:
            df: Input DataFrame
        Returns:
            df: DataFrame with column names having spaces replaced by underscores.
        '''
        df.columns = [x.replace(' ', '_') for x in df.columns]
        log("Cleaned column names")
        return df
    
    @staticmethod
    def standardize_columns(df):
        '''
        Standardizes column names in a DataFrame by renaming specific columns and converting all column names to lowercase.
        Parameters:
            df: Input DataFrame
        Returns:
            df: DataFrame with standardized column names.
        '''
        # df = df.rename(columns= {'Transaction_No': 'Transaction_Id', 'Customer_No': 'Customer_Id', 'Product_No': 'Product_Id', 'Product_Name': 'Name'})
        # df.columns = map(str.lower, df.columns)
        new_columns = []
        for name in df.columns:
            if '_' in name:
                new_columns.append(name.split('_')[0].lower() + '_id')
            else:
                new_columns.append(name.lower())
        df.columns = new_columns
        log("Standardized the column names")
        return df
    
    #removing duplicate data
    @staticmethod
    def remove_duplicates(df):
        '''
        Removes duplicate rows from a DataFrame.
        Parameters:
            df: Input DataFrame
        Returns:
            df: DataFrame with duplicate rows removed.
        '''
        df = df.drop_duplicates()
        log("Removed the duplicate rows")
        return df
    
    # dealing with missing values
    @staticmethod
    def remove_missing_values(df):
        '''
        Removes missing values and specific rows from a DataFrame.
        Parameters:
            df: Input DataFrame
        Returns:
            df: DataFrame with missing values removed and specific rows filtered out.
        '''
        df = df.dropna(subset=['customer_id'])
        df = df[~df['transaction_id'].str.contains('C')]
        log("Removed the missing values")
        return df
    
    # checking for order quantity error values
    @staticmethod
    def remove_empty_orders(df):
        '''
        Removes rows with empty orders (quantity <= 0) from a DataFrame.
        Parameters:
            df: Input DataFrame
        Returns:
            df: DataFrame with rows having empty orders removed.
        '''
        df = df[df['quantity'] > 0]
        log("Removed empty orders")
        return df
    
    # data type catsing 
    @staticmethod
    def cast_types(df):
        '''
        Converts specific columns to the desired data types in a DataFrame.
        Parameters:
            df: Input DataFrame
        Returns:
            df: DataFrame with specified columns converted to the desired data types.
        '''
        df = df.astype({"customer_id": int, "transaction_id": int})
        df["date"]= pd.to_datetime(df["date"], format="%m/%d/%Y")
        log("Type casted column names to necessary data types")
        return df
    
    # creating new columns using existing data
    @staticmethod
    def create_columns(df):
        '''
        Create new columns and convert specific columns to the desired data types.
        Parameters:
            df: Input DataFrame
        Returns:
            df: DataFrame with specified columns converted to the desired data types and date-related information extracted.
        '''
        df["year"] = df['date'].dt.year
        df["day"] = df['date'].dt.day
        df["day_name"] = df['date'].dt.day_name()
        df['month'] = df['date'].dt.month
        df['quarter'] = df['date'].dt.quarter
        df['week'] = df['date'].dt.isocalendar().week

        country_id = df["country_id"] = df["country"].apply(lambda x: x[:3].upper() + str(len(x)))
        df["country_id"] = country_id
        log("Created new columns and type casted necessary data types")
        return df