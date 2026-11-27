from django.shortcuts import render
import oracledb
from dotenv import load_dotenv

def index(request):
    return render(request, 'index.html')

