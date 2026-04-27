import React from 'react';
import styles from './Card.module.css';

export function Card({ title, children, className = '' }) {
  return (
    <section className={`${styles.card} ${className}`}>
      {title && <h2 className={styles.title}>{title}</h2>}
      <div className={styles.content}>
        {children}
      </div>
    </section>
  );
}
