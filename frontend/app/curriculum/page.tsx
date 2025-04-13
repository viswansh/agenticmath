'use client';

import { useEffect, useState } from 'react';
import styles from './page.module.css';

type CurriculumItem = {
  id: number;
  title: string;
  description: string;
};

export default function CurriculumPage() {
  const [items, setItems] = useState<CurriculumItem[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchCurriculum() {
      const res = await fetch('http://localhost:8000/curriculum');
      const data = await res.json();
      setItems(data);
      setLoading(false);
    }

    fetchCurriculum();
  }, []);

  return (
    <main className={styles.container}>
      <h1 className={styles.title}>Curriculum</h1>

      {loading ? (
        <p>Loading...</p>
      ) : (
        <div className={styles.list}>
          {items.map((item) => (
            <div key={item.id} className={styles.card}>
              <h2 className={styles.courseTitle}>{item.title}</h2>
              <p className={styles.description}>{item.description}</p>
            </div>
          ))}
        </div>
      )}
    </main>
  );
}
