def mayuscula(cadena):
    # Divide la cadena en palabras
    palabras = cadena.split()
    
    # pone el primer carácter de cada palabra mayuscula y mantiene el resto igual
    palabras_capitalizadas = [palabra.capitalize() for palabra in palabras]
    
    # Une las palabras en una nueva cadena
    resultado_final = ' '.join(palabras_capitalizadas)
    
    return resultado_final

# Solicita al usuario que ingrese una cadena
cadena_usuario = input("Ingresa una cadena de texto: ")
resultado = mayuscula(cadena_usuario)
print("Cadena con palabras en mayúsculas:", resultado)


