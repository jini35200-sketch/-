import streamlit as st

st.title("📘 유리함수, 쉽게 배우는 교과서")

st.header("1️⃣ 유리함수의 개념")

st.markdown("""
유리함수는 **나누기(÷)** 가 들어 있는 함수입니다.  

예를 들어,  
- f(x) = 1 ÷ x  
- f(x) = (2x + 1) ÷ (x - 3)  
이런 식이 유리함수입니다.  

유리함수에서는 **나누는 수(분모)** 가 0이 되면 계산할 수 없습니다.  
그래서 **x가 분모를 0으로 만드는 값은 사용할 수 없습니다.**

또한, 유리함수의 그래프는 **쌍곡선처럼 양쪽으로 휘어진 모양**입니다.  
예를 들어 **f(x) = 1 ÷ (x - 2)** 라면,  
x가 2일 때 그래프가 끊어지고,  
그 부분을 **수직점근선**이라고 합니다.  
""")

st.divider()

# OX 문제
st.header("2️⃣ O/X 문제로 확인하기")

score = 0

q1 = st.radio("① 유리함수는 나누기(÷)가 들어 있는 함수입니다.", ["O", "X"])
if q1 == "O":
    score += 1

q2 = st.radio("② 유리함수에서는 나누는 수(분모)가 0이 되어도 됩니다.", ["O", "X"])
if q2 == "X":
    score += 1

q3 = st.radio("③ 유리함수의 그래프는 쌍곡선 모양입니다.", ["O", "X"])
if q3 == "O":
    score += 1

if st.button("O/X 채점하기"):
    st.success(f"총 {score}문제를 맞혔습니다! 🎉")

st.divider()

# 빈칸 문제
st.header("3️⃣ 빈칸 채우기 문제")

st.markdown("아래 문장을 읽고 알맞은 말을 넣어보세요 👇")

a1 = st.text_input("① 유리함수는 (    )가 들어 있는 함수입니다.")
a2 = st.text_input("② (    )가 0이 되면 유리함수는 정의되지 않습니다.")
a3 = st.text_input("③ 유리함수의 그래프는 (    ) 모양입니다.")
a4 = st.text_input("④ 그래프가 끊어지는 부분을 (    )이라고 합니다.")

if st.button("채점하기"):
    correct = 0
    if a1.strip() in ["나누기", "나누기(÷)"]:
        correct += 1
    if a2.strip() in ["분모", "나누는 수"]:
        correct += 1
    if a3.strip() == "쌍곡선":
        correct += 1
    if a4.strip() == "수직점근선":
        correct += 1

    st.info(f"정답은 {correct}/4개입니다. 💪")

    st.markdown("""
    **정답 확인**  
    ① 나누기(÷)  
    ② 분모  
    ③ 쌍곡선  
    ④ 수직점근선
    """)

st.divider()

st.caption("© 2025 유리함수 학습 교과서 – 만든이: 백지니")
