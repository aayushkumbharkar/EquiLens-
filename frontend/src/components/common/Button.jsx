import React from 'react';
import styles from './Button.module.css';

export function Button({ 
  children, 
  onClick, 
  disabled = false, 
  isLoading = false, 
  variant = 'primary',
  ariaLabel
}) {
  return (
    <button
      className={`${styles.button} ${styles[variant]}`}
      onClick={onClick}
      disabled={disabled || isLoading}
      aria-disabled={disabled || isLoading}
      aria-busy={isLoading}
      aria-label={ariaLabel}
    >
      {isLoading ? <span className={styles.spinner} aria-hidden="true" /> : null}
      <span className={isLoading ? styles.hiddenText : ''}>{children}</span>
      {isLoading ? <span className={styles.loadingText}>Loading...</span> : null}
    </button>
  );
}
