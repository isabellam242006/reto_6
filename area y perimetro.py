import math

def calcular_area_rectangulo( a: float, b:float) -> float:
    area_rectangulo = a * b
    return area_rectangulo

def calcular_perimetro_rectangulo(a:float, b:float) -> float:
    perimetro_rectangulo = (2 * a) + (2 * b)
    return perimetro_rectangulo

if __name__ == "__main__":
    a = float(input("Ingrese el largo del rectángulo: "))
    b = float(input("Ingrese el ancho del rectángulo: "))
    p_rectangulo = calcular_perimetro_rectangulo(a,b)
    a_rectangulo = calcular_area_rectangulo(a,b)
    print("el perimetro del rectangulo es " + str(p_rectangulo))
    print("el área del rectángulo es " + str(a_rectangulo))

def calcular_area_circulos(r: float) -> float:
    area_circulos = 2*(math.pi * (r**2))
    return area_circulos

def calcular_perimetro_circulos(r:float) -> float:
    perimetro_circulos = 2*(2 * math.pi * r)
    return perimetro_circulos


if __name__ == "__main__":
    r = float(input("Ingrese un radio para los círculos: "))
    p_circulos= calcular_perimetro_circulos(r)
    a_circulos = calcular_area_circulos(r)
    print("el perimetro de los circulos es " + str(p_circulos))
    print("el área de los círculos es " + str(a_circulos))

perimetro_total = p_rectangulo + p_circulos
print("El perimetro total es " + str(perimetro_total))
area_total = a_rectangulo + a_circulos
print("El área total es " + str(area_total))

