import webbrowser
from flask import Flask, render_template, request
import os

webbrowser.open('http://127.0.0.1:5000/')

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/output', methods=["GET","POST"])
def output():
	downloader_type = request.form["downloader_type"]
	url = request.form["url"]
	link_downloads = ""
	if not url.startswith("http"):
		return "<h1>This is not a valid url</h1>"
	if downloader_type == "youtube_mp3":
		from youtube_to_mp3.youtube_to_mp3 import download_mp3
		link_download = download_mp3(url)
	elif downloader_type == "all_youtube_mp3":
		from youtube_to_mp3.youtube_all_video_on_page_mp3_downloader import page_mp3_youtube_download
		link_downloads = page_mp3_youtube_download(url)

	return render_template('output.html', link=link_download, real_link = os.getcwd()+"/"+link_download, links=link_downloads)

@app.route('/downloads_folder')
def downloads_folder():
	os.startfile("C:/Users/djm/Documents/GitHub/Lord-Oxygen/social_downloader/downloads")
	return 

if __name__ == '__main__':
	app.run(debug=False)