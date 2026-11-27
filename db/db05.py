import os
import oracledb
from dotenv import load_dotenv

# 1.불러오기
load_dotenv()
ora_conn= os.getenv('ora_conn')
print(ora_conn)

# 2.db연결
conn = oracledb.connect(ora_conn)
cursor = conn.cursor()
print(conn)
# 이후 sql작업

# 3.쿼리작성실행
sql = 'select * from stuscore'
cursor.execute(sql)

# 4.데이터 정보전달
rows = cursor.fetchall()

# 5.데이터 출력
for row in rows:
    print(row[0],row[1],row[2],row[3])
    

#  5-2. insert, update, delete할 경우
# insert - board
# insert - file1
# insert - file2
# insert - file3


cursor.commit()
cursor.rollback()

# 6. db정보 닫기
cursor.close()
conn.close()