#Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando
#6 kilos, 7 kilos y 1 kilo respectivamente.

def  calcular_total_carne(M,N,K) -> int:
    total_carne = (6*N)+ (7*M) + (K)
    return(total_carne)

if __name__ == "__main__":
    N= int(input("ingrese el número de gallinas: "))
    M= int(input("ingrese el número de gallos: "))
    K= int(input("ingrese el número de pollitos: "))

total = calcular_total_carne(M,N,K)
print("El total de carne es " + str(total) + " kilos")


