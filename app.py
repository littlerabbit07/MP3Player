from flask import Flask, render_template, send_from_directory
import os
import random

app = Flask(__name__)

# Set this to the full path of your external music folder
MUSIC_FOLDER = "D:/Music"  # Change this to your folder path

@app.route('/')
def index():
    if os.path.isdir(MUSIC_FOLDER):
        tracks = [f for f in os.listdir(MUSIC_FOLDER) if f.endswith('.mp3')]
        random.shuffle(tracks)
    else:
        tracks = []
    return render_template('index.html', tracks=tracks)

# Route to serve the MP3 files from external folder
@app.route('/music/<filename>')
def music(filename):
    return send_from_directory(MUSIC_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)
