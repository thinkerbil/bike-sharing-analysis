import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Konfigurasi gaya seaborn
sns.set(style='dark')

# Helper function untuk menyiapkan data
def create_daily_rent_df(df):
    daily_rent_df = df.resample(rule='D', on='dteday').agg({
        "cnt": "sum"
    }).reset_index()
    return daily_rent_df

def create_by_season_df(df):
    return df.groupby("season").cnt.mean().reset_index()

def create_hourly_pattern_df(df):
    return df.groupby(["hr", "workingday"]).cnt.mean().reset_index()

def create_weather_impact_df(df):
    return df.groupby("weathersit").cnt.mean().reset_index()

# Load data
main_df = pd.read_csv("dashboard/main_data.csv")
main_df["dteday"] = pd.to_datetime(main_df["dteday"])

# --- SIDEBAR (FILTER INTERAKTIF) ---
with st.sidebar:
    st.title("Bike Sharing Filter 🚲")
    st.sidebar.image("https://raw.githubusercontent.com/thinkerbil/submission-bike-sharing/main/logo.png", use_container_width=True)
    
    # Mengambil rentang waktu dari data
    min_date = main_df["dteday"].min()
    max_date = main_df["dteday"].max()
    
    start_date, end_date = st.date_input(
        label='Pilih Rentang Waktu',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

# Menghubungkan Filter ke Dataframe Utama
main_df = main_df[(main_df["dteday"] >= str(start_date)) & 
                (main_df["dteday"] <= str(end_date))]

# Menyiapkan DataFrame yang sudah terfilter
daily_rent_df = create_daily_rent_df(main_df)
by_season_df = create_by_season_df(main_df)
hourly_pattern_df = create_hourly_pattern_df(main_df)
weather_impact_df = create_weather_impact_df(main_df)

# --- DASHBOARD MAIN PAGE ---
st.header('Bike Sharing Interactive Dashboard')

# 1. Metrik Utama (KPIs)
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Rentals", value=f"{main_df.cnt.sum():,}")
with col2:
    st.metric("Registered Users", value=f"{main_df.registered.sum():,}")
with col3:
    st.metric("Casual Users", value=f"{main_df.casual.sum():,}")

# 2. Tren Harian
st.subheader('Daily Rentals Trend')
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(daily_rent_df["dteday"], daily_rent_df["cnt"], marker='o', linewidth=2, color="#3498db")
st.pyplot(fig)

# 3. Musim & Cuaca
st.subheader("Impact of Season and Weather")
col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.barplot(x="season", y="cnt", data=by_season_df, palette="viridis", ax=ax)
    ax.set_title("Average Rentals by Season")
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.barplot(x="weathersit", y="cnt", data=weather_impact_df, palette="magma", ax=ax)
    ax.set_title("Average Rentals by Weather")
    st.pyplot(fig)

# 4. Pola Jam
st.subheader("Hourly Patterns: Working Day vs Weekend")
fig, ax = plt.subplots(figsize=(16, 8))
sns.pointplot(data=hourly_pattern_df, x='hr', y='cnt', hue='workingday', ax=ax)
ax.set_xlabel("Hour (0-23)")
ax.set_ylabel("Average Rentals")
st.pyplot(fig)

st.caption('Copyright (c) Nabila Najwa Husna 2026')
