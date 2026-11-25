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
while True:
    kor = int(input('국어점수 입력값 이상 점수를 검색함(ex:50점)'))
    if kor == '': break
    # 실행문
    sql = f'select * from stuscore where kor >= {kor}'
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

# kor+eng+math/3 평균 80점 이상인 사람을 출력하시오.

while True:
    kor = int(input('(ex:50점)'))
    eng = int(input('(ex:50점)'))
    math = int(input('(ex:50점)'))
    avg = (kor+eng+math)/3
    if kor == '': break
    # 실행문
    sql = f'select * from stuscore where {avg} >= 80'}
    cursor.execute(sql)




# 이름에 a가 포함된 학생을 출력하시오.
while True:






# 국어, 영어, 수학 점수를 역순정렬하시오.