


# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import plotly.graph_objects as go
# from sklearn.linear_model import LinearRegression
# import numpy as np

# st.set_page_config(page_title="Cryptocurrency Analysis", layout="wide")

# st.sidebar.title("Cryptocurrency Dashboard")
# page = st.sidebar.radio(
#     "Navigation", ["Overview", "Price Analysis", "Candlestick Chart", "Portfolio Tracker", "Price Prediction"]
# )

# st.sidebar.subheader("Upload Cryptocurrency Data")
# btc_file = st.sidebar.file_uploader("BTC-USD.csv", type=["csv"])
# eth_file = st.sidebar.file_uploader("ETH_1H.csv", type=["csv"])
# currencies = st.sidebar.multiselect("Select Currencies for Analysis", ["Bitcoin", "Ethereum"])

# def load_dataset(file):
#     try:
#         df = pd.read_csv(file)
#         df["Date"] = pd.to_datetime(df["Date"])
#         return df
#     except Exception as e:
#         st.error(f"Error loading file: {e}")
#         return None

# btc_data = load_dataset(btc_file) if btc_file else None
# eth_data = load_dataset(eth_file) if eth_file else None

# def filter_by_date(df, start, end):
#     start = pd.to_datetime(start)
#     end = pd.to_datetime(end)
#     return df[(df["Date"] >= start) & (df["Date"] <= end)]

# def train_linear_regression_model(df, target_date):
#     df = df.sort_values(by="Date")
#     df["Days"] = (df["Date"] - df["Date"].min()).dt.days
#     X = df[["Days"]]
#     y = df["Close"]
#     model = LinearRegression()
#     model.fit(X, y)
    
#     last_date = df["Date"].max()
#     target_date_dt = pd.to_datetime(target_date)
#     forecast_period = (target_date_dt - last_date).days
#     if forecast_period <= 0:
#         st.warning("Target date must be after the last date in the dataset.")
#         return None

#     future_days = np.array([df["Days"].max() + i for i in range(1, forecast_period + 1)]).reshape(-1, 1)
#     predictions = model.predict(future_days)
#     future_dates = pd.date_range(start=last_date + pd.Timedelta(days=1), periods=forecast_period, freq='D')
#     forecast = pd.DataFrame({"ds": future_dates, "yhat": predictions})
#     return forecast

# btc_min_date, btc_max_date = (None, None)
# eth_min_date, eth_max_date = (None, None)

# if btc_data is not None:
#     btc_min_date = btc_data["Date"].min()
#     btc_max_date = btc_data["Date"].max()

# if eth_data is not None:
#     eth_min_date = eth_data["Date"].min()
#     eth_max_date = eth_data["Date"].max()

# overall_min_date = min(filter(None, [btc_min_date, eth_min_date]))
# overall_max_date = max(filter(None, [btc_max_date, eth_max_date]))

# st.sidebar.subheader("Filter by Date Range")
# start_date = st.sidebar.date_input(
#     "Start Date",
#     value=overall_min_date if overall_min_date else pd.to_datetime("2020-01-01"),
#     min_value=overall_min_date,
#     max_value=overall_max_date
# )
# end_date = st.sidebar.date_input(
#     "End Date",
#     value=overall_max_date if overall_max_date else pd.to_datetime("2023-01-01"),
#     min_value=overall_min_date,
#     max_value=overall_max_date
# )

# # Overview Page
# if page == "Overview":
#     st.title("Cryptocurrency Dashboard - Overview")
#     st.markdown("""
#         Analyze Bitcoin and Ethereum prices, trading volume, and trends interactively.
#         Features include:
#         - Price trends visualization
#         - Candlestick charts
#         - Portfolio tracker
#         """)
#     if btc_data is not None:
#         st.subheader("Bitcoin Dataset Preview")
#         st.dataframe(btc_data.head())
#     if eth_data is not None:
#         st.subheader("Ethereum Dataset Preview")
#         st.dataframe(eth_data.head())

# # Price Analysis Page
# if page == "Price Analysis":
#     st.title("Cryptocurrency Price Analysis")
#     if currencies:
#         for currency in currencies:
#             if currency == "Bitcoin" and btc_data is not None:
#                 btc_filtered = filter_by_date(btc_data, start_date, end_date)
#                 st.subheader(f"{currency} Price Trends")
#                 fig = px.line(
#                     btc_filtered,
#                     x="Date",
#                     y=["Open", "Close", "High", "Low"],
#                     title="Bitcoin Price Trends",
#                     labels={"value": "Price (USD)", "variable": "Price Type"},
#                 )
#                 st.plotly_chart(fig, use_container_width=True)
#             elif currency == "Ethereum" and eth_data is not None:
#                 eth_filtered = filter_by_date(eth_data, start_date, end_date)
#                 st.subheader(f"{currency} Price Trends")
#                 fig = px.line(
#                     eth_filtered,
#                     x="Date",
#                     y=["Open", "Close", "High", "Low"],
#                     title="Ethereum Price Trends",
#                     labels={"value": "Price (USD)", "variable": "Price Type"},
#                 )
#                 st.plotly_chart(fig, use_container_width=True)

# # Candlestick Chart Page
# if page == "Candlestick Chart":
#     st.title("Cryptocurrency Candlestick Charts")
#     if currencies:
#         for currency in currencies:
#             if currency == "Bitcoin" and btc_data is not None:
#                 btc_filtered = filter_by_date(btc_data, start_date, end_date)
#                 st.subheader(f"{currency} Candlestick Chart")
#                 fig = go.Figure(
#                     data=[
#                         go.Candlestick(
#                             x=btc_filtered["Date"],
#                             open=btc_filtered["Open"],
#                             high=btc_filtered["High"],
#                             low=btc_filtered["Low"],
#                             close=btc_filtered["Close"],
#                         )
#                     ]
#                 )
#                 fig.update_layout(title="Bitcoin Candlestick Chart", xaxis_title="Date", yaxis_title="Price (USD)")
#                 st.plotly_chart(fig, use_container_width=True)
#             elif currency == "Ethereum" and eth_data is not None:
#                 eth_filtered = filter_by_date(eth_data, start_date, end_date)
#                 st.subheader(f"{currency} Candlestick Chart")
#                 fig = go.Figure(
#                     data=[
#                         go.Candlestick(
#                             x=eth_filtered["Date"],
#                             open=eth_filtered["Open"],
#                             high=eth_filtered["High"],
#                             low=eth_filtered["Low"],
#                             close=eth_filtered["Close"],
#                         )
#                     ]
#                 )
#                 fig.update_layout(title="Ethereum Candlestick Chart", xaxis_title="Date", yaxis_title="Price (USD)")
#                 st.plotly_chart(fig, use_container_width=True)

# # Portfolio Tracker Page
# if page == "Portfolio Tracker":
#     st.title("Cryptocurrency Portfolio Tracker")
#     btc_holdings = st.number_input("Enter your Bitcoin holdings:", min_value=0.0, value=0.0, step=0.01)
#     eth_holdings = st.number_input("Enter your Ethereum holdings:", min_value=0.0, value=0.0, step=0.01)
#     if btc_data is not None and eth_data is not None:
#         btc_filtered = filter_by_date(btc_data, start_date, end_date)
#         eth_filtered = filter_by_date(eth_data, start_date, end_date)
#         merged_data = pd.merge(
#             btc_filtered[["Date", "Close"]].rename(columns={"Close": "BTC_Close"}),
#             eth_filtered[["Date", "Close"]].rename(columns={"Close": "ETH_Close"}),
#             on="Date",
#             how="inner"
#         )
#         merged_data["Portfolio Value (USD)"] = (
#             btc_holdings * merged_data["BTC_Close"] + eth_holdings * merged_data["ETH_Close"]
#         )
#         st.subheader("Portfolio Value Over Time")
#         fig = px.line(
#             merged_data,
#             x="Date",
#             y="Portfolio Value (USD)",
#             title="Portfolio Value Over Time",
#             labels={"Date": "Date", "Portfolio Value (USD)": "Value (USD)"}
#         )
#         st.plotly_chart(fig, use_container_width=True)
#         st.subheader("Portfolio Data Preview")
#         st.dataframe(merged_data)
#     else:
#         st.warning("Please upload both Bitcoin and Ethereum datasets to track your portfolio.")

# # Price Prediction Page
# if page == "Price Prediction":
#     st.title("Cryptocurrency Price Prediction")
#     target_date = "2026-01-01"
#     if btc_data is not None:
#         st.subheader("Bitcoin Price Prediction")
#         btc_forecast = train_linear_regression_model(btc_data, target_date)
#         if btc_forecast is not None:
#             fig = px.line(btc_forecast, x="ds", y="yhat", title="Bitcoin Price Forecast")
#             st.plotly_chart(fig, use_container_width=True)
#             predicted_btc = btc_forecast[btc_forecast["ds"] == target_date]["yhat"].values
#             if len(predicted_btc) > 0:
#                 st.write(f"Predicted Bitcoin Price on {target_date}: ${predicted_btc[0]:,.2f}")
#     if eth_data is not None:
#         st.subheader("Ethereum Price Prediction")
#         eth_forecast = train_linear_regression_model(eth_data, target_date)
#         if eth_forecast is not None:
#             fig = px.line(eth_forecast, x="ds", y="yhat", title="Ethereum Price Forecast")
#             st.plotly_chart(fig, use_container_width=True)
#             predicted_eth = eth_forecast[eth_forecast["ds"] == target_date]["yhat"].values
#             if len(predicted_eth) > 0:
#                 st.write(f"Predicted Ethereum Price on {target_date}: ${predicted_eth[0]:,.2f}")












import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
import numpy as np

st.set_page_config(page_title="Cryptocurrency Analysis", layout="wide")

st.sidebar.title("Cryptocurrency Dashboard")
page = st.sidebar.radio(
    "Navigation", ["Overview", "Price Analysis", "Candlestick Chart", "Portfolio Tracker", "Price Prediction"]
)

st.sidebar.subheader("Upload Cryptocurrency Data")
btc_file = st.sidebar.file_uploader("BTC-USD.csv", type=["csv"])
eth_file = st.sidebar.file_uploader("ETH_1H.csv", type=["csv"])
currencies = st.sidebar.multiselect("Select Currencies for Analysis", ["Bitcoin", "Ethereum"])

def load_dataset(file):
    try:
        df = pd.read_csv(file)
        df["Date"] = pd.to_datetime(df["Date"])
        return df
    except Exception as e:
        st.error(f"Error loading file: {e}")
        return None

btc_data = load_dataset(btc_file) if btc_file else None
eth_data = load_dataset(eth_file) if eth_file else None

def filter_by_date(df, start, end):
    start = pd.to_datetime(start)
    end = pd.to_datetime(end)
    return df[(df["Date"] >= start) & (df["Date"] <= end)]

def train_linear_regression_model(df, target_date):
    df = df.sort_values(by="Date")
    df["Days"] = (df["Date"] - df["Date"].min()).dt.days
    X = df[["Days"]]
    y = df["Close"]
    model = LinearRegression()
    model.fit(X, y)
    
    last_date = df["Date"].max()
    target_date_dt = pd.to_datetime(target_date)
    forecast_period = (target_date_dt - last_date).days
    if forecast_period <= 0:
        st.warning("Target date must be after the last date in the dataset.")
        return None

    future_days = np.array([df["Days"].max() + i for i in range(1, forecast_period + 1)]).reshape(-1, 1)
    predictions = model.predict(future_days)
    future_dates = pd.date_range(start=last_date + pd.Timedelta(days=1), periods=forecast_period, freq='D')
    forecast = pd.DataFrame({"ds": future_dates, "yhat": predictions})
    return forecast

btc_min_date, btc_max_date = (None, None)
eth_min_date, eth_max_date = (None, None)

if btc_data is not None:
    btc_min_date = btc_data["Date"].min()
    btc_max_date = btc_data["Date"].max()

if eth_data is not None:
    eth_min_date = eth_data["Date"].min()
    eth_max_date = eth_data["Date"].max()

overall_min_date = min(filter(None, [btc_min_date, eth_min_date]))
overall_max_date = max(filter(None, [btc_max_date, eth_max_date]))

st.sidebar.subheader("Filter by Date Range")
start_date = st.sidebar.date_input(
    "Start Date",
    value=overall_min_date if overall_min_date else pd.to_datetime("2020-01-01"),
    min_value=overall_min_date,
    max_value=overall_max_date
)
end_date = st.sidebar.date_input(
    "End Date",
    value=overall_max_date if overall_max_date else pd.to_datetime("2023-01-01"),
    min_value=overall_min_date,
    max_value=overall_max_date
)

# Overview Page
if page == "Overview":
    st.title("Cryptocurrency Dashboard - Overview")
    st.markdown("""
        Analyze Bitcoin and Ethereum prices, trading volume, and trends interactively.
        Features include:
        - Price trends visualization
        - Candlestick charts
        - Portfolio tracker
        """)
    if btc_data is not None:
        st.subheader("Bitcoin Dataset Preview")
        st.dataframe(btc_data.head())
    if eth_data is not None:
        st.subheader("Ethereum Dataset Preview")
        st.dataframe(eth_data.head())

# Price Analysis Page
if page == "Price Analysis":
    st.title("Cryptocurrency Price Analysis")
    if currencies:
        for currency in currencies:
            if currency == "Bitcoin" and btc_data is not None:
                btc_filtered = filter_by_date(btc_data, start_date, end_date)
                st.subheader(f"{currency} Price Trends")
                fig = px.line(
                    btc_filtered,
                    x="Date",
                    y=["Open", "Close", "High", "Low"],
                    title="Bitcoin Price Trends",
                    labels={"value": "Price (USD)", "variable": "Price Type"},
                )
                st.plotly_chart(fig, use_container_width=True)
            elif currency == "Ethereum" and eth_data is not None:
                eth_filtered = filter_by_date(eth_data, start_date, end_date)
                st.subheader(f"{currency} Price Trends")
                fig = px.line(
                    eth_filtered,
                    x="Date",
                    y=["Open", "Close", "High", "Low"],
                    title="Ethereum Price Trends",
                    labels={"value": "Price (USD)", "variable": "Price Type"},
                )
                st.plotly_chart(fig, use_container_width=True)

# Candlestick Chart Page
if page == "Candlestick Chart":
    st.title("Cryptocurrency Candlestick Charts")
    if currencies:
        for currency in currencies:
            if currency == "Bitcoin" and btc_data is not None:
                btc_filtered = filter_by_date(btc_data, start_date, end_date)
                st.subheader(f"{currency} Candlestick Chart")
                fig = go.Figure(
                    data=[
                        go.Candlestick(
                            x=btc_filtered["Date"],
                            open=btc_filtered["Open"],
                            high=btc_filtered["High"],
                            low=btc_filtered["Low"],
                            close=btc_filtered["Close"],
                        )
                    ]
                )
                fig.update_layout(title="Bitcoin Candlestick Chart", xaxis_title="Date", yaxis_title="Price (USD)")
                st.plotly_chart(fig, use_container_width=True)
            elif currency == "Ethereum" and eth_data is not None:
                eth_filtered = filter_by_date(eth_data, start_date, end_date)
                st.subheader(f"{currency} Candlestick Chart")
                fig = go.Figure(
                    data=[
                        go.Candlestick(
                            x=eth_filtered["Date"],
                            open=eth_filtered["Open"],
                            high=eth_filtered["High"],
                            low=eth_filtered["Low"],
                            close=eth_filtered["Close"],
                        )
                    ]
                )
                fig.update_layout(title="Ethereum Candlestick Chart", xaxis_title="Date", yaxis_title="Price (USD)")
                st.plotly_chart(fig, use_container_width=True)

# Portfolio Tracker Page
if page == "Portfolio Tracker":
    st.title("Cryptocurrency Portfolio Tracker")
    btc_holdings = st.number_input("Enter your Bitcoin holdings:", min_value=0.0, value=0.0, step=0.01)
    eth_holdings = st.number_input("Enter your Ethereum holdings:", min_value=0.0, value=0.0, step=0.01)
    if btc_data is not None and eth_data is not None:
        btc_filtered = filter_by_date(btc_data, start_date, end_date)
        eth_filtered = filter_by_date(eth_data, start_date, end_date)
        merged_data = pd.merge(
            btc_filtered[["Date", "Close"]].rename(columns={"Close": "BTC_Close"}),
            eth_filtered[["Date", "Close"]].rename(columns={"Close": "ETH_Close"}),
            on="Date",
            how="inner"
        )
        merged_data["Portfolio Value (USD)"] = (
            btc_holdings * merged_data["BTC_Close"] + eth_holdings * merged_data["ETH_Close"]
        )
        st.subheader("Portfolio Value Over Time")
        fig = px.line(
            merged_data,
            x="Date",
            y="Portfolio Value (USD)",
            title="Portfolio Value Over Time",
            labels={"Date": "Date", "Portfolio Value (USD)": "Value (USD)"}
        )
        st.plotly_chart(fig, use_container_width=True)
        st.subheader("Portfolio Data Preview")
        st.dataframe(merged_data)
    else:
        st.warning("Please upload both Bitcoin and Ethereum datasets to track your portfolio.")

# Price Prediction Page with Currency Dropdown
if page == "Price Prediction":
    st.title("Cryptocurrency Price Prediction")
    target_date = "2026-01-01"
    prediction_currency = st.selectbox("Select Currency for Prediction", ["Bitcoin", "Ethereum", "Both"])
    
    if prediction_currency in ["Bitcoin", "Both"] and btc_data is not None:
        st.subheader("Bitcoin Price Prediction")
        btc_forecast = train_linear_regression_model(btc_data, target_date)
        if btc_forecast is not None:
            fig = px.line(btc_forecast, x="ds", y="yhat", title="Bitcoin Price Forecast")
            st.plotly_chart(fig, use_container_width=True)
            predicted_btc = btc_forecast[btc_forecast["ds"] == target_date]["yhat"].values
            if len(predicted_btc) > 0:
                st.write(f"Predicted Bitcoin Price on {target_date}: ${predicted_btc[0]:,.2f}")
                
    if prediction_currency in ["Ethereum", "Both"] and eth_data is not None:
        st.subheader("Ethereum Price Prediction")
        eth_forecast = train_linear_regression_model(eth_data, target_date)
        if eth_forecast is not None:
            fig = px.line(eth_forecast, x="ds", y="yhat", title="Ethereum Price Forecast")
            st.plotly_chart(fig, use_container_width=True)
            predicted_eth = eth_forecast[eth_forecast["ds"] == target_date]["yhat"].values
            if len(predicted_eth) > 0:
                st.write(f"Predicted Ethereum Price on {target_date}: ${predicted_eth[0]:,.2f}")


