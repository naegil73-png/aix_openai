# SQL의 galleryList 테이블에 자료 넣기 명령문
# 실행에 필요한 파일, 환경변수 찾아 실행하고 oracle에 접속(접속정보 이용), 

import json # json 파일 읽고 저장 위해 필요
import os # 환경변수, 경로 변경
from pathlib import Path # 파일, 폴더 경로
import oracledb # 오라클 DB에 접속하기 위해 SQL실행
from dotenv import load_dotenv # SQL 실행을 위해 로그인 파일 필요

# galleryList.json을 작업해야 하므로 이 파일과 env파일을 먼저 찾기 위해 
# 현재 작업중인 gallerylist.py의 위치를 기준으로 대상파일도 같이 찾을 수 있는 폴더 범위로 정함
base_dir = Path(__file__).resolve().parent # galleylist.json 파일이 있는 곳을 찾음
load_dotenv(base_dir /'db2'/'.env') # 환경변수는 load해야 함
gal_path = base_dir/'db2'/'galleryList.json' # 일반파일은 경로만 표시하고, 이후 open 등으로 실행

with open(gal_path,'r',encoding='utf-8') as f: # 파일을 읽는다.
    data = json.load(f)

items = data['response']['body']['items']['item']   # 찾을 대상을 표시

conn = oracledb.connect(                        # conn = oracledb.connect() : 파이썬과 오라클 사이를 연결한다.
    user=os.getenv('ora_id'),                   # 연결 시 오라클 id, pw, dsn 정보로 접속하라
    password = os.getenv('ora_pw'),
    dsn=os.getenv('ora_dsn'),
)
cur = conn.cursor()                             # 접속 통로에 작업자 cur를 만든다.
                                                # items에 있는 item에 대해서
                                                # 작업자 cur는 작업을 1번 시행하라. cur.execute(SQL문자열, 값리스트)
                                                # sql에 있는 테이블에 자료를 넣어라.
                                                # 직접 Data를 넣는 형태가 아닌, 변수에 담긴 파이썬 값을 쓸 때는 자리표시자 :1,:2,~:11을 씀
for i, item in enumerate(items, start=1):       
    cur.execute(                                
        '''INSERT INTO galleryList VALUES (      
        :1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11)''', 
    [
            i,
            item["galContentId"],
            item["galContentTypeId"],
            item["galTitle"],
            item["galWebImageUrl"],
            item["galCreatedtime"],
            item["galModifiedtime"],
            item["galPhotographyMonth"],
            item["galPhotographyLocation"],
            item["galPhotographer"],
            item["galSearchKeyword"],
    ],
    )
conn.commit()                                   # cur.execute하면 오라클의 임시작업공간에 올라가 있음 -> 이 명령으로 저장됨
print(f"저장완료: 총{len(items)}건 저장")          # 완료 메시지

cur.close()                                     # 작업자 종료
conn.close()                                    # 연결 종료