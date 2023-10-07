import operaciones

if __name__ == "__main__":
    a = int(input("Ingrese número: "))
    b = int(input("Ingrese número: "))
    c = int(input("Ingrese número: "))
    d = int(input("Ingrese número: "))
    e = int(input("Ingrese número: "))

    mediana = operaciones.calcular_mediana(a, b, c, d, e)
    print(f"La mediana es: {mediana}")
    p_multiplicativo = operaciones.calcular_promedio_multiplicativo(a,b,c,d,e)
    print(f"El promedio multiplicativo es: {p_multiplicativo}")
    orden_ascendente = operaciones.calcular_orden_ascendente(a,b,c,d,e)
    print(f"El orden ascendente es: {orden_ascendente}")
    orden_descendente = operaciones.calcular_orden_descendente(a,b,c,d,e)
    print(f"El orden descendente es: {orden_descendente}")
    mayor = operaciones.calcular_mayor_número(a,b,c,d,e)
    menor = operaciones.calcular_menor_número(a,b,c,d,e)
    mayor_potencia_menor = mayor ** menor
    print(f"El resultado de elevar el mayor número al menor número es: {mayor_potencia_menor}")
    raiz_cubica = menor ** 1/3
    print(f"La raíz cúbica del menor número es {raiz_cubica}")


    
