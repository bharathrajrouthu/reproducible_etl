# from sqlalchemy import create_engine, text
# import psycopg2

# engine = create_engine("postgresql+psycopg2://postgres:pass123@localhost:5432/onprem_db")

# # postgresql://username:password@host:port/database_name
# # postgresql://myuser:mypassword@localhost:5432/mydatabase
# # postgresql://postgres:postgres@localhost:5432/etl

# engine.connect()
# with engine.connect() as conn:
#   conn.execute(text("""
#     INSERT INTO test (id) VALUES (3);
#     """))

'''
V2
'''

from sqlalchemy import create_engine, text
import psycopg2

# for postgreSQL database credentials can be written as 
user = 'postgres'
password = 'postgres'
host = 'localhost'
port = '5432'
database = 'onprem_db'
# for creating connection string
connection_str = "postgresql://postgres@localhost:5432/onprem_db"
# SQLAlchemy engine
engine = create_engine(connection_str)
# you can test if the connection is made or not
try:
    with engine.connect() as connection_str:
        print('Successfully connected to the PostgreSQL database')
        query = connection_str.execute(text("""
        SELECT * FROM test;
        """))
        print(query.fetchall())
except Exception as ex:
    print(f'Sorry failed to connect: {ex}')