from flask import Flask, request, jsonify, render_template_string
import os

app = Flask(__name__)
flag_dir = "/flags"
submitted_flags = {}

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
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(TEMPLATE, flags=submitted_flags)

@app.route('/submit', methods=['POST'])
def submit_flag():
    data = request.get_json()
    service = data.get('service')
    submitted_flag = data.get('flag')

    try:
        with open(os.path.join(flag_dir, f"{service}/flag.txt")) as f:
            correct_flag = f.read().strip()
    except FileNotFoundError:
        return jsonify({"error": "Service inconnu"}), 404

    valid = submitted_flag.strip() == correct_flag
    submitted_flags[service] = {
        "flag": submitted_flag,
        "valid": valid
    }
    return jsonify({"valid": valid})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
