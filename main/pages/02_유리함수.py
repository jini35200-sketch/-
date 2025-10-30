 import streamlit as st
import random

st.title("📘 유리함수 문제풀이 O/X 맞추기")

# -----------------------------
# 1️⃣ 난이도 선택
# -----------------------------
difficulty = st.number_input("난이도를 선택하세요 (1~6)", min_value=1, max_value=6, step=1)

# -----------------------------
# 2️⃣ 문제 데이터베이스 (예시)
# -----------------------------
problems = {
    1: [
        {"question": "함수 f(x) = 1/x 는 정의역이 모든 실수이다.", "solution": "0에서는 정의되지 않으므로 틀림.", "answer": "X"},
        {"question": "f(x) = 2/x 에서 x=1일 때 f(x)=2이다.", "solution": "x=1 넣으면 f(1)=2/1=2 → 맞음.", "answer": "O"},
    ],
    2: [
        {"question": "f(x)=3/(x-1) 의 점근선은 x=1 이다.", "solution": "분모가 0이 되는 x=1 → 맞음.", "answer": "O"},
        {"question": "f(x)=1/(x+2) 는 x=-2에서 정의된다.", "solution": "x=-2에서 분모 0 → 정의되지 않음.", "answer": "X"},
    ],
    3: [
        {"question": "f(x)=1/(x-2)+3 의 수평점근선은 y=3이다.", "solution": "유리함수의 기본형 a/(x-h)+k → 수평점근선 y=k=3", "answer": "O"},
        {"question": "f(x)=2/(x+1) 의 수직점근선은 x=2 이다.", "solution": "분모 0 → x=-1, 따라서 x=2 아님.", "answer": "X"},
    ],
    4: [
        {"question": "f(x)=1/(x-3)+2 의 그래프는 y축 대칭이다.", "solution": "x→-x 대입 시 형태 달라짐 → 대칭 아님.", "answer": "X"},
        {"question": "f(x)=1/(x-2)+1 은 점 (3,2)를 지난다.", "solution": "f(3)=1/(3-2)+1=2 → 맞음.", "answer": "O"},
    ],
    5: [
        {"question": "f(x)=1/x 의 그래프를 x축으로 대칭이동하면 f(x)=-1/x.", "solution": "x축 대칭 → y 부호 바뀜 → 맞음.", "answer": "O"},
        {"question": "f(x)=1/x 를 y축으로 대칭이동하면 f(x)=1/x.", "solution": "y축 대칭 → x→-x → f(x)=1/(-x)=-1/x → 달라짐.", "answer": "X"},
    ],
    6: [
        {"question": "f(x)=2/(x-1)+3 의 정의역은 x≠1 이다.", "solution": "분모 0 되는 x=1 제외 → 맞음.", "answer": "O"},
        {"question": "f(x)=1/(x-4)-2 의 수평점근선은 y=-4 이다.", "solution": "기본형 a/(x-h)+k → 수평점근선 y=k=-2 → 틀림.", "answer": "X"},
    ]
}

# -----------------------------
# 3️⃣ 문제 생성
# -----------------------------
if st.button("문제 생성"):
    problem = random.choice(problems[difficulty])
    st.session_state["problem"] = problem

# -----------------------------
# 4️⃣ 문제 표시 및 풀이 확인
# -----------------------------
if "problem" in st.session_state:
    problem = st.session_state["problem"]

    st.subheader("문제 📖")
    st.write(problem["question"])

    st.text_area("풀이 보기", problem["solution"], height=100)

    st.write("정답을 선택하세요 👇")
    user_answer = st.radio("당신의 선택:", ["O", "X"])

    if st.button("정답 확인"):
        if user_answer == problem["answer"]:
            st.success("🎉 축하합니다! 정답입니다!")
        else:
            st.error("❌ 다시 생각해보세요.")
