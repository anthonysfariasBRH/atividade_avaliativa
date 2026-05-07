import { useState } from 'react';

const API_URL = 'http://localhost:8000';

function App() {
  const [price, setPrice] = useState('');
  const [discount, setDiscount] = useState('');
  const [result, setResult] = useState(null);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const formatBRL = (value) =>
    new Intl.NumberFormat('pt-BR', {
      style: 'currency',
      currency: 'BRL',
    }).format(value);

  const handleSubmit = async (event) => {
    event.preventDefault();
    setError('');
    setResult(null);

    const parsedPrice = Number(price);
    const parsedDiscount = Number(discount);

    if (Number.isNaN(parsedPrice) || Number.isNaN(parsedDiscount)) {
      setError('Preencha preço e desconto com valores numéricos válidos.');
      return;
    }

    setLoading(true);
    try {
      const response = await fetch(`${API_URL}/discount`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ price: parsedPrice, discount: parsedDiscount }),
      });

      const data = await response.json();

      if (!response.ok) {
        setError(data.detail || 'Erro ao calcular o desconto.');
        return;
      }

      setResult(data.final_price);
    } catch (err) {
      setError('Não foi possível contactar o backend. Ele está rodando?');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <header>
        <h1>Calculadora de Desconto</h1>
        <p className="subtitle">
          Informe o preço original e a porcentagem de desconto para calcular o
          preço final.
        </p>
      </header>

      <form onSubmit={handleSubmit} className="card">
        <label>
          Preço original (R$)
          <input
            type="number"
            step="0.01"
            min="0"
            placeholder="100.00"
            value={price}
            onChange={(event) => setPrice(event.target.value)}
            required
          />
        </label>

        <label>
          Desconto (%)
          <input
            type="number"
            step="0.01"
            min="0"
            max="100"
            placeholder="10"
            value={discount}
            onChange={(event) => setDiscount(event.target.value)}
            required
          />
        </label>

        <button type="submit" disabled={loading}>
          {loading ? 'Calculando...' : 'Calcular'}
        </button>
      </form>

      {error && (
        <div className="message error" role="alert">
          {error}
        </div>
      )}

      {result !== null && !error && (
        <div className="message success">
          <span className="label">Preço final:</span>
          <span className="value">{formatBRL(result)}</span>
        </div>
      )}
    </div>
  );
}

export default App;
