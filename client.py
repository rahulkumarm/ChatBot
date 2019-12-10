import socket
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
 
def Main():
        bot = ChatBot('Bot')
        bot.set_trainer(ListTrainer)
        for files in os.listdir('C:/Users/RAHUL/Desktop/chatbot/chatterbot-corpus-master/chatterbot-corpus-master/chatterbot_corpus/data/english/'):
                data = open('C:/Users/RAHUL/Desktop/chatbot/chatterbot-corpus-master/chatterbot-corpus-master/chatterbot_corpus/data/english/'+ files , 'r').readlines()
                bot.train(data)
        host = '127.0.0.1'
        port = 5000
         
        mySocket = socket.socket()
        mySocket.connect((host,port))
         
        message = 'hey bro'
        print('Server_Bot: ',message)
         
        while message != 'q':
                mySocket.send(str(message).encode())
                data = mySocket.recv(1024).decode()
                 
                print ('Server_Bot: ' + data)
                 
                reply = bot.get_response(message)
                message = reply

                
                 
        mySocket.close()
 
if __name__ == '__main__':
    Main()
