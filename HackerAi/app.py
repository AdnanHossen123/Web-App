

from flask import Flask, render_template, request, jsonify
import requests
import os
from datetime import datetime

app = Flask(__name__)

GITHUB_TOKEN = "ghp_তোমার_TOKEN_এখানে_পেস্ট_করো"  # তোমার token
GITHUB_USERNAME = "তোমার_GitHub_username"  # তোমার username
REPO_NAME = "তোমার_repo_name"  # repo name
FILE_PATH = "notes.txt"  # ফাইলের নাম

GITHUB_API_URL = f"https://api.github.com/repos/{GITHUB_USERNAME}/{REPO_NAME}/contents/{FILE_PATH}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save_note():
    try:
        note = request.json.get('note')
        if not note or note.strip() == "":
            return jsonify({'error': 'Sumthing write!'}), 400
        
        response = requests.get(GITHUB_API_URL, headers={
            'Authorization': f'token {GITHUB_TOKEN}',
            'Accept': 'application/vnd.github.v3+json'
        })
        
        if response.status_code == 404:
            content = note
            sha = None
        else:
            data = response.json()
            content = base64.b64decode(data['content']).decode('utf-8')
            sha = data['sha']
            content += f"\n{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | {note}"
        
        update_data = {
            'message': f'নতুন নোট যোগ: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}',
            'content': base64.b64encode(content.encode('utf-8')).decode('utf-8'),
            'sha': sha
        }
        
        response = requests.put(GITHUB_API_URL, headers={
            'Authorization': f'token {GITHUB_TOKEN}',
            'Accept': 'application/vnd.github.v3+json'
        }, json=update_data)
        
        if response.status_code in [200, 201]:
            return jsonify({'success': True, 'message': 'saved ! 🎉'})
        else:
            return jsonify({'error': 'Sumthing Wrang! Cheakh token/repo'}), 500
            
    except Exception as e:
        return jsonify({'error': f'Error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)