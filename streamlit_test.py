import pandas as pd
import streamlit as st


df_stock=pd.read_csv('stock_data/df_stock.csv')

df_stock.sort_values(by=['Symbol','timestamp'],inplace=True)

df_stock.reset_index(inplace=True)

df_stock_rolling=df_stock.groupby(by='Symbol')['close'].ewm(alpha=0.6).mean().round(2)

df_stock_rolling.reset_index(drop=True,inplace=True)

df_stock=pd.merge(left=df_stock,right=df_stock_rolling,left_index=True,right_index=True,suffixes=('','_ewm'))

stock_select=st.selectbox(label='stock selector',options=set(df_stock['Symbol']),placeholder='Choose an option')

st.dataframe(df_stock[df_stock['Symbol']==stock_select])

st.line_chart(data=df_stock[df_stock['Symbol']==stock_select],x='timestamp',y=['close','close_ewm'],color=['#0000FF','#f44336'])

