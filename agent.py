from flask import Flask, request
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)

@app.route('/run', methods=['POST'])
def run():
    data = request.json
    cmd = data.get('cmd')
    if not cmd:
        return {'error': 'Aucune commande reçue'}, 400
    try:
        subprocess.Popen(cmd, shell=True)
        return {'ok': True}
    except Exception as e:
        return {'error': str(e)}, 500

if __name__ == '__main__':
    app.run(port=5005)
