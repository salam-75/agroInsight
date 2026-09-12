import React, { useState } from "react";
import { createRoot } from "react-dom/client";
import { createPrediction } from "./api";
import "./styles.css";

function App() {
  const [language, setLanguage] = useState("বাংলা");
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  async function diagnose(event) {
    event.preventDefault();
    if (!file) return setError("Choose a leaf image first.");
    setLoading(true);
    setError("");
    try { setResult(await createPrediction(file)); } catch (err) { setError(err.message); }
    finally { setLoading(false); }
  }

  return (
    <main className="shell">
      <header className="topbar">
        <div><span className="eyebrow">AGROINSIGHT</span><h1>Healthier crops, clearer decisions.</h1></div>
        <button className="language" onClick={() => setLanguage(language === "বাংলা" ? "English" : "বাংলা")}>{language}</button>
      </header>
      <section className="hero">
        <p className="eyebrow">LEAF DIAGNOSIS</p>
        <h2>Spot a problem before it spreads.</h2>
        <p className="muted">Upload a clear leaf photo. A trained model will return a possible condition and confidence score.</p>
        <form onSubmit={diagnose}>
          <label className="upload">
            <input type="file" accept="image/*" capture="environment" onChange={(event) => { setFile(event.target.files?.[0] || null); setResult(null); }} />
            <span className="upload-icon">＋</span>
            <strong>{file ? file.name : "Add a leaf photo"}</strong>
            <small>Camera-ready · JPG, PNG or WebP</small>
          </label>
          <button className="primary" disabled={loading}>{loading ? "Checking…" : "Check leaf"}</button>
        </form>
        {error && <p className="error">{error}</p>}
      </section>
      {result && <section className="result card"><div><span className="eyebrow">RESULT</span><h3>{result.disease || "Model not available"}</h3><p>{result.message}</p></div><div className="confidence"><b>{result.confidence ? `${Math.round(result.confidence * 100)}%` : "—"}</b><span>confidence</span></div></section>}
      <section className="grid">
        <article className="card"><span className="tile-icon">✦</span><h3>Advisory</h3><p className="muted">Practical crop-care guidance, coming next.</p><span className="tag">SOON</span></article>
        <article className="card"><span className="tile-icon">◷</span><h3>History</h3><p className="muted">Your saved checks will appear here.</p><span className="tag">SOON</span></article>
        <article className="card"><span className="tile-icon">⌖</span><h3>Find a shop</h3><p className="muted">Locate trusted agricultural suppliers.</p><span className="tag">SOON</span></article>
      </section>
      <footer>Always verify a diagnosis locally before applying any treatment.</footer>
    </main>
  );
}

createRoot(document.getElementById("root")).render(<App />);
