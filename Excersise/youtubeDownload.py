# make sure you have PyTube library
# If not, then install via pip
# pip install pytube
# once installation is successfull, you can run this code and enjoy.

from pytube import YouTube

YouTube('https://www.youtube.com/watch?v=ID_OF_THE_VIDEO').streams.first().download()
