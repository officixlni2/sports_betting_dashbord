
import streamlit as st
import requests
import pandas as pd
import numpy as np

# Title
st.title("Sports Betting Dashboard with Live Data")

# Sidebar for user inputs
st.sidebar.header("Select Sport and League")
sport = st.sidebar.selectbox("Sport", ["Soccer", "Basketball", "Tennis"])
league = st.sidebar.text_input("League (e.g., EPL, NBA)")

# Function to fetch data from OddsAPI (replace with your API key)
def fetch_live_data(sport, league, api_key="8c0a8a88ea324424de4fa9f606f633a1"):
    url = f"https://api.the-odds-api.com/v4/sports/{sport}/odds/"
    params = {"apiKey": api_key, "regions": "us", "markets": "h2h,spreads", "league": league}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Failed to fetch data: {response.status_code}")
        return None

# Fetch and display live data
if sport and league:
    st.write(f"### Fetching Live Odds for {sport} ({league})...")
    data = fetch_live_data(sport, league)
    if data:
        odds_data = []
        for game in data:
            match = game["home_team"] + " vs " + game["away_team"]
            home_odds = game["bookmakers"][0]["markets"][0]["outcomes"][0]["price"]
            away_odds = game["bookmakers"][0]["markets"][0]["outcomes"][1]["price"]
            odds_data.append({"Match": match, "Home Odds": home_odds, "Away Odds": away_odds})
        
        # Display the odds in a table
        st.write("### Live Odds")
        odds_df = pd.DataFrame(odds_data)
        st.table(odds_df)

# Footer
st.write("### Use this dashboard for informational purposes only. Always bet responsibly.")
