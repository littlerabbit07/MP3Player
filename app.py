from flask import Flask, render_template, send_from_directory
import os
import random

app = Flask(__name__)

# Set this to the full path of your external music folder
MUSIC_FOLDER = "/home/natalia/Music"  # Change this to your folder path

@app.route('/')
def index():
    tracks = []
    if os.path.isdir(MUSIC_FOLDER):
        for root, dirs, files in os.walk(MUSIC_FOLDER):
            for f in files:
                if f.endswith('.mp3'):
                    # Store relative path from MUSIC_FOLDER for serving
                    rel_dir = os.path.relpath(root, MUSIC_FOLDER)
                    rel_file = os.path.join(rel_dir, f) if rel_dir != '.' else f
                    tracks.append(rel_file)
        random.shuffle(tracks)
    return render_template('index.html', tracks=tracks)

# Route to serve the MP3 files from external folder
@app.route('/music/<path:filename>')
def music(filename):
    return send_from_directory(MUSIC_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)
