def calcular_vueltas(P, M, H, B) -> int:
    vueltas = B - ((300 * P) + (3300 * M) + (350 * H))
    return vueltas

if __name__ == "__main__":
    P = int(input("ingrese el número de panes: "))
    M = int(input("ingrese el número de bolsas de leche: "))
    H = int(input("ingrese el número de huevos: "))
    B = int(input("ingrese el valor del billete en pesos: "))

total_vueltas = calcular_vueltas(P, M, H, B)

if total_vueltas < 0:
    print("El billete no alcanza para comprar todo eso")
else:
    print("Las vueltas son " + str(total_vueltas) + " pesos")



   
