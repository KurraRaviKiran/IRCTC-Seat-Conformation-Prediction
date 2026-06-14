import streamlit as st
import pandas as pd
import pickle
import plotly.express as px

df = pd.read_csv("Railway Ticket Confirmation.csv")

with open("railway_model.pkl", "rb") as f:
    model = pickle.load(f)


st.title("Railway Ticket Confirmation System")

page = st.sidebar.selectbox(
    "Select Page",
    ["Dashboard", "Prediction"]
)

if page == "Dashboard":

    st.header("Railway Ticket Confirmation Dashboard")

    # Metrics
    total = len(df)
    confirmed = (df["Confirmation Status"] == "Confirmed").sum()
    not_confirmed = (df["Confirmation Status"] == "Not Confirmed").sum()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Bookings", total)

    with col2:
        st.metric("Confirmed Tickets", confirmed)

    with col3:
        st.metric("Not Confirmed Tickets", not_confirmed)

    st.markdown("---")

    # ==========================
    # Pie Chart
    # ==========================
    status_counts = df["Confirmation Status"].value_counts()

    fig1 = px.pie(
        values=status_counts.values,
        names=status_counts.index,
        title="Ticket Confirmation Distribution"
    )

    st.plotly_chart(fig1, use_container_width=True)

    # ==========================
    # Donut Chart
    # ==========================
    quota_counts = df["Quota"].value_counts()

    fig2 = px.pie(
        values=quota_counts.values,
        names=quota_counts.index,
        hole=0.5,
        title="Quota Distribution"
    )

    st.plotly_chart(fig2, use_container_width=True)

    # ==========================
    # Treemap
    # ==========================
    train_counts = df["Train Type"].value_counts().reset_index()
    train_counts.columns = ["Train Type", "Count"]

    fig3 = px.treemap(
        train_counts,
        path=["Train Type"],
        values="Count",
        title="Train Type Distribution"
    )

    st.plotly_chart(fig3, use_container_width=True)

    # ==========================
    # Age Histogram
    # ==========================
    age_df = df.copy()

    age_df["Age of Passengers"] = pd.to_numeric(
        age_df["Age of Passengers"],
        errors="coerce"
    )

    fig4 = px.histogram(
        age_df,
        x="Age of Passengers",
        nbins=20,
        title="Passenger Age Distribution"
    )

    st.plotly_chart(fig4, use_container_width=True)

    # ==========================
    # Travel Distance Box Plot
    # ==========================
    fig5 = px.box(
        df,
        y="Travel Distance",
        title="Travel Distance Spread"
    )

    st.plotly_chart(fig5, use_container_width=True)

    # ==========================
    # Scatter Plot
    # ==========================
    fig6 = px.scatter(
        df,
        x="Travel Distance",
        y="Travel Time",
        color="Confirmation Status",
        title="Distance vs Travel Time"
    )

    st.plotly_chart(fig6, use_container_width=True)