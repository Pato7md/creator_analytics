import React, { useEffect, useState } from "react";
import Plot from "react-plotly.js";
import { getFollowerHistory, getForecast } from "../api/apiClient";

const ChartFollower = () => {
  const [historyData, setHistory] = useState([]);
  const [forecastData, setForecast] = useState([]);

  useEffect(() => {
    async function fetchData() {
      const history = await getFollowerHistory();
      const forecast = await getForecast();
      setHistory(history);
      setForecast(forecast);
    }
    fetchData();
  }, []);

  return (
    <Plot
      data={[
        {
          x: historyData.map(d => d.fetched_at),
          y: historyData.map(d => d.follower_count),
          type: "scatter",
          mode: "lines+markers",
          name: "Followers"
        },
        {
          x: forecastData.map(d => d.ds),
          y: forecastData.map(d => d.yhat),
          type: "scatter",
          mode: "lines",
          name: "Forecast"
        }
      ]}
      layout={{ title: "Twitch Followers & Forecast" }}
    />
  );
};

export default ChartFollower;
