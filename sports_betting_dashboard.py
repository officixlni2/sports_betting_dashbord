
import streamlit as st
import pandas as pd
import numpy as np

# Title
st.title("Sports Betting Predictive Dashboard")

# Sidebar for user inputs
st.sidebar.header("Input Game Details")
game_type = st.sidebar.selectbox("Select Sport", ["Soccer", "Basketball", "Tennis"])
home_team = st.sidebar.text_input("Home Team")
away_team = st.sidebar.text_input("Away Team")
home_odds = st.sidebar.number_input("Home Odds", value=1.8)
away_odds = st.sidebar.number_input("Away Odds", value=2.5)

# Simulating outcomes
def simulate_game(home_odds, away_odds, simulations=10000):
    home_prob = 1 / home_odds
    away_prob = 1 / away_odds
    home_wins = np.random.binomial(simulations, home_prob / (home_prob + away_prob))
    away_wins = simulations - home_wins
    return home_wins / simulations, away_wins / simulations

if home_team and away_team:
    home_win_prob, away_win_prob = simulate_game(home_odds, away_odds)
    
    # Display Results
    st.write(f"### Matchup: {home_team} vs {away_team}")
    st.write(f"**Home Team Win Probability**: {home_win_prob * 100:.2f}%")
    st.write(f"**Away Team Win Probability**: {away_win_prob * 100:.2f}%")
    
    # Chart for probabilities
    st.bar_chart(pd.DataFrame({
        "Teams": [home_team, away_team],
        "Win Probability": [home_win_prob, away_win_prob]
    }))

# Footer
st.write("### Use this dashboard for informational purposes only. Always bet responsibly.")
