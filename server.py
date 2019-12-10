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
    host = "127.0.0.1"
    port = 5000
     
    mySocket = socket.socket()
    mySocket.bind((host,port))
     
    mySocket.listen(1)
    conn, addr = mySocket.accept()
    print ("Connection from: " + str(addr))
    while True:
            data = conn.recv(1024).decode()
            if not data:
                    break
            print ("Client_Bot: " + str(data))
             
            reply = bot.get_response(data) 
            data = reply
            
            conn.send(str(data).encode())
             
    conn.close()
     
if __name__ == '__main__':
    Main()
