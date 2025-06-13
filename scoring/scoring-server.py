from flask import Flask, request, jsonify
import os

app = Flask(__name__)

FLAG_DIR = "../flags/"
flags = {
    "dvwa": open(FLAG_DIR + "dvwa/flag.txt").read().strip(),
    "ftp": open(FLAG_DIR + "ftp/flag.txt").read().strip(),
    "ssh": open(FLAG_DIR + "ssh/flag.txt").read().strip(),
}

@app.route("/submit", methods=["POST"])
def submit_flag():
    data = request.get_json()
    service = data.get("service")
    submitted = data.get("flag")
    correct = flags.get(service) == submitted
    return jsonify({"valid": correct})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
