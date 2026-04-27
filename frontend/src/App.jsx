import { useState, useRef } from 'react';
import './App.css';
import { analysisService } from './services/api';
import { HistoryList } from './components/analysis/HistoryList';
import { ResultsDashboard } from './components/analysis/ResultsDashboard';
import { Button } from './components/common/Button';
import { TextArea } from './components/common/TextArea';
import { Card } from './components/common/Card';
import { Alert } from './components/common/Alert';

function App() {
  const [prompt, setPrompt] = useState('');
  const [isGenerating, setIsGenerating] = useState(false);
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [originalDecision, setOriginalDecision] = useState(null);
  const [analysisResult, setAnalysisResult] = useState(null);
  const [error, setError] = useState(null);
  const [showHistory, setShowHistory] = useState(false);
  
  const isRequestingRef = useRef(false);

  const handleGenerate = async () => {
    if (!prompt.trim() || isRequestingRef.current) return;
    
    isRequestingRef.current = true;
    setIsGenerating(true);
    setOriginalDecision(null);
    setAnalysisResult(null);
    setError(null);
    
    try {
      const data = await analysisService.generate(prompt);
      setOriginalDecision(data.decision);
      
      // Automatically proceed to analysis
      handleAnalyze(prompt, data.decision);
    } catch (err) {
      setError(err.message || 'Error connecting to server');
      setIsGenerating(false);
      isRequestingRef.current = false;
    }
  };

  const handleAnalyze = async (currentPrompt, decision) => {
    setIsGenerating(false);
    setIsAnalyzing(true);
    
    try {
      const data = await analysisService.evaluate(currentPrompt, decision);
      setAnalysisResult(data);
    } catch (err) {
      setError(err.message || 'Error connecting to server');
    } finally {
      setIsAnalyzing(false);
      isRequestingRef.current = false;
    }
  };

  return (
    <div className="app-container">
      <header className="header">
        <h1>EquiLens</h1>
        <p>AI Bias Detection API MVP (Production Ready)</p>
      </header>

      <div style={{ display: 'flex', justifyContent: 'flex-end', marginBottom: '16px' }}>
        <Button onClick={() => setShowHistory(!showHistory)} variant="secondary">
          {showHistory ? "Back to Analysis" : "View History"}
        </Button>
      </div>

      {showHistory ? (
        <HistoryList />
      ) : (
        <>
          <Card className="input-section">
            <TextArea
              id="main-prompt"
              placeholder='e.g., "Select the best candidate for a software engineering role between Rahul and Riya with identical qualifications."'
              value={prompt}
              onChange={(e) => setPrompt(e.target.value)}
              disabled={isGenerating || isAnalyzing}
            />
            <div style={{ display: 'flex', justifyContent: 'flex-end', marginTop: '16px' }}>
              <Button 
                onClick={handleGenerate}
                disabled={!prompt.trim()}
                isLoading={isGenerating || isAnalyzing}
              >
                Submit & Analyze
              </Button>
            </div>
          </Card>
          
          <Alert message={error} type="error" />

          {originalDecision && (
            <Card title="Original AI Decision" className="decision-section">
              <div style={{ whiteSpace: 'pre-wrap', lineHeight: '1.6', color: '#ddd' }}>
                {originalDecision}
              </div>
            </Card>
          )}

          <ResultsDashboard result={analysisResult} />
        </>
      )}
    </div>
  );
}

export default App;
