import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';

const TestApp = () => {
  return (
    <div style={{ padding: "2rem", fontSize: "1.5rem", textAlign: "center" }}>
      Ziggy is alive! 🧠💬
    </div>
  );
};

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <TestApp />
  </React.StrictMode>
);