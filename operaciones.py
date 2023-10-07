#Promedio

def calcular_promedio(a,b,c,d,e) ->float:
    promedio = (a + b + c + d + e)/5
    return promedio


#Mediana

def calcular_mediana(a, b, c, d, e) -> float:
    if a <= b and a <= c and a >= d and a >= e:
        mediana = a
    elif a >= d and a >= e and a <= c and a <= b:
        mediana = a
    elif a <= b and a <= d and a >= c and a >= e:
        mediana = a
    elif a <= c and a <= e and a >= d and a >= b:
        mediana = a
    elif b <= c and b <= d and b >= a and b >= e:
        mediana = b
    elif b >= a and b >= e and b <= c and b <= d:
        mediana = b
    elif b <= c and b <= a and b >= e and b >= d:
        mediana = b
    elif b <= e and b <= d and b >= c and b >= a:
        mediana = b
    elif c <= d and c <= e and c >= a and c >= b:
        mediana = c
    elif c >= a and c >= b and c <= d and c <= e:
        mediana = c
    elif c >= a and c >= d and c <= b and c <= e:
        mediana = c
    elif c >= b and c >= e and c <= a and c <= d:
        mediana = c
    elif d >= a and d >= b and d <= c and d <= e:
        mediana = d
    elif d <= c and d <= e and d >= a and d >= b:
        mediana = d
    elif d <= c and d <= a and d >= e and d >= b:
        mediana = d
    elif d <= e and d <= b and d >= c and d >= a:
        mediana = d
    elif e >= a and e >= b and e <= c and e <= d:
        mediana = e
    elif e <= c and e <= d and e >= a and e >= b:
        mediana = e
    elif e <= c and e <= a and e >= d and e >= b:
        mediana = e
    elif e <= d and e <= b and e >= c and e >= a:
        mediana = e
    return mediana

#promedio multiplicativo

def calcular_promedio_multiplicativo(a,b,c,d,e) -> float:
    promedio_multiplicativo = (a*b*c*d*e)**1/5
    return promedio_multiplicativo

#Calcular orden ascendente
def calcular_orden_ascendente(a: float, b: float, c: float, d: float, e: float) -> tuple:
    primer_orden = a
    segundo_orden = b
    tercer_orden = c
    cuarto_orden = d
    quinto_orden = e

    if primer_orden < segundo_orden:
        orden = segundo_orden
        segundo_orden = primer_orden
        primer_orden = orden

    if primer_orden < tercer_orden:
        orden = tercer_orden
        tercer_orden = primer_orden
        primer_orden = orden

    if primer_orden < cuarto_orden:
        orden = cuarto_orden
        cuarto_orden = primer_orden
        primer_orden = orden

    if primer_orden < quinto_orden:
        orden = quinto_orden
        quinto_orden = primer_orden
        primer_orden = orden

    if segundo_orden < tercer_orden:
        orden = tercer_orden
        tercer_orden = segundo_orden
        segundo_orden = orden

    if segundo_orden < cuarto_orden:
        orden = cuarto_orden
        cuarto_orden = segundo_orden
        segundo_orden = orden

    if segundo_orden < quinto_orden:
        orden = quinto_orden
        quinto_orden = segundo_orden
        segundo_orden = orden

    if tercer_orden < cuarto_orden:
        orden = cuarto_orden
        cuarto_orden = tercer_orden
        tercer_orden = orden

    if tercer_orden < quinto_orden:
        orden = quinto_orden
        quinto_orden = tercer_orden
        tercer_orden = orden

    if cuarto_orden < quinto_orden:
        orden = quinto_orden
        quinto_orden = cuarto_orden
        cuarto_orden = orden

    return quinto_orden,cuarto_orden,tercer_orden,segundo_orden,primer_orden

#Calcular orden descendente
def calcular_orden_descendente(a: float, b: float, c: float, d: float, e: float) -> tuple:
    primer_orden = a
    segundo_orden = b
    tercer_orden = c
    cuarto_orden = d
    quinto_orden = e

    if primer_orden < segundo_orden:
        orden = segundo_orden
        segundo_orden = primer_orden
        primer_orden = orden

    if primer_orden < tercer_orden:
        orden = tercer_orden
        tercer_orden = primer_orden
        primer_orden = orden

    if primer_orden < cuarto_orden:
        orden = cuarto_orden
        cuarto_orden = primer_orden
        primer_orden = orden

    if primer_orden < quinto_orden:
        orden = quinto_orden
        quinto_orden = primer_orden
        primer_orden = orden

    if segundo_orden < tercer_orden:
        orden = tercer_orden
        tercer_orden = segundo_orden
        segundo_orden = orden

    if segundo_orden < cuarto_orden:
        orden = cuarto_orden
        cuarto_orden = segundo_orden
        segundo_orden = orden

    if segundo_orden < quinto_orden:
        orden = quinto_orden
        quinto_orden = segundo_orden
        segundo_orden = orden

    if tercer_orden < cuarto_orden:
        orden = cuarto_orden
        cuarto_orden = tercer_orden
        tercer_orden = orden

    if tercer_orden < quinto_orden:
        orden = quinto_orden
        quinto_orden = tercer_orden
        tercer_orden = orden

    if cuarto_orden < quinto_orden:
        orden = quinto_orden
        quinto_orden = cuarto_orden
        cuarto_orden = orden

    return primer_orden, segundo_orden, tercer_orden, cuarto_orden, quinto_orden

if __name__ == "__main__":
    a = float(input("Ingrese primer número: "))
    b = float(input("Ingrese segundo número: "))
    c = float(input("Ingrese tercer número: "))
    d = float(input("Ingrese cuarto número: "))
    e = float(input("Ingrese quinto número: "))

    orden_ascendente = calcular_orden_ascendente(a, b, c, d, e)
    orden_descendente = calcular_orden_descendente(a, b, c, d, e)

    print(f"Valores en orden ascendente: {orden_ascendente}")
    print(f"Valores en orden descendente: {orden_descendente}")

#La potencia del mayor número elevado al menor número

def calcular_mayor_número(a, b, c, d, e):
    if a >= b >= c >= d >= e:
        mayor = a
    elif b >= c >= d >= e >= a:
        mayor = b
    elif c >= d >= e >= a >= b:
        mayor = c
    elif d >= e >= a >= b >= c:
        mayor = d
    elif e >= a >= b >= c >= d:
        mayor = e
    elif b >= mayor:
        mayor = b
    elif c >= mayor:
        mayor = c
    elif d >= mayor:
        mayor = d
    elif e >= mayor:
        mayor = e
    return mayor

def calcular_menor_número(a, b, c, d, e):
    if a <= b <= c <= d <= e:
        menor = a
    elif b <= c <= d <= e <= a:
        menor = b
    elif c <= d <= e <= a <= b:
        menor = c
    elif d <= e <= a <= b <= c:
        menor = d
    elif e <= a <= b <= c <= d:
        menor = e
    return menor


#Raiz cúbica
raiz_cubica = calcular_menor_número ** 1/3


    


    


        
    
