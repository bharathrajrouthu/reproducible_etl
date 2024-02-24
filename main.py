from extract import Extract
from transform import Transform
from load import Load

from sqlalchemy import create_engine, text

def main():
    '''
    Extract data
    '''
    extract = Extract()
    df = extract.read_data('data/transaction-data.csv')
    '''
    Transform the data
    '''
    transform = Transform()
    # Clean column names
    df = transform.clean_columns(df)
    # Standardize column names
    df = transform.standardize_columns(df)
    # Remove duplicates
    df = transform.remove_duplicates(df)
    # Remove missing values
    df = transform.remove_missing_values(df)
    # Remove empty orders
    df = transform.remove_empty_orders(df)
    # Cast types
    df = transform.cast_types(df)
    # Cast data types
    df = transform.create_columns(df)
    # the processed dataframe
    print("** TEST DATA FRAME **")
    print(df.columns)
    '''
    Load data to the Database
    '''
    try:
        load = Load()
        sales_df, customer_df, product_df, transaction_df, country_df, date_df = load.create_tables(df)
        load.insert_tables(sales_df, customer_df, product_df, transaction_df, country_df, date_df)

    except Exception as e:
        print("Error has occured during DB Ingestion: ", e)

if __name__ == '__main__':
    main()


############################################################################################################
    '''
    Step 1: Call extract data from extract.py
    Step 2: Call transform function from transform.py - pass data as argumnet to perform transformations
    Step 3: Once returned df. Call load from load.py
    '''

    # data = extract_data()
    # transform = transform_data(data)
    '''
    Try test connection from postgres DB
    '''
    # load = load_data(transform)
