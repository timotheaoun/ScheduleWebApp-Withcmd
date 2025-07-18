from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/run', methods=['POST'])
def run_command():
    data = request.get_json()
    cmd = data.get("cmd")
    if not cmd:
        return jsonify({"status": "error", "message": "No command provided"}), 400
    try:
        subprocess.Popen(cmd, shell=True)
        return jsonify({"status": "ok"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5005)
