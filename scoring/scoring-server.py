import os
from flask import Flask, request, jsonify, render_template_string
import sqlite3

app = Flask(__name__)
flag_dir = "/flags"

DATABASE = "scoring/scoring.db"

# Création de la base SQLite si inexistante
def init_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS submissions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            service TEXT NOT NULL,
            flag TEXT NOT NULL,
            valid INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

def insert_submission(service, flag, valid):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("INSERT INTO submissions (service, flag, valid) VALUES (?, ?, ?)", (service, flag, valid))
    conn.commit()
    conn.close()

def get_submissions():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT service, flag, valid FROM submissions ORDER BY id DESC")
    rows = c.fetchall()
    conn.close()
    result = {}
    for service, flag, valid in rows:
        # Garde la dernière soumission par service (optionnel)
        if service not in result:
            result[service] = {"flag": flag, "valid": bool(valid)}
    return result

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Scoring</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="p-5">
    <h1 class="mb-4">Scoring Offensive Lab</h1>
    <table class="table table-bordered">
        <thead>
            <tr><th>Service</th><th>Flag soumis</th><th>Statut</th></tr>
        </thead>
        <tbody>
            {% for service, result in flags.items() %}
            <tr>
                <td>{{ service }}</td>
                <td>{{ result['flag'] }}</td>
                <td>
                    {% if result['valid'] %}
                        ✅ Valide
                    {% else %}
                        ❌ Invalide
                    {% endif %}
                </td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
    <p>Soumettez un flag via l'endpoint POST /submit (JSON : {service: ..., flag: ...})</p>
</body>
</html>
"""

@app.route('/')
def index():
    flags = get_submissions()
    return render_template_string(TEMPLATE, flags=flags)

@app.route('/submit', methods=['POST'])
def submit_flag():
    data = request.get_json()
    service = data.get('service')
    submitted_flag = data.get('flag')

    if not service or not submitted_flag:
        return jsonify({"error": "Paramètres manquants"}), 400

    try:
        with open(os.path.join(flag_dir, f"{service}/flag.txt")) as f:
            correct_flag = f.read().strip()
    except FileNotFoundError:
        return jsonify({"error": "Service inconnu"}), 404

    valid = submitted_flag.strip() == correct_flag
    insert_submission(service, submitted_flag, int(valid))

    return jsonify({"valid": valid})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
