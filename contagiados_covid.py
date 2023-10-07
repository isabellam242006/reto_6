#El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. 
#Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, 
#si el número de contagiados actuales es C.

def calcular_total_contagiados(D,C) -> int:
    total_contagiados =  C * (2**D)
    return total_contagiados

if __name__ == "__main__":
    C = int(input("ingrese el número de contagiados actuales: "))
    D = int(input("ingrese el número de días: "))

total_contagiados = calcular_total_contagiados(D,C)
print("Hasta el día " + str(D) + " hay " + str(total_contagiados) + " contagiados en total")




