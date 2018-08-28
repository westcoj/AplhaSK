'''
Created on Aug 9, 2018

@author: cody.west
'''

import pygame as pg, sys
from pygame.locals import *
import os

class MusicSide(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        #self.__player = pg.mixer.init()
        
    def playSound(self, path):
        #print('Handle Music')
#         self.__player.music.load(path);
#         self.__player.music.play(0)
#         while self.__player.music.get_busy(): 
#             pg.time.Clock().tick(10)
            
        pg.mixer.init()
        #pg.mixer.music.load(path);
        pg.mixer.music.load(path)
        pg.mixer.music.play(0)
        while pg.mixer.music.get_busy(): 
            pg.time.Clock().tick(10)
        #print("played music")
        
        
        
if __name__ == "__main__":
    mu = MusicSide()
    mu.playSound('lol')
#     MusicK = MusicSide("C:\\SoundFiles\\Client\\lz.mp3")
#     MusicK.playSound()
#     threading.Thread(target = MusicK.playSound()).start()
        
#     ClientK = ClientSide("127.0.0.1",1445);
#     ClientK.connecter()
#     while True:
#         command = raw_input("Enter Command")
#         x = ClientK.comSwitch(command)
#         if(x==1):
#             break
#         data = ClientK.getR();
#         print(str(data.decode('ascii')))