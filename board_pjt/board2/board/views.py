from django.shortcuts import render
import os
from pathlib import Path
from dotenv import load_dotenv
import oracledb

# 환경변수 가져와서 로드
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
load_dotenv(BASE_DIR/'.env')

# 오라클에 연결(연결을 위한 모듈로 oracledb를 가져옴 -> 연결하라 = 오라클에 연결하라는 의미)
ora_conn = os.getenv('ora_conn') # cra_conn에 id,pw,dsn 모두 포함

def blist(request):
    conn = oracledb.connect(ora_conn)