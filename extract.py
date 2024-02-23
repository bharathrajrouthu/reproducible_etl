from logs.log import log
import pandas as pd

class Extract:
    def __init__(self):
        pass

    def read_data(self, path):
        '''
        Load in new data from CSV file
        '''
        try:
            data = pd.read_csv(path)
        except UnicodeDecodeError:
            print('There has been an encoding error, please check the file you are loading is in \
                UTF-8 encoding.')
        log("Read data operation completed successfully")
        log("Returning the data frame")
        return data


######################################################################################################################################################################################

# # df = pd.read_csv('data/Sales Transaction_15rows.csv')

# df = pd.read_csv('data/Sales Transaction v.4a.csv')

# shape_df = df.shape


# # replace column spaces with '_' for consistency

# df.columns = [x.replace(' ', '_') for x in df.columns]



# # standardising column names
# '''
# enhances data consistency, simplifies data management, and improves data analysis by ensuring a uniform naming convention across datasets.
# '''
# # df = df.rename(columns= {'TransactionNo': 'transaction_id', 'Date'})
# df.columns = map(str.lower, df.columns)

# # print(df[:5])

# # removing duplicate data
# '''
# data duplicates improves data accuracy, reduces storage space, and enhances analysis results by eliminating redundant information.
# '''
# df = df.drop_duplicates()

# # print(df)

# # dealing with missing values
# '''
# missing values, including imputation and deleting data containing missing values.

# Canceled transactions
# '''
# df.isnull().sum()

# null_value = df.loc[df['customer_no'].isnull()].index

# missing_val = df.drop(null_value, inplace= True)

# # Enrichment
# # dealing with missing values
# '''
# handling rows due to the presence of canceled transactions and negative order quantity values.
# '''
# canceled_transaction = df.loc[df['transaction_no'].str.contains('C')].index

# df.drop(canceled_transaction, inplace= True)

# # checking for order quantity error values
# '''
# If order quantity less than zero
# '''

# empty_quantity = df.loc[df['quantity']<= 0]

# # print(df.shape)

# # data type catsing 

# df = df.astype({"transaction_no": int, "customer_no": int})

# df["date"]= pd.to_datetime(df["date"], format="%m/%d/%Y")

# # print(df.dtypes)


# # creating new columns using existing data
# '''
# The purpose is to enhance the information obtained and to make better decisions. 

# Extracts data from date columns to get deeper insights, such as year, quarter, month, week, date, and even day. 
# '''
# df["year"] = df['date'].dt.year
# df['quarter'] = df['date'].dt.quarter
# df['month'] = df['date'].dt.month
# df['week'] = df['date'].dt.isocalendar().week
# df["day"] = df['date'].dt.day
# df["day_name"] = df['date'].dt.day_name()

# country_id = df["country"].str.upper().str.slice(stop=3) + df["country"].str.len().astype(str)
# df["country_id"] = country_id

# print(df.head)
# print(df.columns)





    
    
        