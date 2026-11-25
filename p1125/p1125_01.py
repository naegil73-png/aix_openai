import oracledb
import os
from dotenv import load_dotenv

load_dotenv()
print(os.getenv('ora_id'))

# 오라클 db접속 방법
# 1번째
# conn = oracledb.connect(user='ora_user',password='1111',\
#                         dsn='localhost:1521/XE')
# 2번째
# conn = oracledb.connect('ora_user/1111@localhost:1521/XE')

#3번째
# conn = oracledb.connect(ora_conn)


conn = oracledb.connect('ora_user/1111@localhost:1521/XE')

cursor = conn.cursor()
sql = 'select * from stuscore'
cursor.execute(sql)


rows = cursor.fetchall()

for row in rows:
    print('{},{},{},{},{},{},{},{},{},{},{},{}'.format(*row))





# openai zl



# oracle 연결방법


import oracledb
import os
from dotenv import load_dotenv

load_dotenv()
print(os.getenv('ora_id'))

# 오라클 db접속
# conn = oracledb.connect(user='ora_user',password='1111',\
#                         dsn='localhost:1521/XE')

conn = oracledb.connect('ora_conn') # 간단히 이렇게 작성해도 됨

cursor = conn.cursor()
sql = 'select * from stuscore'
cursor.execute(sql)


rows = cursor.fetchall()

for row in rows:
    print('{},{},{},{},{},{},{},{},{},{},{},{}'.format(*row))