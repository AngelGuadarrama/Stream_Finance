import streamlit as st
import yfinance as yf
import pandas as pd
import cufflinks as cf
import datetime

# App title
st.markdown('''
# Choose the stock you want, the period, the start and finish date
''')
st.write('---')

# Sidebar
st.sidebar.subheader('Parameters')
start_date = st.sidebar.date_input("Start date", datetime.date(2019, 2, 28))
end_date = st.sidebar.date_input("End date", datetime.date(2021, 2, 28))

# Retrieving tickers data
ticker_list = pd.read_csv('https://github.com/AngelGuadarrama/Stream_Finance/blob/main/ipc_symbols.txt')
tickerSymbol = st.sidebar.selectbox('Stock ticker', ticker_list) # Select ticker symbol

ticker_periods= ['1d','5d','1mo','3mo','6mo','1y','2y','5y','10y','ytd','max']
ticker_period = st.sidebar.selectbox('Stock period', ticker_periods) # Select ticker symbol

tickerData = yf.Ticker(tickerSymbol) # Get ticker data
tickerDf = tickerData.history(period= ticker_period, start=start_date, end=end_date) #get the historical prices for this ticker

# Ticker information
string_logo = '<img src=%s>' % tickerData.info['logo_url']
st.markdown(string_logo, unsafe_allow_html=True)

string_name = tickerData.info['longName']
st.header('**%s**' % string_name)

string_name = tickerData.info['sector']
st.write('**%s**' % string_name)

string_name = tickerData.info['country']
st.write('**%s**' % string_name)

string_name = tickerData.info['website']
st.write('**%s**' % string_name)

string_summary = tickerData.info['longBusinessSummary']
st.info(string_summary)

st.header('**Ticker data**')
st.write(tickerDf)

st.header('**Bollinger Bands**')
qf=cf.QuantFig(tickerDf,title='First Quant Figure',legend='top',name='GS')
qf.add_bollinger_bands()
fig = qf.iplot(asFigure=True)
st.plotly_chart(fig)
