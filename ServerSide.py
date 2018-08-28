'''
Created on Aug 7, 2018

@author: cody.west
'''
from socket import *
from _socket import SOCK_STREAM, AF_INET
from _thread import *
import threading
import os
import struct

class ServerSide(object):
    '''
    Classdocs
    Class for handling server side issues. Distributing files amongst client(s).

    '''


    def __init__(self, ip, port):
        '''
        Constructor
        Class for handling server side issues. Distributing files amongst client(s).
        '''
        
        self.__SS = socket(AF_INET,SOCK_STREAM,0);
        self.__hostname = "127.0.0.1" #self.__SS.gethostname();
        self.__port = 1445;
        self.__SS.bind((self.__hostname,self.__port));
        self.__dir = self.directory();
        self.__strDir = self.dirChange()
        
    def listen(self):
        self.__SS.listen(5)
        while(True):
            CS,CS_Addr = self.__SS.accept();
            CS.settimeout(200)
            #CS.setblocking(True)
            #threading.Thread(target = self.clientHandler, args = (CS, CS_Addr)).start()
            threading.Thread(target = self.clientHandler2, args = (CS, CS_Addr)).start()
            
    """
    Start True Data Handling Methods
    """
    
    def trueSend(self,socket, data):
        data = struct.pack('>I', len(data)) + data
        socket.sendall(data)
        
    def trueRecv(self,socket):
        rawSize = self.trueAll(socket, 4)
        if not rawSize:
            return None
        dataSize = struct.unpack('>I', rawSize)[0]
        # Read the message data
        return self.trueAll(socket, dataSize)
    
    def trueAll(self,socket, length):
        # Helper function to recv n bytes or return None if EOF is hit
        data = b''
        while len(data) < length:
            packet = socket.recv(length - len(data))
            if not packet:
                return None
            data += packet
            return data
        
    """
    End True Data Handling Methods
    """

#             
#     def sendDir(self,cs):
#         sendArr = self.directory()
#         for x in sendArr:
#             cs.send(x.encode())
#         cs.send('finish'.encode())
            
    #Server doesn't currently use a command handler, but one will need to be implemented later.
    def commHandler(self,cs,com):
        if(com=='ls'):
            self.sendDir(cs)
            
        if(com == 'File'):
#             cs.send('Enter the file you want: '.encode('ascii'))
#             fileStrData = cs.recv(1024)
#             fileStr = str(fileStrData.decode('ascii'))
            print('Handling File Request')
            self.fileHandler(cs);
            
    def directory(self):
        arr = os.listdir("C:\\SoundFiles\\Server\\");
        return arr
    
    def dirChange(self):
        strDir = ""
        for x in self.__dir:
            strDir = strDir + x
            strDir += "\n"
        return strDir
    
#     def blockRecv(self, cs):
#         data = cs.socket.recv(1024)
#         if(not data):
#             while (not data):
#                 data = cs.socket.recv(1024)
                
    
#     def fileHandler(self,cs):
#         cs.send('Enter the file you want: '.encode('ascii'))
#         print('getting name....')
#         fileStrData = cs.recv(1024)
#         print('Name got...')
#         #print(str(fileStrData.decode('ascii')))
#         fileStr = str(fileStrData.decode())
#         print(fileStr)
#         #print(fileStr)
#         try:
#             print('getting file stats')
#             #stats = os.stat(fileStr);
#             stats = os.path.getsize("C:\\SoundFiles\\Server\\" + fileStr + '.mp3') #stat("C:\\SoundFiles\\Server\\lz.mp3")
#             fileSize = stats #stats.st_stat
#             attempts = fileSize/1024
#             final = fileSize%1024
#             print('File Size: ', fileSize)
#             print('Attempts: ', attempts)
#             print('Final Size: ', final)
#             print('Sending FileSize...')
#             cs.send(str(fileSize).encode('ascii'))
#             file = open("C:\\SoundFiles\\Server\\"+fileStr + '.mp3','rb')
#             print('Found file, sending now')
#             #cont = file.read(1024);
#             bytesC = 0#1024
#             i = 1
#             while(i<attempts):
#                 cont = file.read(1024)
#                 cs.send(cont)
#                 i+=1
#                 bytesC += 1024
#                 print(bytesC)
#                 print(i, ' :I | A: ', attempts)
#             cont = file.read(47)#final);
#             cs.send(cont)
#             bytesC+=47
#             print('File Sent Bytes: ',bytesC)
#             print(fileSize, "  ", final)
#         except:
#             print("Sending file issue")
#             size = str(-1)
#             #size = (-1).to_bytes()
#             cs.send(size.encode('ascii'))
            
    def fileHandler2(self, name, cs):
#         try:
#             #name = name[1:len(name)-1]
#             print(name)
#             print('getting file')
#             stats = os.path.getsize("C:\\SoundFiles\\Server\\" + name) #stat("C:\\SoundFiles\\Server\\lz.mp3")
#             print('found file')
#             file = open("C:\\SoundFiles\\Server\\"+name,'rb')
#             fileData = file.read()
#             file.close()
#             print('sending file')
#             cs.trueSend(fileData)
#             
#         except:
#             print('error with file transfer')
            #name = name[1:len(name)-1]
        print(name)
        print('getting file')
        stats = os.path.getsize("C:\\SoundFiles\\Server\\" + name) #stat("C:\\SoundFiles\\Server\\lz.mp3")
        print('found file')
        file = open("C:\\SoundFiles\\Server\\"+name,'rb')
        fileData = file.read(stats)
#         print(len(fileData))
        file.close()
        print('sending file')
        self.trueSend(cs,fileData)

            
        
#     def clientHandler(self, cs, addr):
#         """Threaded Clients"""
#         #Default packet size
#         print('Handling Client')
#         size = 1024
#         while(True):
#             data = cs.recv(size)
#             if(data):
#                 print(str(data.decode('ascii')))
#                 response = str(data.decode('ascii'))
#                 self.commHandler(cs, response)
# #         while(1):
# #             try:
# #                 data = cs.recv(size)
# #                 if data:
# #                     print(str(data.decode('ascii')))
# #                     response = str(data.decode('ascii'))
# #                     self.commHandler(cs, response)
# #                 #print(response)
# #                 #cs.send(response.encode('ascii'))
# #                 else:
# #                     raise ('No message');
# #             except:
# #                 cs.close();
# #                 return False;

    def clientHandler2(self,cs,addr):
        "Threaded clients"
        print("Connection established...")
        commData = self.trueRecv(cs)
        while not commData:
            commData = self.trueRecv(cs)
        comm = commData.decode()
        if(comm =="ls"):
            self.trueSend(cs, self.__strDir.encode())
        else:
            print('handling file 1')
            self.fileHandler2(comm, cs)      
        cs.close()
            
        
        
            
        
 
 
        
if __name__ == "__main__":
    #stats = os.path.getsize("C:\\SoundFiles\\Server\\lz.mp3")
    #THIS IS THE MAIN DIR FOR FILES
    os.chdir("C:\\SoundFiles\\Server\\")
    ServerK = ServerSide("127.0.0.1",1445);
    ServerK.listen()
    #ServerK.SS.listen()
#     while(True):
#         CS, addr = ServerK.SS.accept()
#         clientT = threading.Thread(target = ServerK.clientHandler, args = (CS));
#         clientT.start()
        
        
#         thread = Thread(target = threaded_function, args = (10, ))
#         thread.start()
#         thread.join()
#         print "thread finished...exiting"
#         
        