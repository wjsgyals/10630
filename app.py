import streamlit as st
from openai import OpenAI

client = OpenAI(
    api_key="여기에_API키"
)

st.title("💕 AI 연애 코치")

user_input = st.text_area("연애 고민 입력")

if st.button("상담받기"):

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "너는 다정한 연애 상담가다."
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    answer = response.choices[0].message.content

    st.write(answer)
