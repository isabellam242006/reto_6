import math

def calcular_volumen_esfera( r1: float) -> float:
    volumen_esfera = 4/3 * math.pi * (r1**3)
    return volumen_esfera

def calcular_area_esfera(r1: float) -> float:
    area_esfera = 4 * math.pi * (r1**2)
    return area_esfera

if __name__ == "__main__":
    r1 = float(input("Ingrese un radio para la esfera: "))
    v_esfera = calcular_volumen_esfera(r1)
    a_esfera = calcular_area_esfera(r1)
    print("el volumen de la esfera es " + str(v_esfera))
    print("el area superficial de la esfera es " + str(a_esfera))

def calcular_volumen_cono(r2: float, h:float) -> float:
    volumen_cono = 1/3 * math.pi * h * (r2**2)
    return volumen_cono

def calcular_area_cono(r2: float, h:float) -> float:
    area_cono = (math.pi*r2*h)+(math.pi*r2**2)
    return area_cono


if __name__ == "__main__":
    r2 = float(input("Ingrese un radio para el cono: "))
    h = float(input("Ingrese una altura para el cono: "))
    v_cono = calcular_volumen_cono(r2,h)
    a_cono= calcular_area_cono(r2,h)
    print("el volumen del cono es " + str(v_cono))
    print("el área superficial del cono es " + str(a_cono))

volumen_total = v_cono + v_esfera
print("El volumen total es " + str(volumen_total))
area_superficial_total = a_cono + a_esfera
print("El área superficial total es " + str(area_superficial_total))



