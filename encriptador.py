#unArchivoPrueba = open('prueba.txt', 'a')
#unArchivoPrueba.write('probando el archivo!')
#unArchivoPrueba.close()
##prueba exitosa, se creó como debía!!!

#para que lo lea en consola
unArchivoPrueba = open('prueba.txt', 'r')
print(unArchivoPrueba.read())



#tex = input('esto es un encriptador, ingrese el texto o los números: ')


def encriptar(texto):
    textoFinal = ''
    for letra in texto:
        ascii = ord(letra)
        ascii +=1
        textoFinal += chr(ascii) #doc de las funciones abajo.
    #print(textoFinal)
    return textoFinal


#encriptar(tex)

#texEncriptado = input(
    'esto es un desencriptador, ingrese el texto o los números: '#)


def desencriptar(texto):
    textoFinal = ''
    
    for letra in texto:
        ascii = ord(letra)
        ascii -=1
        textoFinal += chr(ascii) #doc de las funciones abajo.
        
    #print(textoFinal)
    return textoFinal

#desencriptar(texEncriptado)

#creamos una función que sirva para leer un archivo encriptado

def encriptarArchivo(rutaArchivo):
    archivo = open(rutaArchivo, 'r')
    #leemos y lo almacenamos en una variable
    texto= archivo.read()
    archivo.close()
    ##encriptamos el archivo
    #textoEncriptado:str
    textoEncriptado= encriptar(texto)

    #lo abre y escribimos
    archivo = open(rutaArchivo, 'w')
    archivo.write(textoEncriptado)
    archivo.close()


#llamamos a la función

#encriptarArchivo()


#función de desencriptar

def desencriptarArchivo(rutaArchivo):
    archivo = open(rutaArchivo, 'r')
    #leemos y lo almacenamos en una variable
    archivoEncriptado= archivo.read()
    archivo.close()
    ##encriptamos el archivo
    #textoEncriptado:str
    textoDesencriptado= desencriptar(archivoEncriptado)

    #lo abre y escribimos
    archivo = open(rutaArchivo, 'w')
    archivo.write(textoDesencriptado)
    archivo.close()


#desencriptarArchivo()


#le preguntamos por consola que archivo quiere encriptar o desencriptar

respuestaUsuario= input('Presione '+'E' +' para encriptar un archivo o '+'D' +' para desencriptar: ')
rutaArchivo = input('ingrese la ruta del archivo que desea encriptar/desencriptar: ')

if respuestaUsuario=='E':
    encriptarArchivo(rutaArchivo)
    print('Se encriptó exitosamente')
else:
    desencriptarArchivo(rutaArchivo)
    print('Se desencriptó correctamente, chau')



#funciones 
#ord("h")
#nos imprime el número que representa esa letra
#chr("64") # lo contrario de la función de arriba