import sqlite3
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB = BASE_DIR / 'comments.db'
PROFANITY_FILE = BASE_DIR / 'profanities.txt'

def load_profanities():
    if not PROFANITY_FILE.exists():
        return []
    with open(PROFANITY_FILE, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

def main():
    bad = load_profanities()
    if not bad:
        print('No profanities defined; nothing to do')
        return
    pattern = re.compile(r'(' + '|'.join(re.escape(w) for w in bad) + r')', re.IGNORECASE)
    conn = sqlite3.connect(DB)
    cur = conn.execute('SELECT id, text FROM comments')
    rows = cur.fetchall()
    removed = 0
    for r in rows:
        if pattern.search(r[1]):
            conn.execute('DELETE FROM comments WHERE id=?', (r[0],))
            removed += 1
    conn.commit()
    conn.close()
    print(f'Removed {removed} comments')

if __name__ == '__main__':
    main()
