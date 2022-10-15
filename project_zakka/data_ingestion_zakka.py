#!/usr/bin/env python
# coding: utf-8

# In[3]:


import psycopg2
import os
import sys

table_name = sys.argv[1]


# In[10]:


#get credentials
host = os.environ['POSTGRES_HOST']
dbname = os.environ['POSTGRES_DB']
user = os.environ['POSTGRES_USER']
port = os.environ['POSTGRES_PORT']
password = os.environ['POSTGRES_PASSWORD']

conn = psycopg2.connect(host=host, dbname=dbname, user=user, port=port, password=password)


# In[11]:


out_file = open(f"{table_name}.csv", "w")


# In[12]:


sql = f"copy (SELECT * FROM {table_name} LIMIT 100) to stdout csv header"


# In[13]:


cur = conn.cursor()
cur.copy_expert(sql, out_file)
cur.close()


# In[14]:


conn.close()


# In[ ]:




