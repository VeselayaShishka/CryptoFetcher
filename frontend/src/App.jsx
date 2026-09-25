import { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  const [projects, setProjects] = useState([]);
  const [loading, setLoading] = useState(true);

  const [search, setSearch] = useState('');
  const [maxFdv, setMaxFdv] = useState('');
  const [sortBy, setSortBy] = useState('mcap');

  useEffect(() => {
    fetch('http://localhost:8000/api/crypto')
      .then(res => res.json())
      .then(data => {
        setProjects(data);
        setLoading(false);
      })
      .catch(err => {
        console.error("Error fetching data:", err);
        setLoading(false);
      });
  }, []);

  const filteredAndSortedProjects = projects
    .filter(p => p.name.toLowerCase().includes(search.toLowerCase()) || p.symbol.toLowerCase().includes(search.toLowerCase()))
    .filter(p => maxFdv === '' || (p.fully_diluted_valuation && p.fully_diluted_valuation < Number(maxFdv)))
    .sort((a, b) => {
      if (sortBy === 'mcap') return b.market_cap - a.market_cap;
      if (sortBy === 'volume') return b.total_volume - a.total_volume;
      return 0;
    });

  return (
    <div className="container mt-4">
      <h2 className="mb-4">Crypto Project Screener</h2>

      <div className="row mb-4">
        <div className="col-md-4">
          <input
            type="text"
            className="form-control"
            placeholder="Search by name (e.g., eth)..."
            value={search}
            onChange={e => setSearch(e.target.value)}
          />
        </div>
        <div className="col-md-4">
          <input
            type="number"
            className="form-control"
            placeholder="Max FDV (e.g., 50000000)"
            value={maxFdv}
            onChange={e => setMaxFdv(e.target.value)}
          />
        </div>
        <div className="col-md-4">
          <select
            className="form-select"
            value={sortBy}
            onChange={e => setSortBy(e.target.value)}
          >
            <option value="mcap">Sort by Market Cap</option>
            <option value="volume">Sort by 24h Volume</option>
          </select>
        </div>
      </div>

      {loading ? (
        <p>Loading data from backend...</p>
      ) : (
        <table className="table table-striped table-hover">
          <thead className="table-dark">
            <tr>
              <th>Name</th>
              <th>Symbol</th>
              <th>Market Cap</th>
              <th>FDV</th>
              <th>24h Volume</th>
            </tr>
          </thead>
          <tbody>
            {filteredAndSortedProjects.map(p => (
              <tr key={p.id}>
                <td>{p.name}</td>
                <td>{p.symbol.toUpperCase()}</td>
                <td>${p.market_cap.toLocaleString()}</td>
                <td>{p.fully_diluted_valuation ? `$${p.fully_diluted_valuation.toLocaleString()}` : 'N/A'}</td>
                <td>${p.total_volume.toLocaleString()}</td>
              </tr>
            ))}
            {filteredAndSortedProjects.length === 0 && (
              <tr>
                <td colSpan="5" className="text-center">No projects match the criteria.</td>
              </tr>
            )}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default App;