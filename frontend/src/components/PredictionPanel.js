import React, { useEffect, useState } from "react";
import { getForecast } from "../api/apiClient";

const PredictionPanel = () => {
  const [forecast, setForecast] = useState([]);

  useEffect(() => {
    async function fetchData() {
      const data = await getForecast();
      setForecast(data);
    }
    fetchData();
  }, []);

  return (
    <div className="prediction-panel">
      <h2>Follower Forecast</h2>
      <ul>
        {forecast.map((f, index) => (
          <li key={index}>{f.ds}: {Math.round(f.yhat)}</li>
        ))}
      </ul>
    </div>
  );
};

export default PredictionPanel;
