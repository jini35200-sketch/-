import streamlit as st

st.title("📘 유리함수의 개념 교과서")

st.header("1️⃣ 유리함수의 개념 쉽게 이해하기")

st.markdown("""
유리함수는 **분모에 문자가 포함된 함수**를 말해요.  
예를 들어, \\( f(x) = \\frac{1}{x} \\) 나 \\( f(x) = \\frac{2x+1}{x-3} \\) 같은 형태예요.

이런 함수는 **분모가 0이 되는 값에서는 정의되지 않아요.**  
즉, **분모 = 0**이 되는 값은 함수의 정의역에서 제외돼요.

또한, 유리함수의 그래프는 **쌍곡선 모양**을 가지며,  
분모의 차수가 커지면 그래프의 모양도 달라지고,  
특히 분모의 0이 되는 부분에서 **수직점근선**이 생겨요.

예를 들어 \\( f(x) = \\frac{1}{x-2} \\) 라면,  
분모가 0이 되는 \\( x = 2 \\) 에서 그래프가 끊기고,  
그곳이 바로 수직점근선이에요.
""")

st.divider()

# OX 문제
st.header("2️⃣ O/X 문제로 확인하기")

score = 0

q1 = st.radio("① 유리함수는 분모가 0이 되어도 정의된다.", ["O", "X"])
if q1 == "X":
    score += 1

q2 = st.radio("② f(x) = 1/x 의 그래프는 쌍곡선이다.", ["O", "X"])
if q2 == "O":
    score += 1

q3 = st.radio("③ 유리함수의 수직점근선은 분모가 0이 되는 곳이다.", ["O", "X"])
if q3 == "O":
    score += 1

if st.button("O/X 채점하기"):
    st.success(f"총 {score}문제 정답입니다! 🎉")

st.divider()

# 빈칸 문제
st.header("3️⃣ 빈칸 채우기 (간단 서답형)")

st.markdown("아래 문장을 읽고 빈칸을 채워보세요 👇")

a1 = st.text_input("① 유리함수는 (    )에 문자가 포함된 함수이다.")
a2 = st.text_input("② 유리함수는 (    )이 0이 되는 값에서 정의되지 않는다.")
a3 = st.text_input("③ 유리함수의 그래프는 (    ) 모양이다.")
a4 = st.text_input("④ 분모가 0이 되는 부분에서 그래프는 (    )을 가진다.")

if st.button("채점하기"):
    correct = 0
    if a1.strip() == "분모":
        correct += 1
    if a2.strip() == "분모":
        correct += 1
    if a3.strip() == "쌍곡선":
        correct += 1
    if a4.strip() == "수직점근선":
        correct += 1

    st.info(f"정답 {correct}/4 개 맞췄어요! 💪")

    st.markdown("""
    **정답 확인**  
    ① 분모  
    ② 분모  
    ③ 쌍곡선  
    ④ 수직점근선
    """)

st.divider()

st.caption("© 2025 유리함수 학습 스트림릿 교과서 – 만든이: [백지니]")
