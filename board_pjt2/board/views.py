# sql을 이용해서 board, member에 모두 있는 id로
# bno,nickname,btitle,bcontent,bgroup,bstep,bindent,bhit,bdate를 
# 불러와서 게시판에 추가하라

# 고려사항 : sql에 접속하려면 oracle, 접속파일(.env파일), 다른 경로 폴더

from django.shortcuts import render
import os
from pathlib import Path
import oracledb
from dotenv import load_dotenv
from board.models import Board
# from board.models import Board

BASE_DIR = Path(__file__).resolve().parent.parent.parent
env_file = BASE_DIR / 'db2'/'.env'
load_dotenv(env_file)

# ora_conn = f"{os.getenv('ora_user')}/{os.getenv('ora_pw')}/{os.getenv('ora_dsn')}"

print("ENV KEYS:", [k for k in os.environ.keys() if "ora" in k.lower()])
def blist(request):
    # conn = oracledb.connect(ora_conn)
    conn = oracledb.connect(
    user=os.getenv("ORA_ID"),
    password=os.getenv("ORA_PW"),
    dsn=os.getenv("ORA_DSN"),
)
    cursor = conn.cursor()

    sql = ''' select bno, nickname, btitle, bcontent, bgroup, bstep, bindent, bhit, bdate 
    from board a, member b where a.id = b.id
'''
    cursor.execute(sql) # sql을 실행하면, oracledb는 열이름과 설명자료, 순수 자료를 분리해서 반환함
    columns = [col[0] for col in cursor.description] # cursor.description에는 'BNO', <DbType NUMBER>, ...이 있는데, 첫번째가 변수명임
    rows = cursor.fetchall() # 실행한 순수 자료를 모두 가져와라

    rows_list = []
    for row in rows:
        data = dict(zip(columns,row))
        if data['BCONTENT'] is not None and \
        hasattr(data['BCONTENT'],'read'):
            data['BCONTENT'] = data['BCONTENT'].read() # 본문 내용이 비어있지 않고, 읽기 기능이 있다면, 본문 내용을 읽어서 BCONTENT에 담아라
        rows_list.append(data)
    cursor.close()
    conn.close()
    context={'blist':rows_list}
    return render(request,'blist.html',context)

def blist2(request):
    qs = Board.objects.all()
    print('확인')
    context = {'blist':qs}
    return render(request,'blist2.html',context)