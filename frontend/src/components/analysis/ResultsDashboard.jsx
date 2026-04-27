import React from 'react';
import { Card } from '../common/Card';
import { Badge } from '../common/Badge';
import { ScoreDisplay } from './ScoreDisplay';
import styles from './ResultsDashboard.module.css';

export function ResultsDashboard({ result }) {
  if (!result) return null;

  const isBiased = result.bias_detected;

  return (
    <Card className={styles.dashboard}>
      <div className={styles.header}>
        <div className={styles.badgeWrapper}>
          <Badge status={isBiased ? 'error' : 'success'}>
            {isBiased ? 'Bias Detected' : 'No Bias Detected'}
          </Badge>
        </div>
        <ScoreDisplay score={result.fairness_score} />
      </div>
      
      <div className={styles.section}>
        <h3 className={styles.sectionTitle}>Explanation</h3>
        <div className={styles.textBlock} aria-live="polite">
          {result.explanation}
        </div>
      </div>
      
      <div className={styles.section}>
        <h3 className={styles.sectionTitle}>Suggested Unbiased Output</h3>
        <div className={styles.textBlock} aria-live="polite">
          {result.suggested_fix}
        </div>
      </div>
    </Card>
  );
}
