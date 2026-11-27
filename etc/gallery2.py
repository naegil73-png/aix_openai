import oracledb
from pathlib import Path
import os
import json
from dotenv import load_dotenv

base_dir = Path(__file__).resolve().parent
load_dotenv(base_dir /'db2'/'.env')
gallery = base_dir/'db2'/'gallery.json'

with open(gallery,'r',encoding='utf-8') as f:
    data = json.load(f)