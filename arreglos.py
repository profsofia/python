numerosEnPalabras ={
    "0": "cero",
    "1": "uno",
    "2": "dos",
    "3": "tres",
    "4": "cuatro",
    "5": "cinco",
    "6": "seis",
    "7": "siete",
    "8": "ocho",
    "9": "nueve"
}

texto = input("ingrese un número, para saber como se escribe ")
#para que ponga los números de dos o mas cifras y no sale error
textoFinalEnUnaSolaLinea=''
for letra in texto:
    textoFinalEnUnaSolaLinea += numerosEnPalabras[letra] + ' '

print(textoFinalEnUnaSolaLinea)
print("chau")