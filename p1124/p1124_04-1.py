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
    txt = '관광지는 경주, 계룡산, 설악산이고 각각에 대해서 출발지는 서울입니다. 1박2일 여행코스를 알려주세요'
    if txt: break
    print("입력하셔야 서비스를 이용할 수 있습니다.")
client = OpenAI(api_key=api_key)

try:
    response = client.responses.create(
        model = 'gpt-5.6',
        instructions=('당신은 여행전문 가이드입니다.입력한 관광지의 여행코스와 숙소, 순서를 제시해 주세요, 1000자 이내로 짧게 설명요청해 주세요'),
        input = f'{txt} 질문을 가지고, 여행코스 제안을 해 주세요.',
        max_output_tokens=1000
    )

    result = response.output_text.strip()
    if not result:
        raise RuntimeError('응답결과 내용이 없습니다.')

    print(f'[{txt}]')
    print(result)

    output_file = BASE_DIR / 'tourlist.csv'
    with open(output_file, 'w', encoding='utf-8-sig') as f:
        f.write(result)

    print('저장 완료 경로:', output_file.resolve())

except openai.APIConnectionError as error:
    print(f"인터넷 연결 확인 요망 : {error}")
except openai.RateLimitError as error:
    print(f"토큰 갯수 확인 요망 : {error}")
except openai.APIError as error:
    print(f"인터넷 연결 확인 요망 : {error}")