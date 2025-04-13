'use client';

import { useState } from 'react';
import styles from './page.module.css';

import Link from 'next/link';
// inside JSX
<Link href="/curriculum" className={styles.link}>View Curriculum</Link>


export default function HomePage() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [token, setToken] = useState('');
  const [error, setError] = useState('');

  async function handleLogin() {
    try {
      const res = await fetch('http://localhost:8000/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password }),
      });

      const data = await res.json();

      if (!res.ok) {
        setError(data.detail || 'Login failed');
        setToken('');
        return;
      }

      setToken(data.access_token);
      setError('');
    } catch (err) {
      setError('Network error');
      setToken('');
    }
  }

  return (
    <main className={styles.container}>
      <h1 className={styles.title}>Login</h1>

      <input
        className={styles.input}
        placeholder="Username"
        onChange={(e) => setUsername(e.target.value)}
      />

      <input
        className={styles.input}
        type="password"
        placeholder="Password"
        onChange={(e) => setPassword(e.target.value)}
      />

      <button className={styles.button} onClick={handleLogin}>
        Login
      </button>

      {error && <p className={styles.error}>{error}</p>}
      {token && <p className={styles.token}>Token: {token}</p>}
    </main>
  );
}
