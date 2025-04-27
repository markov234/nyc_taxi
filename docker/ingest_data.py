#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from sqlalchemy import create_engine
import argparse
import time
import requests

def main(params):
    user=params.user
    password=params.password
    host=params.host
    port=params.port
    database=params.database
    table=params.table
    url=params.url

    file_name = 'output.parquet'

    response = requests.get(url)
    if response.status_code == 200:
        with open(file_name, 'wb') as f:
            f.write(response.content)
    else:
        print(f"Failed to download file: {response.status_code}")
    
    # Create a connection to the database. Will help us in getting the correct schema for postgres.
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')
    engine.connect()

    # Read in data. 3.4 million rows.
    print("Reading Parquet file...")
    df = pd.read_parquet(file_name)

    # This creates the table with just the columns (no rows yet).
    df.head(n=0).to_sql(name='yellow_taxi_data', con=engine, if_exists='replace')

    chunk_size = 100000
    num_rows = len(df)

    print("Starting upload...")

    # Now add rows to the table in chunks.
    for i in range(0, num_rows, chunk_size):
        print(f"Inserting rows {i} to {i + chunk_size}...")

        df_chunk = df[i:i + chunk_size]

        chunk_start = time.time()

        df_chunk.to_sql(
            name='yellow_taxi_data',
            con=engine,
            if_exists='append',
            index=False
        )

        chunk_end = time.time()
        print(f"Chunk took {chunk_end - chunk_start:.2f} seconds")

    print("Upload finished.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest parquet data to Postgres')

    parser.add_argument('--user', type=str, help='Postgres username')
    parser.add_argument('--password', type=str, help='Postgres password')
    parser.add_argument('--host', type=str, help='Postgres host')
    parser.add_argument('--port', type=str, help='Postgres port')
    parser.add_argument('--database', type=str, help='Postgres database name')
    parser.add_argument('--table', type=str, help='Postgres table name')
    parser.add_argument('--url', type=str, help='URL of the parquet file')

    args = parser.parse_args()

    main(args)
