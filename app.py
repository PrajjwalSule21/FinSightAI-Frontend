import streamlit as st
import requests
import time
import os
from utils.utils import page_config, template_end, social_media
from dotenv import load_dotenv  
load_dotenv()

API_ENDPOINT = os.getenv("API_ENDPOINT")


page_config()


st.title("📊 FinSightAI - AI-Powered Stock Analyzer")
st.markdown("""
Welcome to FinSightAI, your AI-powered assistant for performing fundamental analysis on stock data.  
Enter your API Key and the ticker symbol of the company you want to analyze.
""")


st.sidebar.title("FinSightAI - Stock Analyzer")
st.sidebar.markdown("### 🔐 Enter Credentials")
api_key = st.sidebar.text_input("Lyzr X API Key", type="password")
symbol = st.sidebar.text_input("Ticker Symbol (e.g., AMZN, AAPL)").upper()


if st.button("🔍 Analyze"):

    if not api_key or not symbol:
        st.warning("👈 Please enter both API Key and Ticker Symbol at sidebar.")
    else:
        with st.spinner("🔄 Starting the FinSightAI engine... (Render cold start may take ~30s)"):
            time.sleep(2)  

        with st.spinner("📡 Collecting data from Alpha Vantage..."):
            time.sleep(2)

        with st.spinner("🧠 Generating AI analysis report..."):
            headers = {
                "x-api-key": api_key,
                "Content-Type": "application/json"
            }
            payload = {"symbol": symbol}

            try:
                response = requests.post(API_ENDPOINT, json=payload, headers=headers, timeout=90)

                if response.status_code == 200:
                    data = response.json()
                    st.success(f"✅ Report generated for {data['symbol']}")

                    fin = data["financial_data"]

                    # Company Overview
                    st.markdown("## 🏢 Company Overview")
                    overview = fin["overview"]
                    st.markdown(f"""
**Name:** {overview['Name']}  
**Symbol:** {overview['Symbol']}  
**Exchange:** {overview['Exchange']}  
**Sector:** {overview['Sector']}  
**Industry:** {overview['Industry']}  
**Market Cap:** ${int(overview['MarketCapitalization']) / 1e12:.2f} Trillion  
**Country:** {overview['Country']}  
**Website:** [Visit]({overview['OfficialSite']})  
                    """)

                    # Financial Ratios
                    st.markdown("## 💹 Key Financial Ratios")
                    ratios = fin["ratios"]
                    st.write({
                        "EPS": ratios["EPS"],
                        "P/E Ratio": ratios["P/E Ratio"],
                        "P/B Ratio": ratios["P/B Ratio"],
                        "Debt-to-Equity": ratios["Debt-to-Equity Ratio"],
                        "ROE (%)": f"{ratios['ROE'] * 100:.2f}",
                        "ROA (%)": f"{ratios['ROA'] * 100:.2f}",
                        "Gross Margin (%)": f"{ratios['Gross Margin'] * 100:.2f}",
                        "Net Profit Margin (%)": f"{ratios['Net Profit Margin'] * 100:.2f}",
                    })

                    # Income Statement
                    st.markdown("## 📄 Income Statement Highlights")
                    income = fin["income_statement"]
                    st.write({
                        "Total Revenue": f"${int(income['totalRevenue']) / 1e9:.2f} B",
                        "Gross Profit": f"${int(income['grossProfit']) / 1e9:.2f} B",
                        "Operating Income": f"${int(income['operatingIncome']) / 1e9:.2f} B",
                        "Net Income": f"${int(income['netIncome']) / 1e9:.2f} B",
                        "EBITDA": f"${int(income['ebitda']) / 1e9:.2f} B"
                    })

                    # Balance Sheet
                    st.markdown("## 🧾 Balance Sheet Highlights")
                    bs = fin["balance_sheet"]
                    st.write({
                        "Total Assets": f"${int(bs['totalAssets']) / 1e9:.2f} B",
                        "Total Liabilities": f"${int(bs['totalLiabilities']) / 1e9:.2f} B",
                        "Shareholder Equity": f"${int(bs['totalShareholderEquity']) / 1e9:.2f} B",
                        "Cash & Equivalents": f"${int(bs['cashAndCashEquivalentsAtCarryingValue']) / 1e9:.2f} B"
                    })

                    # Cash Flow
                    st.markdown("## 💵 Cash Flow Highlights")
                    cf = fin["cash_flow"]
                    st.write({
                        "Operating Cash Flow": f"${int(cf['operatingCashflow']) / 1e9:.2f} B",
                        "Capital Expenditures": f"${int(cf['capitalExpenditures']) / 1e9:.2f} B",
                        "Net Income": f"${int(cf['netIncome']) / 1e9:.2f} B"
                    })

                    # Analysis Report
                    st.markdown("## 🤖 AI Analysis Report")
                    st.markdown(data["analysis_report"], unsafe_allow_html=True)

                else:
                    st.error(f"❌ Error {response.status_code}: {response.json().get('detail')}")

            except requests.exceptions.Timeout:
                st.error("❌ Request timed out. The backend may still be starting. Please try again.")
            except Exception as e:
                st.error(f"❌ An error occurred: {str(e)}")


template_end()
st.sidebar.markdown('---')
social_media(justify="space-evenly")