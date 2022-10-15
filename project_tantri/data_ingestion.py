#!/usr/bin/env python
# coding: utf-8

# In[9]:


import psycopg2
import os
import sys

table_name=sys.argv[1]

host=os.environ['POSTGRES_HOST']
dbname=os.environ['POSTGRES_DB']
port=os.environ['POSTGRES_PORT']
user=os.environ['POSTGRES_USER']
password=os.environ['POSTGRES_PASSWORD']

conn = psycopg2.connect(host=host, dbname=dbname, user=user, port=port, password=password)

out_file=open(f"{table_name}.csv","w")

sql="copy (select * from olist_customers_dataset_csv limit 100) to stdout csv header"

cur = conn.cursor()
cur.copy_expert(sql, out_file)


conn.close()





