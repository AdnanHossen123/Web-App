
from flask import Flask, render_template, request, redirect, url_for
import requests
import base64
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()  # .env থেকে ভ্যারিয়েবল লোড

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_OWNER = os.getenv('GITHUB_OWNER')
GITHUB_REPO = os.getenv('GITHUB_REPO')
FILE_PATH = os.getenv('FILE_PATH')

# GitHub API হেডার
headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_data = request.form['data']  # ফর্ম থেকে নতুন ডেটা
        if new_data:
            # প্রথমে বিদ্যমান ফাইল কনটেন্ট GET করো
            url = f"https://api.github.com/repos/{GITHUB_OWNER}/{GITHUB_REPO}/contents/{FILE_PATH}"
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                file_info = response.json()
                sha = file_info['sha']  # SHA দরকার আপডেটের জন্য
                current_content = base64.b64decode(file_info['content']).decode('utf-8')

                # নতুন ডেটা অ্যাপেন্ড (নতুন লাইন যোগ)
                updated_content = current_content + '\n' + new_data

                # Base64 এনকোড
                encoded_content = base64.b64encode(updated_content.encode('utf-8')).decode('utf-8')

                # PUT রিকোয়েস্ট দিয়ে আপডেট
                payload = {
                    'message': 'Appended new data from web app',
                    'content': encoded_content,
                    'sha': sha
                }
                update_response = requests.put(url, headers=headers, json=payload)

                if update_response.status_code == 200:
                    return redirect(url_for('index'))  # সাকসেস, রিফ্রেশ
                else:
                    return "Error updating file: " + update_response.text
            else:
                return "Error fetching file: " + response.text
        else:
            return "No data provided!"

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)