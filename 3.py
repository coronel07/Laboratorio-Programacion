def contar_palabras(texto):
    contador_palabras = 0

    for caracter in texto:
        if caracter == ' ':
            contador_palabras += 1
    contador_palabras += 1
    return contador_palabras

txt = "hola como estas"
resultado = contar_palabras(txt)
print("Número de palabras:", resultado)

