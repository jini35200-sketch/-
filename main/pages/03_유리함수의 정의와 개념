# 파일명: rational_function_basic.py
# 스트림릿: 고1 수준 유리함수 정의와 개념 학습용 앱

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="유리함수의 정의와 개념", layout="centered")

st.title("📘 유리함수의 정의와 개념")
st.write("""
**유리함수(rational function)**란  
분자와 분모가 모두 다항식인 함수로, 보통 다음과 같이 표현됩니다.

\[
f(x) = \frac{P(x)}{Q(x)}, \quad (Q(x) \neq 0)
\]

이 앱에서는 간단한 유리함수를 입력하고  
그래프를 통해 **정의역**, **점근선**, **절편** 등을 관찰할 수 있습니다.
""")

st.divider()

# --- 사용자 입력 ---
st.subheader("1️⃣ 유리함수 입력")
col1, col2 = st.columns(2)
with col1:
    st.write("**분자 P(x)** (예: x, x+1, 2x-3 등)")
    num_expr = st.text_input("분자", value="x", key="num")
with col2:
    st.write("**분모 Q(x)** (예: x-1, x+2 등)")
    den_expr = st.text_input("분모", value="x-1", key="den")

# --- 함수 계산용 ---
x = np.linspace(-10, 10, 1000)
try:
    # 안전한 평가
    allowed = {"x": x, "np": np}
    y = eval(f"({num_expr})/({den_expr})", {"__builtins__": {}}, allowed)
except Exception:
    st.error("식을 올바르게 입력하세요. 예: x/(x-1), (x+1)/(x-2)")
    st.stop()

# --- 그래프 영역 ---
st.subheader("2️⃣ 그래프 관찰")

fig, ax = plt.subplots(figsize=(7,4))
ax.plot(x, y, label=r"$f(x)=\frac{%s}{%s}$" % (num_expr, den_expr))
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.set_ylim(-10, 10)
ax.set_xlim(-10, 10)
ax.grid(True, linestyle=':')
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.legend()

st.pyplot(fig)

st.caption("⚠️ 분모가 0이 되는 곳에서는 함수값이 정의되지 않아 그래프가 끊어집니다.")

# --- 성질 계산 ---
st.subheader("3️⃣ 함수의 성질 알아보기")

# 수직점근선 (분모=0 되는 값)
try:
    den_roots = np.roots(np.polyfit(x, eval(den_expr, {"__builtins__": {}}, {"x": x, "np": np}), 0))
except:
    den_roots = []

# 정의역: 분모가 0이 되는 x 제외
st.markdown(f"**정의역:** 분모가 0이 되는 x값을 제외한 모든 실수")

# 수직점근선 찾기 (근사)
from sympy import symbols, solve, sympify
X = symbols('x')
try:
    denom_sym = sympify(den_expr)
    asym_x = solve(denom_sym, X)
    asym_x = [float(a) for a in asym_x if a.is_real]
except:
    asym_x = []

if len(asym_x) > 0:
    st.write("**수직점근선:**", ", ".join([f"x = {a}" for a in asym_x]))
else:
    st.write("**수직점근선:** 없음 (분모가 0이 되는 실수 x가 없음)")

# 수평점근선 판단
num_deg = sympify(num_expr).as_poly(X).degree()
den_deg = sympify(den_expr).as_poly(X).degree()
if num_deg < den_deg:
    st.write("**수평점근선:** y = 0")
elif num_deg == den_deg:
    lc_num = sympify(num_expr).as_poly(X).LC()
    lc_den = sympify(den_expr).as_poly(X).LC()
    st.write(f"**수평점근선:** y = {lc_num/lc_den}")
else:
    st.write("**수평점근선:** 없음 (분자의 차수가 더 큼)")

# 절편 계산
try:
    f0 = eval(f"({num_expr})/({den_expr})", {"__builtins__": {}}, {"x":0, "np":np})
    st.write(f"**y절편:** (0, {f0:.2f})")
except:
    st.write("**y절편:** 분모가 0이 되어 존재하지 않음")

# x절편
try:
    num_sym = sympify(num_expr)
    x_zeros = solve(num_sym, X)
    real_zeros = [float(z) for z in x_zeros if z.is_real]
    st.write("**x절편:** " + ", ".join([f"({z:.2f}, 0)" for z in real_zeros]))
except:
    st.write("**x절편:** 계산 불가")

st.divider()

st.subheader("📖 개념 정리")
st.markdown("""
- **유리함수의 정의**: 분모와 분자가 다항식인 함수  
  \\( f(x) = \\frac{P(x)}{Q(x)}, Q(x)\\neq 0 \\)
- **정의역**: 분모가 0이 되는 x를 제외한 모든 실수  
- **수직점근선**: 분모가 0이 되는 실수 x의 위치  
- **수평점근선**:
  - 분자 차수 < 분모 차수 → y=0  
  - 분자 차수 = 분모 차수 → y=계수비  
- **절편**:
  - x절편: 분자가 0이 되는 x값  
  - y절편: x=0일 때 함수값
""")

st.divider()
st.subheader("🎯 탐구 활동 예시")
st.markdown("""
1. \( f(x) = \frac{x}{x-1} \) 을 입력하고 그래프에서 수직·수평점근선을 찾아보세요.  
2. \( f(x) = \frac{x^2}{x} \), \( f(x) = \frac{x}{x^2} \) 를 비교하여 차수가 점근선에 미치는 영향을 관찰하세요.  
3. \( f(x) = \frac{x-1}{x+2} \) 의 정의역과 점근선을 설명해보세요.
""")
