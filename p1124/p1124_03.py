import os
from pathlib import Path
from dotenv import load_dotenv
import openai
from openai import OpenAI

load_dotenv()
api_key = os.getenv('open_ai_key')
print(api_key)


# 디장고에 할 때는 views.py에서 작업하나, env파일은 다른 폴더에 있을 것임
# 파일 불러오기
BASE_DIR = Path(__file__).resolve().parent.parent
envFile = BASE_DIR / '.env'
print(BASE_DIR)

load_dotenv(envFile)
api_key = os.getenv('open_ai_key')
print(api_key)

# chat gpt 연결해서 진행
while True:
    txt_input = input('가고 싶은 여행지를 입력하세요.').strip()
    if txt_input:break
    print('여행지를 입력하셔야 검색이 가능합니다.')
    print()

# OoenAI client

# openai client 연결부분 - 글자생성, 이미지 생성, 음성 생성, 동영상 생성 -> 이 부분에 대한 요청이 중요함
client = OpenAI(api_key=api_key)

try:
    response = client.responses.create(
        model = 'gpt-5.6',
        instructions = (
            '당신은 여행설계 전문가입니다.'
            '여행 일정을 1박2일 코스, 2박 3일 코스를 설계해 주세요.'
            '[기차여행],[버스여행]으로 알려주세요.'
            '여행자가 이해하기 쉽게 간략하게 답합니다.'
        ),
        input = f'{txt_input}를 가지고 [1박2일 코스]-버스여행, 여행지, 숙소, 식사 등을 제안해 주세요.',
        max_output_tokens=100,
    )


except openai.APIConnectionError as error:
    print(f"인터넷연결, 방화벽 문제 등 확인 요망:{error}")
except openai.RateLimitError as error:
    print(f"요청량 또는 프로젝트 사용한도 확인:{error}")
except openai.APIError as error:
    print(f"인증, 권한 등 api 오류 확인:{error}")

# ------------------결과 확인 ----------------------------------

result = response.output_text.strip()
if not result:
    raise RuntimeError('응답결과 내용이 없습니다.')

print(f'[{txt_input} 여행정보]')
print(result)