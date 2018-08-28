'''
Created on Aug 8, 2018

@author: cody.west
'''
from socket import *
from pip._vendor.distlib.compat import raw_input
from SKPkg.MusicSide import MusicSide
import struct
from sys import stdout


class ClientSide(object):
    '''
    classdocs
    '''

    def __init__(self, ip, port): 
        '''
        Constructor
        '''
        self.__hostname = ip
        self.__port = port
        self.__socket = socket(AF_INET, SOCK_STREAM)
        #self.__socket.setblocking(True)
        self.__moosic = MusicSide()
        self.__dirHolder = []
        self.__dir2 =""
        self.testSize = 0
        
    def connecter(self):
        self.__socket = socket(AF_INET, SOCK_STREAM)
        self.__socket.connect((self.__hostname, self.__port))
        
    """
    Start True Data Handling Methods
    """
    
    def trueSend(self, data):
        data = struct.pack('>I', len(data)) + data
        self.__socket.sendall(data)
        
    def trueRecv(self):
        rawSize = self.trueAll(4)
        if not rawSize:
            return None
        dataSize = struct.unpack('>I', rawSize)[0]
        print('First Data: ' + str(dataSize))
        print('hi')
        # Read the message data
        return self.trueAll(dataSize)
    
    def trueAll(self, length):
        # Helper function to recv n bystes or return None if EOF is hit
        print('Second Data: ' + str(length))
        data = b''
        i = 0
        while len(data) < length:
            print(i)
            i+=1
            packet = self.__socket.recv(length - len(data))
            if not packet:
                print('Found no more data: ' + len(data))
                return None
            data += packet
            print(str(len(data)) + ' Data Got||Total: ' + str(length))
        return data
        
    """
    End True Data Handling Methods
    """
        
    def msgService(self):
        msg = raw_input("Enter Message: ");
        self.__socket.send((msg.encode('ascii')))
        
#     def handleMusic(self, path):
#         print('Handle Music')
#         self.__moosic.playSound("C:\\SoundFiles\\Client\\lz.mp3")
#         mixer.init()
#         mixer.music.load(path)
#         mixer.music.play()

#     def dirGrab(self):
#         self.__socket.send('ls'.encode('ascii'))
#         while(True):
#             tsData = self.__socket.recv(1024)
#             ts = tsData.decode();
# #         dataSize = self.__socket.recv(1024);
# #         grabSize = int(dataSize.decode('ascii'))
# #         print(grabSize)
# #         data = self.__socket.recv(grabSize)
# #         self.__dirHolder = pickle.loads(data)
        
    def getDirHolder(self):
#         return self.__dirHolder
        return self.__dir2
        
#     def comSwitch(self, com):
#         if(com == "Send"):
#             self.msgService();
#             return 0
#         if(com == "Exit"):
#             self.disconnect();
#             return 1;
#         if(com == 'File'):
#             x = self.fileHandlerGUI('06 Red Balloon - Bailiff-b7EGU0lq-6g');
#             if(x == 1):
#                 return 1;
#             if(x == 0):
#                 return 0;
#         if(com == 'ls'):
#             self.dirGrab()
#         
    def disconnect(self):
        self.__socket.close();
        
#     def getR(self):
#         size = 1024
#         data = self.__socket.recv(size)
#         return data
#     
#     def blockRecv(self, cs):
#         data = self.__socket.recv()
#         if(not data):
#             while (not data):
#                 data = self.__socket.recv()
#                 
#     def bytes_to_int(self, gBytes):
#         return int(gBytes.encode('hex'), 16)
    
    
#     def fileHandlerGUI(self, path):
#         self.__socket.send('File'.encode('ascii'))
#         data = self.__socket.recv(1024)
#         #fileName = raw_input(str(data.decode('ascii')))
# #             need check here to see client doesn't have file already...
#         #self.__socket.send(fileName.encode('ascii'))
#         self.__socket.send(path.encode())
#         print("FileName Sent")
#         #print(path);
#         data = self.__socket.recv(1024)
#         #while(not data):
#             #data = self.__socket.recv(1024)
#         fileSizeS = int(data.decode('ascii'))
# #           print(fileSizeS);
#         print('File Size: ', fileSizeS)
#         fileSize = int(fileSizeS)
#         if(fileSize == -1):
#             print('Error with file');
#             return 0
#         attempts = fileSize / 1024
#         final = fileSize % 1024
#         print('File Size: ', fileSize)
#         print('Attempts: ', attempts)
#         print('Final Size: ', final)
#         file = open("C:\\SoundFiles\\Client\\" + path + '.mp3', 'wb+')
#         bytesC = 0
#         i = 1
#         while(i < attempts):
#             data = self.__socket.recv(1024)
#             file.write(data)
#             i += 1
#             bytesC += 1024
#             print(i, ' :I | A: ', attempts, 'Bytes: ', bytesC)
#         
#         print('grabbing final');
#         data = self.__socket.recv(final)
#         print('Got final')
#         file.write(data)
#         file.close(); 
#         return 1
    
    def fileHandler2(self,name):
        self.trueSend(name.encode())
        fileData = self.trueRecv()
        print(len(fileData))
        file = open("C:\\SoundFiles\\Client\\" + name, 'wb+')        
        file.write(fileData);
        file.close();
        return 1
#         try:
#             self.trueSend(name.encode())
#             fileData = self.trueRecv()
#             print(len(fileData))
#             file = open("C:\\SoundFiles\\Client\\" + name, 'wb+')        
#             file.write(fileData);
#             file.close();
#             return 1
#         except:
#             return -1
    
#     def fileHandler(self):
#         self.__socket.send('File'.encode('ascii'))
#         data = self.__socket.recv(1024)
#         #fileName = raw_input(str(data.decode('ascii')))
#         # need check here to see client doesn't have file already...
#         # self.__socket.send(fileName.encode('ascii'))
#         self.__socket.send('lz.mp3'.encode('ascii'))
#         print("FileName Sent")
#         # print(fileName);
#         data = self.__socket.recv(1024)
#         while(not data):
#             data = self.__socket.recv(1024)
#         fileSizeS = int(data.decode('ascii'))
#         print(fileSizeS);
#         print('File Size: ', fileSizeS)
#         fileSize = int(fileSizeS)
#         if(fileSize == -1):
#             print('Error with file');
#             return 0
#         attempts = fileSize / 1024
#         final = fileSize % 1024
#         print('File Size: ', fileSize)
#         print('Attempts: ', attempts)
#         print('Final Size: ', final)
#         file = open("C:\\SoundFiles\\Client\\lz.mp3", 'wb+')
#         bytesC = 0
#         i = 1
#         while(i < attempts):
#             data = self.__socket.recv(1024)
#             file.write(data)
#             i += 1
#             bytesC += 1024
#             print(i, ' :I | A: ', attempts, 'Bytes: ', bytesC)
#             
#         print('grabbing final');
#         data = self.__socket.recv(final)
#         print('Got final')
#         file.write(data)
#         file.close();
#         print('Going to Music')
#         self.handleMusic("C:\\SoundFiles\\Client\\lz.mp3")
#         return 1
    
    
    def dirGrab2(self):
        self.trueSend('ls'.encode())
        data = self.trueRecv().decode()
        return data.split('\n')
    
    
    def commSwitch2(self,comm):
        self.connecter();
        if(comm=='ls'):
            self.__dir2 = self.dirGrab2()
        else:
            stdout.write('handling file request')
            return self.fileHandler2(comm)
        self.disconnect()
            
    def giveDir2(self):
        return self.__dir2();
                           
    
if __name__ == "__main__":
    ClientK = ClientSide("127.0.0.1", 1445);
    #ClientK.connecter()
    while True:
        #command = raw_input("Enter Command")
#         ClientK.connecter()
#         ClientK.trueSend("'Pridemoor Keep' Shovel Knight Remix-k3IKgJUTjlM.mp3".encode())
        ClientK.commSwitch2("'Pridemoor Keep' Shovel Knight Remix-k3IKgJUTjlM.mp3")
        print('done')
        break

        
