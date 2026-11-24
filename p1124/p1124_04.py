# 경제전문가로 가정
# 2027년 주식시세가 어떻게 될 지 알려주는 프로그램을 구현하시오.
# 반도체주, 전력시설주, 우주항공주 각각에 대한 설명, 1000자 이내로 짧게 설명요청

import os
from pathlib import Path
from dotenv import load_dotenv
import openai
from openai import OpenAI

load_dotenv()
api_key = os.getenv('open_ai_key')
print(api_key)

BASE_DIR = Path(__file__).resolve().parent.parent
envFile = BASE_DIR / '.env'
print(BASE_DIR)

load_dotenv(envFile)
api_key = os.getenv('open_ai_key')
print(api_key)

while True:
    txt = '2027년 주식시세가 어떻게 될 지 알려주세요'
    if txt: break
    print("입력하셔야 서비스를 이용할 수 있습니다.")
client = OpenAI(api_key=api_key)

try:
    response = client.responses.create(
        model = 'gpt-5.6',
        instructions=('경제전문가로 가정하고, 반도체주, 전력시설주, 우주항공주 각각에 대해 설명하되, 1000자 이내로 짧게 설명요청해 주세요'),
        input = f'{txt} 질문을 가지고, 2027년 주식투자 제안을 해 주세요.',
        max_output_tokens=1000
    )

except openai.APIConnectionError as error:
    print(f"인터넷 연결 확인 요망 : {error}")
except openai.RateLimitError as error:
    print(f"토큰 갯수 확인 요망 : {error}")
except openai.APIError as error:
    print(f"인터넷 연결 확인 요망 : {error}")

result = response.output_text.strip()
if not result:
    raise RuntimeError('응답결과 내용이 없습니다.')

print(f'[{txt}]')
print(result)