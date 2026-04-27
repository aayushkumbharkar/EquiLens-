import React from 'react';
import styles from './ScoreDisplay.module.css';

export function ScoreDisplay({ score }) {
  return (
    <div className={styles.scoreContainer}>
      <div className={styles.scoreValue} aria-label={`Fairness Score: ${score}%`}>
        {score}%
      </div>
      <div className={styles.scoreLabel} aria-hidden="true">Fairness Score</div>
    </div>
  );
}
