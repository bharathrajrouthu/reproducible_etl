from extract import Extract
from transform import Transform
from load import Load

from sqlalchemy import create_engine, text

def main():
    '''
    Data Extarction
    '''
    extract = Extract()
    df = extract.read_data('data/transaction-data.csv')
    print("**DATA EXTRACTION COMPLETED**")
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
    print("**DATA TRANSFROMATION DONE**")
    '''
    Load data to the Database
    '''
    try:
        load = Load()
        sales_df, customer_df, product_df, transaction_df, country_df, date_df = load.create_tables(df)
        load.insert_tables(sales_df, customer_df, product_df, transaction_df, country_df, date_df)
        print("**LOAD TO DB FINISHED**")

    except Exception as e:
        print("Error has occured during DB Ingestion: ", e)

if __name__ == '__main__':
    main()
