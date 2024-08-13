import math

def es_primo(n):
    """
    Verifica si un número es primo.
    
    Parámetros:
    - n: El número a verificar.
    
    Retorna:
    - True si n es primo, False en caso contrario.
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True
def contar_primos(lista):
    """
    Cuenta la cantidad de números primos en una lista.
    
    Parámetros:
    - lista: La lista de números a evaluar.
    
    Retorna:
    - La cantidad de números primos en la lista.
    """
    return sum(1 for numero in lista if es_primo(numero))
def main():
    """
    Función principal que integra la verificación de números primos y el conteo en una lista.
    """
    # Lista de números para verificar
    numeros = [2, 3, 4, 5, 10, 13, 17, 18, 19, 23, 24, 29]
    
    print("Lista de números:", numeros)
    
    # Contar números primos en la lista
    cantidad_primos = contar_primos(numeros)
    
    print(f"Cantidad de números primos en la lista: {cantidad_primos}")

if __name__ == "__main__":
    main()
