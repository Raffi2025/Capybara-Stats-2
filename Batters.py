import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from MainApp import batterList


#Full table
data = pd.read_csv("batters.csv")
st.subheader(f"Batters")
st.write(data)

#Percentile Graph
st.subheader("wOBA Percentile Graph")

#Generate the percentile graph for wOBA
def generate_woba_percentile_graph(batterList):
    # Filter valid players
    valid_players = [
        player for player in batterList
        if player["wOBA"] != "N/A" and player["PA"] >= 5
    ]

    if not valid_players:
        return None  # No valid players

    # Sort by wOBA
    valid_players.sort(key=lambda x: x["wOBA"])

    # Extract data
    woba_values = [player["wOBA"] for player in valid_players]
    percentiles = np.linspace(0, 100, len(woba_values))

 # Create plot
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=percentiles,
        y=woba_values,
        mode='lines+markers',
        name='wOBA',
        line=dict(color='royalblue')
    ))
    fig.update_layout(
        title="wOBA Percentile Graph (PA ≥ 5)",
        xaxis_title="Percentile",
        yaxis_title="wOBA",
        template="plotly_dark"
    )

    return fig

#Display the percentile graph
fig = generate_woba_percentile_graph(batterList)
if fig:
  st.plotly_chart(fig, use_container_width=True)
else:
  st.warning("No valid wOBA data available")
