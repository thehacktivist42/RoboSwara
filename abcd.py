import re
import vlc
import pafy
import sys
url = "https://www.youtube.com/watch?v=G0OqIkgZqlA"                                                                                            
video = pafy.new(url)                                                                                                                          
best = video.getbestaudio()                                                                                                                    
playurl = best.url                                                                                                                             
player = vlc.MediaPlayer(playurl)                                                                                                              
player.play()
