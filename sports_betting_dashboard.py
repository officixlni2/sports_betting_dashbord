
import streamlit as st
import requests
import pandas as pd

# API Key
API_KEY = "549902"

# Function to fetch data from The Sports DB API
def fetch_data(endpoint, params=None):
    url = f"https://www.thesportsdb.com/api/v1/json/{API_KEY}/{endpoint}"
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Failed to fetch data from The Sports DB: {response.status_code}")
        return None

# Function to display data in a table format
def display_table(data, title):
    if data is not None and len(data) > 0:
        st.write(f"### {title}")
        st.dataframe(pd.DataFrame(data))
    else:
        st.warning(f"No data available for {title}.")

# Sidebar for user inputs
st.sidebar.header("Select Sport and Data Type")
sport = st.sidebar.selectbox("Sport", ["NBA", "NFL", "NHL", "Soccer", "Tennis"])
data_type = st.sidebar.radio("Data Type", ["Upcoming Games", "Previous Games", "Standings", "Injuries"])

# Map sport to league IDs (replace with actual IDs from The Sports DB)
SPORTS_IDS = {
    "NBA": "4387",
    "NFL": "4391",
    "NHL": "4380",
    "Soccer": "4328",  # Example for English Premier League
    "Tennis": "4396"  # Example Tennis ID
}

# Fetch and display data based on user selection
if sport and data_type:
    league_id = SPORTS_IDS.get(sport)
    if data_type == "Upcoming Games":
        endpoint = f"eventsnextleague.php"
        data = fetch_data(endpoint, {"id": league_id})
        if data:
            display_table(data.get("events", []), f"Upcoming {sport} Games")
    elif data_type == "Previous Games":
        endpoint = f"eventspastleague.php"
        data = fetch_data(endpoint, {"id": league_id})
        if data:
            display_table(data.get("events", []), f"Previous {sport} Games")
    elif data_type == "Standings":
        endpoint = f"lookuptable.php"
        data = fetch_data(endpoint, {"l": league_id})
        if data:
            display_table(data.get("table", []), f"{sport} Standings")
    elif data_type == "Injuries":
        # No direct injuries endpoint, replace with placeholder or relevant lookup if available
        st.warning("Injuries data not supported for this sport in The Sports DB.")

# Insights Section
st.header("Insights and Analysis")
user_query = st.text_input("Ask a question about the selected sport or matchup (e.g., 'Who is likely to win Lakers vs Heat?')")
if user_query:
    st.write(f"### Your Question: {user_query}")
    # Placeholder response for now
    st.write("Analyzing the matchup...")
    st.write("Based on recent trends and stats, here are the key insights:")
    st.write("- Example insight: The Lakers have won 4 of their last 5 games.")
    st.write("- Example insight: Heat's top scorer is injured for this matchup.")

# Footer
st.write("### Use this dashboard for informational purposes only. Always bet responsibly.")
