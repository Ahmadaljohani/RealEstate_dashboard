import streamlit as st
import pandas as pd
import numpy as np

import plotly.express as px
import seaborn as sns
 
 
st.sidebar.header('Real Estate Dashboard')
st.sidebar.write('The dashboard represente United States Real Estate Marketing')
st.sidebar.write('')
st.sidebar.write('Catogarail Filter')
cat_filter= st.sidebar.selectbox('Categorical Filter', [None,'Region','Home Size'])
num_filter=st.sidebar.selectbox('Numerical Filter', [None,'Average Sales Price','Mean Income - 2022 Dollars','Number of Households (Thousands)','Median Income - 2022 Dollars'])
row_filter=st.sidebar.selectbox('Row Filter', [None,'Region','Home Size'])
col_filter=st.sidebar.selectbox('Column Filter', [None,'Region','Home Size'])

st.sidebar.write('')
st.sidebar.markdown('Made with :smile: by Mr. [Ahmad Aljohani](www.linkedin.com/in/ahmad-aljohani-773854188)')

df=pd.read_csv('C:/Users/ahmad/OneDrive/المستندات/RealEstateUnitedStates.csv')
df['Year']=df['Year'].astype('object')


#row a
a1 ,a2 ,a3 = st.columns(3)
a1.metric('Max Averge sales Price ', df['Average Sales Price'].max())
a2.metric('Max Mean Income - 2022 Dollars ', df['Mean Income - 2022 Dollars'].max())
a3.metric('Max Median Income - 2022 Dollars ', df['Median Income - 2022 Dollars'].max())

#row b

fig= px.scatter(data_frame=df , x= 'Year' , y= 'Average Sales Price'
                , color=cat_filter 
                , size=num_filter,
                 facet_row=row_filter
                ,facet_col=col_filter )
st.plotly_chart(fig, use_container_width=True)

#row c
b1, b2 ,b3 = st.columns((4,3,3))
with b1:
    st.text('Home Size Vs Averge Sales Price')
    fig= px.bar(data_frame=df , x='Home Size'
                , y='Average Sales Price')
    st.plotly_chart(fig , use_container_width=True)

with b2:
    st.text('Region Vs Averge Sales Price')
    fig= px.pie(data_frame=df , names='Region'
                , values='Average Sales Price', color=cat_filter)
    st.plotly_chart(fig , use_container_width=True)

with b3:
    st.text('Home Size Vs Number of Households (Thousands)')
    fig= px.pie( data_frame=df , names='Home Size' , values='Number of Households (Thousands)', color=cat_filter
                , hole=0.4)
    st.plotly_chart(fig , use_container_width=True)

