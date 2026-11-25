import oracledb
import os
from dotenv import load_dotenv

# oracle접속정보 - sql정보를 더블클릭
load_dotenv()
ora_conn = os.getenv('ora_conn')
conn = oracledb.connect(ora_conn)
# print(conn.version)

# 커서연결 - sql명령어 창연결
cursor = conn.cursor()

# 실행문
sql = '''select substr(period,1,4) year,
to_char(sum(loan_jan_amt)*100000,'L999,999,999,999,999')
from kor_loan_status
where substr(period,1,4)>=2012
group by substr(period,1,4)'''
cursor.execute(sql)

# 데이터 연결
# rows타입은 [( )]
rows = cursor.fetchall()
print(rows)
cursor.close()
conn.close()
# for row in rows:
#     print(row)

# row 타입 ()
# row = cursor.fetchone()
# print(row)