# reto_6

1.Dado la figura de la imagen, desarrolle:

- Una función matemática para calcular el volumen y el área superficial.
- Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r1, r2 y h.
- Revise como utilizar el valor de pi usando import math y math.pi

*Para este punto primero importé la librería ```math```, luego definí la función para el volumen y el área superficial de ambas figuras por separado(esfera y cono) y al final del código sumé los resultados para que me diera el valor total de la figura. Para pi se utilizó la extensión ```math.pi```*
```
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
```
2. Dado la figura de la imagen, desarrolle:

- Una función matemática para calcular el área y el perimetro.
- Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r, a y b.
- Revise como utilizar el valor de pi usando import math y math.pi

*Similar al punto anterior definí las funciones de área y perímetro por separado de las figuras(en este caso dos círculos y un rectángulo) y luego sumé los resultados para que me diera el valor de la figura completa. También se utilizó la librería ```math``` y la extensión ```math.pi```*

```
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
```
3. Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.

  *En esta ocasión se creó una función que relacionara la cantidad de animales dados por computadora y sus respectivo peso en kilos*
```
def  calcular_total_carne(M,N,K) -> int:
    total_carne = (6*N)+ (7*M) + (K)
    return(total_carne)

if __name__ == "__main__":
    N= int(input("ingrese el número de gallinas: "))
    M= int(input("ingrese el número de gallos: "))
    K= int(input("ingrese el número de pollitos: "))

total = calcular_total_carne(M,N,K)
print("El total de carne es " + str(total) + " kilos")
```
4. Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.

*Para este punto se calculó el monto total que se gastó en cada alimento. Luego al billete que se dio, se le resta este valor. Si el valor del billete es menor, se devuelve un mensaje que dice que no es posible comprar lo solicitado*

```
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
```
5. Haga un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto del i por n meses.

*Para este punto se utilizó la fórmula de interés compuesto*
```
def calcular_valor_prestamo(C,i,n) -> float:
    valor_prestamo = C * ((1 +i)**n)
    return valor_prestamo

if __name__ == "__main__":
    C = float(input("Ingrese el valor del préstamo inicial: "))
    i = float(input("Ingrese el valor de la tasa de interés en decimales: "))
    n = float(input("Ingrese la cantidad de meses: "))

valor_prestamo = calcular_valor_prestamo(C,i,n)
print("El valor total del préstamo será de " + str(valor_prestamo))
```
6. El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.

*Para este punto se utilizó la fórmula de aumento exponencial*
```
def calcular_total_contagiados(D,C) -> int:
    total_contagiados =  C * (2**D)
    return total_contagiados

if __name__ == "__main__":
    C = int(input("ingrese el número de contagiados actuales: "))
    D = int(input("ingrese el número de días: "))

total_contagiados = calcular_total_contagiados(D,C)
print("Hasta el día " + str(D) + " hay " + str(total_contagiados) + " contagiados en total")
```
7.Escriba un programa que pida 5 números reales y calcule las siguientes operaciones usando una función para cada una:

- El promedio
- La mediana
- El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
- Ordenar los números de forma ascendente
- Ordenar los números de forma descendente
- La potencia del mayor número elevado al menor número
- La raíz cúbica del menor número

*Para este punto se definieron funciones independientes para cada ítem. Teniendo en cuenta que son 5 variables fue necesario analizar cada caso de forma que se tuvieran las distintas posibilidades de combinación*
```
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
```
8. Para el punto anterior incluir las funciones en un archivo independiente e importarlas para su uso.

*Para este punto se importaron las funciones con la palabra ```import``` y luego se definieron las variables para que se puedan ingresar por computador. Por último se imprimen los mensajes que dan los resultados. Para llamar las funciones es necesario usar la extensión ```operaciones.```*
```
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
```

9. Consultar qué es y cómo funciona pip en python.
    
"pip" es una herramienta en Python que se utiliza para instalar y gestionar paquetes de software (bibliotecas) desarrollados por la comunidad de Python. Estos paquetes pueden contener código adicional, módulos y funcionalidades que pueden ser utilizados en proyectos de Python. pip es una parte fundamental del ecosistema de Python porque facilita la instalación y gestión de bibliotecas de terceros.

A continuación se presenta una breve descripción de cómo pip funciona en Python:

**Instalación de pip**: En versiones recientes de Python (a partir de Python 3.4 en adelante), pip generalmente se instala automáticamente junto con Python. Si se está utilizando una versión anterior de Python o se necesita actualizar pip, se puede hacer manualmente.

**Búsqueda y listado de paquetes:** pip se puede utilizar para buscar paquetes disponibles en el Índice de Paquetes de Python (PyPI) o para listar los paquetes que ya están instalados en el entorno Python.

**Para buscar paquetes:** pip search nombre_del_paquete
**Para listar paquetes instalados:** pip list
**Instalación de paquetes:** pip permite la instalación de paquetes específicos desde PyPI u otras fuentes, como archivos de distribución o repositorios de control de versiones. Por ejemplo:

**Para instalar un paquete desde PyPI:** pip install nombre_del_paquete

**Para instalar un paquete desde un archivo .whl o .tar.gz:** pip install ruta_al_archivo

**Para instalar un paquete desde un repositorio de control de versiones:** pip install git+URL_del_repositorio

**Desinstalación de paquetes:** pip se puede utilizar para desinstalar paquetes que ya no sean necesarios con el comando pip uninstall nombre_del_paquete.

**Gestión de entornos virtuales:** pip es comúnmente utilizado junto con virtualenv o venv para crear entornos virtuales aislados para proyectos individuales. Los entornos virtuales permiten que diferentes proyectos utilicen diferentes versiones de paquetes sin interferir entre sí.

**Actualización de paquetes:** pip permite la actualización de paquetes a versiones más recientes si están disponibles. Por ejemplo: pip install --upgrade nombre_del_paquete.

**Requisitos del proyecto:** Se pueden definir los requisitos del proyecto en un archivo llamado requirements.txt y luego utilizar pip para instalar todos los paquetes especificados en ese archivo en una sola línea de comando. Esto es útil para compartir el proyecto con otros y garantizar que tengan las mismas dependencias.

**Para generar un archivo requirements.txt:** pip freeze > requirements.txt

**Para instalar paquetes desde un archivo requirements.txt:** pip install -r requirements.txt

10. Hacer un listado de módulos populares para python que se puedan instalar com pip y consultar cómo instalarlos.

**Numpy:**

Descripción: Biblioteca para cálculos numéricos y manipulación de matrices.

Instalación: pip install numpy

**Pandas:**

Descripción: Biblioteca para análisis y manipulación de datos en Python.

Instalación: pip install pandas

**Matplotlib:**

Descripción: Biblioteca para la creación de gráficos y visualización de datos.

Instalación: pip install matplotlib

**Requests:**

Descripción: Biblioteca para realizar solicitudes HTTP en Python.

Instalación: pip install requests

**Django:**

Descripción: Marco de desarrollo web de alto nivel para construir aplicaciones web.

Instalación: pip install Django

**Flask:**

Descripción: Marco de desarrollo web ligero y flexible para crear aplicaciones web.

Instalación: pip install Flask

**SQLAlchemy:**

Descripción: Biblioteca de mapeo objeto-relacional (ORM) para trabajar con bases de datos.

Instalación: pip install SQLAlchemy

**TensorFlow:**

Descripción: Biblioteca de aprendizaje automático y redes neuronales.

Instalación: pip install tensorflow

**PyTorch:**

Descripción: Biblioteca de aprendizaje profundo y redes neuronales desarrollada por Facebook.

Instalación: Puedes encontrar las instrucciones de instalación en el sitio web oficial de PyTorch (https://pytorch.org/).

**Scikit-Learn:**

Descripción: Biblioteca para aprendizaje automático y minería de datos.

Instalación: pip install scikit-learn
