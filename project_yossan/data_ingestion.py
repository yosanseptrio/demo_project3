import psycopg2
import os
import sys

table_name=sys.argv[1]

#get credentials
host=os.environ['POSTGRES_HOST']
dbname=os.environ['POSTGRES_DB']
user=os.environ['POSTGRES_USER']
port=os.environ['POSTGRES_PORT']
password=os.environ['POSTGRES_PASSWORD']

conn = psycopg2.connect(host=host, dbname=dbname, user=user, port=port, password=password)

out_file=open(f"{table_name}.csv", 'w')

sql=f"copy (select * from {table_name} limit 100) to stdout csv header"

cur = conn.cursor()
cur.copy_expert(sql, out_file)
cur.close()

conn.close()
