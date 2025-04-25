import React, { useState, useEffect } from 'react';

function App() {
  const [question, setQuestion] = useState('');
  const [response, setResponse] = useState('');

  useEffect(() => {
    try {
      localStorage.setItem("__ziggy_test__", "true");
      localStorage.removeItem("__ziggy_test__");
    } catch (err) {
      console.warn("Ziggy can’t access localStorage in this environment. All good though!");
    }
  }, []);

  const askZiggy = async () => {
    const res = await fetch('http://localhost:5000/ask', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ question }),
    });

    const data = await res.json();
    setResponse(data.answer);
  };

  return (
    <div className="min-h-screen bg-indigo-50 flex items-center justify-center p-6">
      <div className="bg-white rounded-xl shadow-md p-6 w-full max-w-xl">
        <h1 className="text-2xl font-bold mb-4">Ziggy 🤖 – Your Indigo Chatbot</h1>
        <input
          type="text"
          className="w-full border border-gray-300 p-2 rounded mb-4"
          placeholder="Ask Ziggy something..."
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
        />
        <button
          onClick={askZiggy}
          className="bg-indigo-600 text-white px-4 py-2 rounded hover:bg-indigo-700"
        >
          Ask
        </button>
        {response && (
          <div className="mt-4 p-4 bg-gray-100 rounded">
            <strong>Ziggy says:</strong> {response}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
