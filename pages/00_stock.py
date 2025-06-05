# stock_visualizer_app.py

import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
from datetime import datetime, timedelta

# 글로벌 시가총액 기준 Top 10 기업 (2025년 기준으로 추정된 티커 리스트)
top10_tickers = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Nvidia": "NVDA",
    "Saudi Aramco": "2222.SR",  # 사우디 증권거래소
    "Alphabet (Google)": "GOOGL",
    "Amazon": "AMZN",
    "Berkshire Hathaway": "BRK-B",
    "Meta (Facebook)": "META",
    "TSMC": "TSM",
    "Eli Lilly": "LLY"
}

# 날짜 범위 설정 (최근 1년)
end_date = datetime.today()
start_date = end_date - timedelta(days=365)

# Streamlit UI
st.title("📈 글로벌 시가총액 Top 10 기업의 최근 1년간 주가 변화")
st.markdown("데이터 출처: Yahoo Finance")

selected_companies = st.multiselect(
    "기업 선택:",
    options=list(top10_tickers.keys()),
    default=list(top10_tickers.keys())
)

if selected_companies:
    fig = go.Figure()

    for company in selected_companies:
        ticker = top10_tickers[company]
        data = yf.download(ticker, start=start_date, end=end_date)
        
        if not data.empty:
            fig.add_trace(go.Scatter(
                x=data.index,
                y=data["Adj Close"],
                mode='lines',
                name=company
            ))

    fig.update_layout(
        title="최근 1년간 주가 변화 (종가 기준)",
        xaxis_title="날짜",
        yaxis_title="주가 (USD)",
        template="plotly_white"
    )

    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("하나 이상의 기업을 선택해주세요.")
