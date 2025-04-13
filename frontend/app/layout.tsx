import './globals.css';
import Link from 'next/link';
import styles from './layout.module.css';

export const metadata = {
  title: 'Learning App',
  description: 'Curriculum-based learning platform',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className={styles.body}>
        <nav className={styles.nav}>
          <Link href="/" className={styles.navLink}>Home</Link>
          <Link href="/curriculum" className={styles.navLink}>Curriculum</Link>
        </nav>
        <main className={styles.main}>{children}</main>
      </body>
    </html>
  );
}
