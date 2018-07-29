#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Programa en Python que se conecta por ssh a una o varias
# máquinas y comprueba el estado de un servidor Apache.
# Si el servidor está detenido, lo arranca y si el servidor
# se encuentra en ejecución, lo reinicia
#
# Usage:
# python ej1.py -i <ip> -u <user> -x <pass> [-p <port != 22>]
# python ej1.py -f file

# file format:
# 192.168.1.3:22:user:user123
# 192.168.1.44:2022:root:rootpass
# ...

import argparse
import paramiko
import sys


def sshconnect(ip, port, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username=username, password=password)
    return client

def serverapachecheck(client):

    stdin, stdout, stderr = client.exec_command('service apache2 status')
    msg=stdout.readlines()

    try:
        if "Apache2 is running" in msg[0]:
            print "Apache2 is running."
            stdin, stdout, stderr = client.exec_command('service apache2 restart')
            for line in stdout.readlines():
                print line.rstrip()

        elif "Apache2 is NOT running" in msg[0]:
            print "Apache2 is NOT running"
            stdin, stdout, stderr = client.exec_command('service apache2 start')
            for line in stdout.readlines():
                print line.rstrip()
    except:
        print "Error: ",
        for line in stderr.readlines():
            print line,


parser = argparse.ArgumentParser(description='Remote HTTP server checker.')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-i','--ip', help='Specify IP address to connect to.', type=str, default=None)
parser.add_argument('-p','--port', help='Choose port. 22 by default', type=int, default=22)
parser.add_argument('-u','--username', help='Remote username to login.', type=str, default=None)
parser.add_argument('-x','--password', help='Password.', type=str, default=None)
group.add_argument('-f','--file', help='Provide a file with IP:port:username:password format and test in N hosts. ', type=str)
args = parser.parse_args()

if args.ip is not None and (args.password is None or args.username is None):
    parser.error('--ip and --password must be given together.')
elif args.port < 1 or args.port > 65535:
    parser.error('--port must be between 1 and 65535.')


if args.ip:
    try:
        client = sshconnect(args.ip, args.port, args.username, args.password)
    except paramiko.ssh_exception.AuthenticationException:
        sys.stderr.write("Authentication failed\n")
        exit()
    except paramiko.ssh_exception.NoValidConnectionsError:
        sys.stderr.write("Unable to connect to port "+str(args.port)+" on "+args.ip+"\n")
        exit()
    serverapachecheck(client)
    client.close()

elif args.file:
    try:
        data = file(args.file)

        for line in data:
            info = line.rstrip().split(':')

            ip = info[0]
            port = info[1]
            username = info[2]
            password = info[3]

            print "\nChecking "+ip+":"+port+"..."

            try:
                client = sshconnect(ip, int(port), username, password)
                serverapachecheck(client)
            except paramiko.ssh_exception.AuthenticationException:
                sys.stderr.write("Authentication failed\n")
            except paramiko.ssh_exception.NoValidConnectionsError:
                sys.stderr.write("Unable to connect to port "+port+" on "+ip+"\n")

            client.close()


    except IndexError:
        sys.stderr.write("Wrong file format. Must be: <ip>:<port>:<user>:<pass>\n")
        exit()
    except IOError:
        sys.stderr.write("Error: file "+args.file+" doesn't exist.\n")
        exit()
