import streamlit as st
import pandas as pd

st.title('실습 페이지')

data=pd.DataFrame({
    'color':['red','orange','blue','green','purple'],
    'score':[1,2,3,4,5],
    '승률 (%)':[30,30,20,15,5]
})

fig2=data.plot.pie(
    y='11',
    labels=data['color'],
    autopct='%1.1f%%',
    figsize=(6,6),
    legend=False,
    title='11'
).get_figure()

st.pyplot(fig2)

