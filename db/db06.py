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
# employees, emprank 두 파일을 non-equi를 이용해서 월급의 등급을 출력하시오
# -- 연봉이 4천이하 E등급, 
# 4천~7천 미만 D등급, 
# 7천~1억 미만 C등급, 
# 1억~1억2천미만 B등급, 
# 1억 2천~3억 A등급


# employees, departments 파일 이용해서 - emp_name,department_id,department_name을 출력
sql = 'select name,kor+eng+math total,sw from stuscore'
cursor.execute(sql)

# 컬럼명을 추출
columns = [col[0] for col in cursor .description]
print(cursor.description)
print(columns)


# sql = '''select emp_name, salary, e_rank2 from employees, salrank2 
#         where salary between low_sal2 and high_sal2 '''
# cursor.execute(sql)

# 4.데이터 정보전달
rows = cursor.fetchall()
print(rows)

# 4-2. 딕셔너리 형태로 변환
rows = [dict(zip(columns,row)) for row in rows]
print(rows)

# return render('index.html',context={'stulist':rows})

# 5.데이터 출력
# for row in rows:
#     print(row[0],row[1],row[2],row[3])
    

#  5-2. insert, update, delete할 경우
# insert - board
# insert - file1
# insert - file2
# insert - file3


# cursor.commit()
# cursor.rollback()

# 6. db정보 닫기
cursor.close()
conn.close()