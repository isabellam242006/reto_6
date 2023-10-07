#Haga un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto del i por n meses

def calcular_valor_prestamo(C,i,n) -> float:
    valor_prestamo = C * ((1 + i/(12/n))**(12/n * n/12))
    return valor_prestamo

if __name__ == "__main__":
    C = float(input("Ingrese el valor del préstamo inicial: "))
    i = float(input("Ingrese el valor de la tasa de interés: "))
    n = float(input("Ingrese la cantidad de meses: "))

valor_prestamo = calcular_valor_prestamo(C,i,n)
print(valor_prestamo)
