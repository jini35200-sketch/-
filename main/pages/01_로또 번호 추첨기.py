import streamlit as st
import random

st.title("🎲 로또 번호 생성기")

# 게임 수 입력 (1~10)
game_count = st.number_input("생성할 게임 수를 입력하세요 (1~10)", min_value=1, max_value=10, value=1)

# '생성' 버튼
if st.button("번호 생성"):
    st.subheader(f"총 {game_count}게임의 로또 번호 추천 💡")
    
    for i in range(game_count):
        # 1~45 중 6개 무작위 선택
        lotto = sorted(random.sample(range(1, 46), 6))
        st.write(f"🎯 게임 {i+1}: ", lotto)
