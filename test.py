import pandas as pd
from logs.log import log

df = pd.read_csv('data/transaction-data.csv')
df.columns = [x.replace(' ', '_') for x in df.columns]
df = df.rename(columns= {'Transaction_No': 'Transaction_Id', 'Customer_No': 'Customer_Id'})
df.columns = map(str.lower, df.columns)
df = df.drop_duplicates()
# print(df.head())
        

def remove_missing_values(df):
    df.isnull().sum()

    null_value = df.loc[df['customer_id'].isnull()].index

    df.drop(null_value, inplace= True)

    return df

def func_2(df):
    canceled_transaction = df.loc[df['transaction_id'].str.contains('C')].index

    df.drop(canceled_transaction, inplace= True)

    return df

# def remove_missing_values2(df):
#     df = df.dropna(subset=['customer_id'])
#     df = df[~df['transaction_id'].str.contains('C')]
#     return df

# answer_1 = remove_missing_values(df)
# answer = func_2(answer_1)
# # ans_2 = remove_missing_values2(df)

def test_standard(df):
    # filter_columns = [col_name for col_name in df.columns if '_' in col_name]
    # print(filter_columns)
    # df.columns = [name.split('_')[0].lower() + '_id' for name in df.columns if '_' in name]
    new_columns = []
    
    for name in df.columns:
        if '_' in name:
            new_columns.append(name.split('_')[0].lower() + '_id')
        else:
            new_columns.append(name.lower())

    print(new_columns)
    df.columns = new_columns
    # df.columns = new_columns

    # df = df.rename(columns= {'Transaction_No': 'Transaction_Id', 'Customer_No': 'Customer_Id', 'Product_No': 'Product_Id', 'Product_Name': 'Name'})
    # df.columns = map(str.lower, df.columns)

    return df

data = [['123', '456' , '123', '456' , '123', '456' , '123', '456' ]]
input_df = pd.DataFrame(data, columns=['Transaction_No','Date', 'Product_No', 'Name', 'Price' ,'Quantity' ,'Customer_No' ,'Country'])

log("Checking the shape of DataFrame")

print(test_standard(input_df))
# print(ans_2.shape)


