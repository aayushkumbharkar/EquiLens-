import React from 'react';
import styles from './TextArea.module.css';

export function TextArea({ 
  id,
  value, 
  onChange, 
  placeholder, 
  disabled = false, 
  error,
  label 
}) {
  return (
    <div className={styles.container}>
      {label && <label htmlFor={id} className={styles.label}>{label}</label>}
      <textarea
        id={id}
        className={`${styles.textarea} ${error ? styles.textareaError : ''}`}
        value={value}
        onChange={onChange}
        placeholder={placeholder}
        disabled={disabled}
        aria-invalid={!!error}
        aria-describedby={error ? `${id}-error` : undefined}
      />
      {error && <span id={`${id}-error`} className={styles.errorText} role="alert">{error}</span>}
    </div>
  );
}
