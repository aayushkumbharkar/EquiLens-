import React from 'react';
import styles from './Alert.module.css';

export function Alert({ message, type = 'error' }) {
  if (!message) return null;
  return (
    <div className={`${styles.alert} ${styles[type]}`} role="alert">
      {message}
    </div>
  );
}
