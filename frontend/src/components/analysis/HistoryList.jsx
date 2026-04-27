import React, { useEffect, useState } from 'react';
import { analysisService } from '../../services/api';
import { Card } from '../common/Card';
import { Badge } from '../common/Badge';
import { Button } from '../common/Button';
import { Alert } from '../common/Alert';

export function HistoryList() {
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const fetchHistory = async () => {
    setLoading(true);
    try {
      const data = await analysisService.getHistory();
      setHistory(data);
      setError(null);
    } catch (err) {
      setError("Failed to fetch history");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchHistory();
  }, []);

  return (
    <div style={{ marginTop: '24px', display: 'flex', flexDirection: 'column', gap: '16px' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <h2 style={{ color: '#fff', margin: 0 }}>Analysis History</h2>
        <Button onClick={fetchHistory} disabled={loading} variant="secondary">
          Refresh
        </Button>
      </div>

      <Alert message={error} type="error" />

      {loading && !history.length ? (
        <div style={{ textAlign: 'center', color: '#999', padding: '20px' }} aria-busy="true">
          Loading history...
        </div>
      ) : null}

      {!loading && history.length === 0 && !error ? (
        <div style={{ textAlign: 'center', color: '#999', padding: '20px' }}>
          No past analyses found.
        </div>
      ) : null}

      <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
        {history.map(record => (
          <Card key={record.id}>
            <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '12px' }}>
              <strong style={{ color: '#646cff' }}>Fairness Score: {record.fairness_score}%</strong>
              <Badge status={record.bias_detected ? 'error' : 'success'}>
                {record.bias_detected ? 'Bias Detected' : 'Fair'}
              </Badge>
            </div>
            <p style={{ color: '#999', margin: '4px 0', fontSize: '0.95rem' }}>
              <strong>Prompt:</strong> {record.prompt}
            </p>
            <p style={{ margin: '8px 0', fontSize: '0.95rem', color: '#ddd' }}>
              <strong>Explanation:</strong> {record.explanation}
            </p>
            <small style={{ color: '#666' }}>{new Date(record.created_at).toLocaleString()}</small>
          </Card>
        ))}
      </div>
    </div>
  );
}
