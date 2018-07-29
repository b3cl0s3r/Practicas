#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#  Script que recupera todos los ficheros y subdirectorios de un directorio especificado por parámetro en la línea de comandos
#  de forma recursiva

import argparse
import os
import random
import psycopg2
import getpass


# Está hecho así para que se de el caso de que NO se cree ningún fichero

def createfiles(m="", n="", o=""):
        nfiles = random.randint(1,4)
        for i in range(0,nfiles):
            if i == 0:
                continue
            filename="file"+m+n+o+str(i)
            f = open(filename,"w")
            f.close()


def recursivesearch(cwd):

    os.chdir(cwd)
    entries = os.listdir(".")
    dirs = list()
    files = list()

    for i in entries:
        if os.path.isdir(i):
            dirs.append(i)
        else:
            files.append(i)

    if not dirs and not files:
        print "No files here"
        os.chdir("..")
        return

    elif not dirs and files:
        print files
        os.chdir("..")
        return

    else:
        for i in dirs:
            print "Inside dir: "+i
            recursivesearch(i)

        print files
        os.chdir("..")



parser = argparse.ArgumentParser(description='Recover all files and directories recursively and store them in a database')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-d','--dir', help='Initial directory to start the search.', type=str, default=None)
group.add_argument('-g','--gen', help='Create a random directory tree to test this program.', type=str, default=None)
args = parser.parse_args()

if args.dir != None:

    try:
        os.chdir(args.dir)

    except OSError as msg:
        if msg[0] == 2:
            print 'Error. %s does not exist' %(args.dir)
        else:
            print 'Error Code: %s. Message: %s' %(str(msg[0]), msg[1])
        exit()

    recursivesearch(".")

elif args.gen != None:

    try:
        os.makedirs(args.gen)

    except OSError as msg:
        if msg[0] == 17:
            print 'Error. %s already exists.'%(args.gen)
        elif msg[0] == 13:
            print "Error. Permission denied."
        else:
            print 'Error Code: %s. Message: %s' %(str(msg[0]), msg[1])
        exit()

    os.chdir(args.gen)

## Crear arbol de directorios y archivos de forma aleatoria. 3 Niveles y no está automatizado
## para soportar N niveles.

    for i in range(1,random.randint(3,6)):
        os.makedirs(str(i))
        os.chdir(str(i))
        createfiles(str(i))

        for j in range(1,random.randint(2,5)):
            os.makedirs(str(i)+str(j))
            os.chdir(str(i)+str(j))
            createfiles(str(i), str(j))

            for k in range(0, random.randint(1,4)):
                if k == 0:
                    continue
                os.makedirs(str(i)+str(j)+str(k))
                os.chdir(str(i)+str(j)+str(k))
                createfiles(str(i), str(j), str(k))
                os.chdir("..")

            os.chdir("..")

        os.chdir("..")

    createfiles()
