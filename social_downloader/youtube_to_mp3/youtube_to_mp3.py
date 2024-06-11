# importing packages 
from pytube import YouTube 
import os 
import sys
def download_mp3(input_):
    while True:
        # url input from user#
        
        yt = YouTube(str(input_)) 
          
        # extract only audio 
        video = yt.streams.filter(only_audio=True).first() 
          
        # check for destination to save file 
        destination = "downloads/"
          
        # download the file 

        out_file = video.download(output_path=destination) 
          
        
        # result of success 
        print(yt.title + " has been successfully downloaded.")
    
        if input_ == "exit":
            sys.exit()
        if not __name__ == '__main__':
            return destination + yt.title +".mp3"
            break

if __name__ == '__main__':
        input_ = input("Enter the URL of the video you want to download (or type exit to exit): \n>> ")
        download_mp3(input_)