import streamlit as st

# 앱 제목 설정
st.title("🔢 세 정수 중 가장 큰 수 찾기")
st.write("세 개의 정수를 입력하면 가장 큰 수를 찾아줍니다.")

# 1. 기존 input()을 st.number_input()으로 변경
# step=1을 설정하여 정수(int)만 입력받도록 합니다.
num1 = st.number_input("첫 번째 정수를 입력하세요", value=0, step=1)
num2 = st.number_input("두 번째 정수를 입력하세요", value=0, step=1)
num3 = st.number_input("세 번째 정수를 입력하세요", value=0, step=1)

# 값을 확인하고 결과를 보여줄 버튼 생성
if st.button("가장 큰 수 찾기"):
    
    # ----------------------------------------------------
    # [원본 로직 유지] 작성하신 조건문 알고리즘을 그대로 가져왔습니다.
    if num1 > num2:
        if num1 > num3:
            max_num = num1
        else:
            max_num = num3
    else:
        if num2 > num3:
            max_num = num2
        else:
            max_num = num3
    # ----------------------------------------------------
    
    # 2. 기존 print() 대신 st.success()를 사용해 화면에 예쁘게 출력
    st.success(f"입력한 숫자 중 가장 큰 수는 **{max_num}** 입니다.")