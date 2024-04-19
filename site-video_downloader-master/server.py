from flask import Flask, request, send_file, send_from_directory
from pytube import YouTube
import os

app = Flask(__name__)

@app.route("/")
def index():
    return send_file("templates\\index.html")

@app.route("/baixar")
def baixar():
    link = request.args.get("link")
    
    try:
        yt = YouTube(link)
        video = yt.streams.get_highest_resolution()

        # Definindo o caminho para a pasta de downloads desejada
        downloads_path = r"C:\Users\ferna\Downloads"

        # Criando o caminho completo para o vídeo na pasta de downloads
        video_path = os.path.join(downloads_path, yt.title + '.mp4')

        # Baixando e salvando o vídeo na pasta de downloads
        video.download(filename=video_path)

        return f"Download concluído! O vídeo foi salvo em {downloads_path}"
    except Exception as e:
        return str(e)

@app.route("/static/<path:path>")
def serve_static(path):
    return send_from_directory("static", path)

if __name__ == "__main__":
    app.run(debug=True)