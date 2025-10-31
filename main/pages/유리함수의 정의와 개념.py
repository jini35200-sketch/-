import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="유리함수의 정의와 개념", layout="centered")

st.title("📘 유리함수의 정의와 개념")

# 1️⃣ 도입
st.markdown("""
### 🌟 유리함수란?
유리함수는 **두 다항식의 비로 나타내어진 함수**입니다.  
즉, 다음과 같은 형태로 쓸 수 있습니다.
$$ f(x) = \\frac{P(x)}{Q(x)}, \\quad (Q(x) \\neq 0) $$

예를 들어,  
- \\( f(x) = \\frac{1}{x} \\)  
- \\( f(x) = \\frac{2}{x-1} \\)  
- \\( f(x) = \\frac{x+1}{x} \\)  
등이 모두 유리함수입니다.
""")

# 2️⃣ 함수 선택
st.subheader("함수를 선택해보세요 👇")
option = st.selectbox(
    "유리함수를 선택하세요",
    ["f(x) = 1/x", "f(x) = 2/x", "f(x) = 1/(x-2)", "f(x) = (x+1)/x"]
)

x = np.linspace(-10, 10, 400)
y = None

if option == "f(x) = 1/x":
    y = 1/x
    func = r"f(x)=\frac{1}{x}"
    asymp_x, asymp_y = 0, 0
elif option == "f(x) = 2/x":
    y = 2/x
    func = r"f(x)=\frac{2}{x}"
    asymp_x, asymp_y = 0, 0
elif option == "f(x) = 1/(x-2)":
    y = 1/(x-2)
    func = r"f(x)=\frac{1}{x-2}"
    asymp_x, asymp_y = 2, 0
elif option == "f(x) = (x+1)/x":
    y = (x+1)/x
    func = r"f(x)=\frac{x+1}{x}"
    asymp_x, asymp_y = 0, 1

# 3️⃣ 그래프
fig, ax = plt.subplots()
ax.set_ylim(-10, 10)
ax.axhline(0, color='gray', linestyle='--')  # x축
ax.axvline(0, color='gray', linestyle='--')  # y축

# 수직/수평 아심프토트 표시
if asymp_x != 0:
    ax.axvline(asymp_x, color='red', linestyle='--', label=f"x={asymp_x} (수직 아심프토트)")
if asymp_y != 0:
    ax.axhline(asymp_y, color='blue', linestyle='--', label=f"y={asymp_y} (수평 아심프토트)")

ax.plot(x, y, color='black', label=func)
ax.legend()
ax.grid(True)
st.pyplot(fig)

# 4️⃣ 개념 정리
st.subheader("📘 핵심 개념 정리")
if option == "f(x) = 1/x":
    st.markdown("""
    - 정의역: x ≠ 0  
    - 그래프는 원점을 기준으로 **점대칭**
    - 수직 아심프토트: x = 0  
    - 수평 아심프토트: y = 0
    """)
elif option == "f(x) = 2/x":
    st.markdown("""
    - 정의역: x ≠ 0  
    - y값이 2배 커져서 그래프가 위아래로 퍼짐  
    - 수직 아심프토트: x = 0  
    - 수평 아심프토트: y = 0
    """)
elif option == "f(x) = 1/(x-2)":
    st.markdown("""
    - 정의역: x ≠ 2  
    - 그래프가 오른쪽으로 2만큼 이동  
    - 수직 아심프토트: x = 2  
    - 수평 아심프토트: y = 0
    """)
elif option == "f(x) = (x+1)/x":
    st.markdown("""
    - 정의역: x ≠ 0  
    - 수직 아심프토트: x = 0  
    - 수평 아심프토트: y = 1  
    - 그래프가 전체적으로 위로 1만큼 이동
    """)

# 5️⃣ 간단 퀴즈
st.subheader("🧩 퀴즈")
st.write("아래 문제의 답을 입력해보세요!")

if option == "f(x) = 1/(x-2)":
    answer = st.text_input("이 함수의 정의역은 무엇인가요?")
    if answer:
        if "x≠2" in answer or "x != 2" in answer:
            st.success("정답이에요! ✅")
        else:
            st.error("아쉽지만 다시 생각해보세요. 😅")
else:
    answer = st.text_input("이 함수의 수직 아심프토트는 어디인가요? (예: x=0)")
    if answer:
        correct = asymp_x
        if f"x={correct}" in answer or f"x = {correct}" in answer:
            st.success("정답이에요! ✅")
        else:
            st.error("다시 확인해보세요.")

st.caption("© 2025. 고1 수학 I 디지털 교과서 제작 프로젝트 예시 by Streamlit")
