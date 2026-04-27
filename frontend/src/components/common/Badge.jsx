import React from 'react';
import styles from './Badge.module.css';

export function Badge({ status = 'neutral', children }) {
  return (
    <span className={`${styles.badge} ${styles[status]}`}>
      {children}
    </span>
  );
}
