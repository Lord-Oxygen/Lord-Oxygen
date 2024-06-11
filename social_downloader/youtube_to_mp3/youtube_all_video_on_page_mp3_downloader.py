#youtube_all_video_on_page_mp3_downloader https://www.youtube.com/@JadaFacer/videos

# import HTMLSession from requests_html
from requests_html import HTMLSession
from bs4 import BeautifulSoup
if __name__ == '__main__':
	from youtube_to_mp3 import download_mp3
else:
	from youtube_to_mp3.youtube_to_mp3 import download_mp3


def get_all_the_links(url):
	not_done = True
	while not_done:
		print("|", end="")
		# create an HTML Session object
		session = HTMLSession()
		 
		# Use the object above to connect to needed webpage
		resp = session.get(url)
		 
		# Run JavaScript code on webpage
		resp.html.render()
		html_page = resp.html.html
		link_dict = {}# {/watch?v=asdh12 : True}
		soup = BeautifulSoup(html_page, features="lxml")
		for link in soup.findAll('a'):
			watch_link = str(link.get('href'))
			if watch_link.startswith("/watch"):
				link_dict["https://www.youtube.com"+watch_link] = True
				if len(link_dict) > 2:
					not_done = False
		resp.session.close()
	
	link_list = []
	for link in link_dict.keys(): link_list.append(link)
	return link_list
def page_mp3_youtube_download(url):
	link_list = get_all_the_links(url)
	link_downloads = []
	for link in link_list:
		link_download = download_mp3(link)
		link_downloads.append(link_download)
	return link_downloads

if __name__ == '__main__':
	url = input("Enter the URL of the page with the videos you want to download\n>>")
	page_mp3_youtube_download(url)