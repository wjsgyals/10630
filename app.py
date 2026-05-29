import streamlit as st
import random

st.title("💕 AI 연애 코치")

user_input = st.text_area("연애 고민을 입력하세요")

answers = [
    "상대방 마음을 너무 조급하게 확인하려 하지 마세요 😊",
    "지금은 진심 있는 대화가 가장 중요해 보여요.",
    "너무 혼자 끙끙 앓지 말고 솔직하게 표현해보세요.",
    "상대 입장에서도 생각해보면 도움이 될 거예요.",
    "연애는 타이밍도 정말 중요해요 💕",
    "자신감을 가지는 모습이 더 매력적으로 보여요.",
    "억지로 관계를 끌고 가려고 하지 않아도 괜찮아요.",
    "가볍게 연락하면서 분위기를 편하게 만들어보세요."
]

if st.button("상담받기"):

    if user_input == "":
        st.warning("고민을 입력해주세요!")
    else:
        answer = random.choice(answers)

        st.write("### AI 답변")
        st.success(answer)
