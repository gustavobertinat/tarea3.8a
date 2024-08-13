def suma_y_promedio(lista):
    """
    Calcula la suma y el promedio de una lista de números.
    
    Parámetros:
    - lista: La lista de números a procesar.
    
    Retorna:
    - Una tupla con la suma y el promedio de los números en la lista.
    """
    if not lista:  # Verifica si la lista está vacía
        return (0, 0)  # Si la lista está vacía, la suma y el promedio son 0
    
    suma = sum(lista)  # Calcula la suma de los números en la lista
    promedio = suma / len(lista)  # Calcula el promedio
    return suma, promedio  # Devuelve la suma y el promedio como una tupla
def main():
    """
    Función principal que demuestra el uso de la función suma_y_promedio.
    """
    numeros = [10, 20, 30, 40, 50]
    
    suma, promedio = suma_y_promedio(numeros)
    
    print(f"Suma: {suma}")
    print(f"Promedio: {promedio:.2f}")

if __name__ == "__main__":
    main()
