#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Servidor TCP que, tras entablar una conexión, recibe comandos de los
# clientes y los ejecuta sobre el sistema. Indicar errores
#

import socket
import os
import sys
from thread import *
from threading import *
import argparse
import errno
from subprocess import Popen, PIPE
import readline

RESET = '\033[0m'
BLUE = '\033[94m'
YELLOW = '\033[93m'
RED = '\033[91m'
WHITE = '\033[97m'

class Server():
    def __init__(self, ip, port, password):

        self.busy = False
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            serversocket.bind((ip, port))

        except socket.error as msg:
            print 'Bind failed. Error Code: %s Message: %s ' %(str(msg[0]), str(msg[1]))
            sys.exit()

        print "Server running on port "+str(port)

        try:
            #Maximo max conexiones concurrentes
            serversocket.listen(1)

            while True:
                if self.busy:
                    conn, addr = serversocket.accept()
                    conn.send("!{Server_Full}")
                    continue
                else:
                    conn, addr = serversocket.accept()
                    print 'Connection with %s : %s ' %(addr[0], str(addr[1]))
                    self.busy = True
                    start_new_thread(self.clientthread,(conn,password,))

        except:
            print "\nClosing server..."

            try:
                conn.send("!{Server_OFF}")
                conn.close()
            except:
                pass
        finally:
            serversocket.close()

#
# HILO CLIENTE
#

    def clientthread(self,conn,password):
        data = conn.recv(1024)
        if data != password:
            conn.send("!{Wrong_Password}")
            exit()
        else:
            try:
                string = "Welcome to the server!. Type /exit to leave.\n"
                conn.send(string)

                # username@hostname:

                subprocess = Popen("whoami", shell=True, stdout=PIPE)
                tupla = subprocess.communicate(input=None)
                name = tupla[0].rstrip()
                subprocess = Popen("hostname", shell=True, stdout=PIPE)
                tupla = subprocess.communicate(input=None)
                hostname = tupla[0].rstrip()

                user = RED+name+YELLOW+"@"+BLUE+hostname+RESET+": "
                conn.sendall(user)

                # command execution

                while True:
                    data = conn.recv(1024)
                    if not data or data == "/exit":
                        exit()
                    # user can try /stderr command without using a command before
                    elif data == "/stderr":
                        try:
                            conn.sendall(last[:-1])
                        except:
                            conn.sendall("There isn't anything in stderr.")
                    else:
                        subprocess = Popen(data, shell=True, stdout=PIPE, stderr=PIPE)
                        stdout, stderr = subprocess.communicate(input=None)
                        if stderr:
                            last=stderr
                            conn.sendall(stderr[:-1])
                        else:
                            conn.sendall(stdout[:-1])

            except socket.error:
                print "Client has disconnected!"

            finally:
                self.busy = False
                conn.close()

class Client():

    def __init__(self, ip, port, password):

        self.exit = False
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            client.connect((ip, port))
        except socket.error as serr:
            if serr.errno == errno.ECONNREFUSED:
                print "The server isn't up!"
                exit()
            else:
                raise

        client.send(password)
        message = client.recv(1024)

        if message == "!{Wrong_Password}":
            print "Wrong password! Disconnecting..."
            client.close()
            exit()
        elif message == "!{Server_Full}":
            print "Server is busy. Try again later."
            client.close()
            exit()

        # message from server + username@hostname:
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print message

            self.username = client.recv(1024)

            try:
                recthread = Thread(target=self.receive, args=(client,))
                sendthread = Thread(target=self.send, args=(client,))
                recthread.start()
                sendthread.start()
                sendthread.join()
                recthread.join()
            except:
                pass
            finally:
                client.close()

#
# Receive messages
#

    def receive(self, client):
        while True:
            message = client.recv(1024)
            if not message:
                self.exit=True
                exit()
            elif message == "!{Server_OFF}":
                print "Server closed!"
                self.exit=True
                exit()
            # Move cursor to right in each line
            for line in message.splitlines():
                print '\033[C'+line
            if self.exit:
                break

#
# Send messages
#

    def send(self, client):
        while True:
            message = raw_input()
            ## Comandos con mensajes en claro, sin colores
            if message == "" and self.exit == False:
                continue
            elif message == "/exit":
                client.send(message)
                print "\033[A"+self.username+message
                self.exit = True
                break
            elif message == "/help":
                print "\033[A"+self.username+message
                self.help()
                continue
            elif message == "/clear" or message == "clear":
                os.system('cls' if os.name == 'nt' else 'clear')
                continue
            elif self.exit:
                break
            client.send(message)
            print "\033[A"+self.username+message

    def help(self):
        print YELLOW+"/clear :"+WHITE+" clear screen"
        print YELLOW+"/stderr :"+WHITE+" shows last error message gotten."
        print YELLOW+"/exit :"+WHITE+" leave server"+RESET

parser = argparse.ArgumentParser(description='Remote TCP server command execution.')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-s','--server', help='Run program as server', action="store_true")
group.add_argument('-c','--client', help='Run program as client', action="store_true")
parser.add_argument('-x','--password', help='Password.', type=str, required=True)
parser.add_argument('-i','--ip', help='Specify IP address to connect to. Localhost by default', type=str, default="0.0.0.0")
parser.add_argument('-p','--port', help='Choose port. 8080 by default', type=int, default=8080)
args = parser.parse_args()

if args.port > 65535 or args.port < 1024:
    print "Invalid port. Choose one between 1024 and 65535 \n"
    exit()

if args.client:
    client = Client(args.ip, args.port, args.password)
elif args.server:
    server = Server(args.ip, args.port, args.password)
