import streamlit as st

st.title('오늘은 신나는 월요알')
st.header('오늘은 Streamlit 배우는 날~~')
st.subheader('Streamlit으로 만들어 보는 내 사이트!')

my_site=st.text_input('오늘 내가 만들어 보고 싶은 사이트는?') # input 박스 생성
# print(my_site) # 터미널 출력용
st.write(my_site) 

if st.button(f'{my_site} 접속하기'):
    st.success(f'{my_site}로 접속중 ')

