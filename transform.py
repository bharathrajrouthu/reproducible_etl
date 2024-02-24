from logs.log import log
import pandas as pd

class Transform:
    '''
    To transform and clean the raw data
    '''
    def __init__(self):
        pass
    '''
    Functions for transsformations
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
    



################################################################################
# '''
# Extracted df as data from Extract.py
# '''
# # data = load_data()

# # df = data
# '''
# Functions for transsformations
# '''
# # replace column spaces with '_' for consistency
# def clean_column_names(df):
    
#     df.columns = [x.replace(' ', '_') for x in df.columns]
#     return df

# # standardising column names
# def standard_column_names(df):
#     df = df.rename(columns= {'Transaction_No': 'Transaction_Id', 'Customer_No': 'Customer_Id'})
#     df.columns = map(str.lower, df.columns)
#     return df

# #removing duplicate data
# def remove_duplicates(df):
#     df = df.drop_duplicates()
#     return df

# # dealing with missing values

# def remove_missing_values(df):
#     df.isnull().sum()
#     null_value = df.loc[df['customer_id'].isnull()].index
#     df = df.drop(null_value, inplace= True)

#     canceled_transaction = df.loc[df['transaction_id'].str.contains('C')].index
#     df = df.drop(canceled_transaction, inplace= True)

#     return df

# # checking for order quantity error values
# def remove_empty_orders(df):
#     empty_quantity = df.loc[df['quantity']<= 0].index
#     df = df.drop(empty_quantity, inplace= True)
#     return df

# # data type catsing 
# def cast_types(df):
#     df = df.astype({"transaction_id": int, "customer_id": int})
#     df["date"]= pd.to_datetime(df["date"], format="%m/%d/%Y")
#     return df

# # creating new columns using existing data
# def cast_dtypes(df):
#     df["year"] = df['date'].dt.year
#     df['quarter'] = df['date'].dt.quarter
#     df['month'] = df['date'].dt.month
#     df['week'] = df['date'].dt.isocalendar().week
#     df["day"] = df['date'].dt.day
#     df["day_name"] = df['date'].dt.day_name()

#     country_id = df["country"].str.upper().str.slice(stop=3) + df["country"].str.len().astype(str)
#     df["country_id"] = country_id
#     return df




# '''
# Previos code gists
# '''
# # def check_duplicates(self, remove:bool=False):
# #     '''
# #     Check for duplicates 
# #     :param remove: Boolean set to True if the duplicates should be removed
# #     '''
# #     dupes = len(self.data) - len(self.data.drop_duplicates())

# #     if dupes is not None:
# #         self.messages.update({'Duplicates': dupes})
# #     if remove:
# #         self.data.drop_duplicates(inplace= True)