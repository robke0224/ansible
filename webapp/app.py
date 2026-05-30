from flask import Flask, request, redirect, render_template_string
import sqlite3
from pathlib import Path

DB = 'comments.db'
app = Flask(__name__)

TEMPLATE = '''
<!doctype html>
<title>Comments</title>
<h1>Leave a comment</h1>
<form method=post>
  <textarea name=comment rows=4 cols=50></textarea><br>
  <button type=submit>Post</button>
</form>
<h2>Comments</h2>
{% for c in comments %}
  <div style="border:1px solid #ddd;padding:8px;margin:8px 0">{{c[1]}}</div>
{% endfor %}
'''

def init_db():
    if not Path(DB).exists():
        conn = sqlite3.connect(DB)
        conn.execute('CREATE TABLE comments (id INTEGER PRIMARY KEY, text TEXT)')
        conn.commit()
        conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    init_db()
    conn = sqlite3.connect(DB)
    if request.method == 'POST':
        txt = request.form.get('comment','').strip()
        if txt:
            conn.execute('INSERT INTO comments (text) VALUES (?)', (txt,))
            conn.commit()
        return redirect('/')
    cur = conn.execute('SELECT id, text FROM comments ORDER BY id DESC')
    comments = cur.fetchall()
    conn.close()
    return render_template_string(TEMPLATE, comments=comments)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
