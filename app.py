import streamlit as st
st.title('집에 가고싶다')
st.write('집에 가고싶다')
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# 환경변수 로드
load_dotenv()

# OpenAI 클라이언트
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# 페이지 설정
st.set_page_config(
    page_title="AI 연애 코치",
    page_icon="💕",
    layout="centered"
)

# 제목
st.title("💕 AI 연애 코치")
st.caption("연애 고민을 편하게 이야기해보세요.")

# 세션 상태 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []

# 이전 대화 출력
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 사용자 입력
user_input = st.chat_input("연애 고민을 입력하세요")

if user_input:

    # 사용자 메시지 저장
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # 사용자 메시지 출력
    with st.chat_message("user"):
        st.markdown(user_input)

    # AI 응답 영역
    with st.chat_message("assistant"):

        with st.spinner("생각 중..."):

            try:
                response = client.chat.completions.create(
                    model="gpt-4.1-mini",
                    messages=[
                        {
                            "role": "system",
                            "content": """
너는 공감 능력이 뛰어난 연애 코치다.
비난하지 말고 현실적인 조언을 제공해라.
답변은 따뜻하고 자연스럽게 작성해라.
"""
                        },
                        *st.session_state.messages
                    ],
                    temperature=0.8,
                    max_tokens=500
                )

                ai_reply = response.choices[0].message.content

                st.markdown(ai_reply)

                # 저장
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": ai_reply
                })

            except Exception as e:
                st.error(f"오류 발생: {e}")
5. requirements.txt
streamlit
openai
python-dotenv
6. 실행
streamlit run app.py

추가하면 좋은 기능:

연애 스타일 분석
MBTI 기반 코칭
카톡 답장 추천
썸 가능성 분석
재회 상담 모드
남녀 시점 변환
음성 상담
익명 저장
감정 분석 그래프

UI도 예쁘게 꾸밀 수 있습니다:

st.markdown(
    """
    <style>
    .stApp {
        background-color: #fff5f7;
    }
    </style>
    """,
    unsafe_allow_html=True
)
