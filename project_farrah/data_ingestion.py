#!/usr/bin/env python
# coding: utf-8

# In[7]:


import psycopg2
import os
import sys

# In[8]:
table_name=sys.argv[1]

host=os.environ['POSTGRES_HOST']
dbname=os.environ['POSTGRES_DB']
user=os.environ['POSTGRES_USER']
port=os.environ['POSTGRES_PORT']
password=os.environ['POSTGRES_PASSWORD']

conn = psycopg2.connect(host=host, dbname=dbname, user=user, port=port, password=password)


# In[11]:


#out_file=open("customers.csv",'w')

out_file=open(f"{table_name}.csv",'w')
# In[12]:


sql="copy (select * from olist_customers_dataset_csv limit 100) to stdout csv header"


# In[13]:


cur = conn.cursor()
cur.copy_expert(sql, out_file)
cur.close()


# In[ ]:




conn.close()

