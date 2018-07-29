#
# Buscar en un fichero coincidencias con X palabras
# Si no se especifica, busca por defecto casa, hogar, trabajo y perro en el fichero
#
# Nota: de esta forma funciona al igual que un CTRL+F: busca en el fichero X coincidencias, tal que si hay una palabra como
# asaaacasascass se cuenta como verdadera si se busca la palabra "casa" porque está contenida en el string.
#
# Para buscar "casa" a secas, se puede añadir que word = " "+word+" ", pero todas aquellas que tengan signo de puntuación serán ignoradas
# Así que, en caso de hacerse de esta forma, habría que hacer varias busquedas que sean " "+word+",", " "+word+".", " "+word+":" .....
# y sumarse todos los resultados


import argparse

parser = argparse.ArgumentParser(description='Given some words, this program finds coincidences in a given text file.')
parser.add_argument('-f','--file', help='File to use.', type=str, default=None, required=True)
parser.add_argument('-w','--words', help='Words to find.', type=str, default=None, nargs='*')
parser.set_defaults(words = ['casa','hogar','trabajo','perro'])
args = parser.parse_args()

try:

    for word in args.words:

        data = file(args.file)
        count=0
        nlinea=1
        lineas=[]
        # word = " "+word+" "

        for line in data:
            if word in line:
                count+=line.count(word)
                lineas.append(nlinea)
            nlinea+=1


        print "\nPalabra: "+word
        print "Ocurrencias: "+str(count)
        print "Lineas: ",
        for i in lineas:
            print i,
        print

except:
    print "Error: el fichero especificado no existe."
