peliculas = {
    'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
    'P102': ['Noche Neón', 'acción', 125, 'C', 'Ingles', True],
    'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español', False],
    'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
    'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
    'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles', False],}
cartelera = {
    'P101': [5990, 40],
    'P102': [7990, 0],
    'P103': [4990, 25],
    'P104': [6990, 12],
    'P105': [8990, 8],
    'P106': [7490, 3],}
def cupos_genero(genero):
    cupo=0
    for codigo in peliculas:
        if genero==peliculas[codigo][1]:
            cupo+=cartelera[codigo][1]
    if cupo>0:
        print(f"Hay {cupo} cupos de ese genero")
    else:
        print("No hay cupo")


def busqueda_precio(p_min, p_max):
    lista_pelicula=""
    for codigo in cartelera:
        if p_max>=cartelera[codigo][0]>=p_min:
            lista_pelicula+=peliculas[codigo][0]
            lista_pelicula+="--"
    if len(lista_pelicula)==0:
        print("No hay peliculas en ese rango")
    else:
        print(f"{lista_pelicula}")

def actualizar_precio(codigo, nuevo_precio):
    for codigo in cartelera:
        if codigo_pelicula not in cartelera:
            return False
        elif codigo_pelicula in cartelera:
            cartelera[codigo][0]=nuevo_precio
            return True

def agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos):
    peliculas+=[codigo][titulo][genero][duracion][clasificacion][idioma][es_3d]
    cartelera+=[codigo][precio][cupos]

def eliminar_pelicula(codigo): 
    for codigo in peliculas:
        if codigo==peliculas[codigo]:
            del peliculas[codigo]
            del cartelera[codigo]
    if codigo not in peliculas:
        print("No esta ese codigo")

def validacion_1(codigo):
    if codigo not in peliculas:
        return True
    else:
        print("El código ya existe") 
        return False
def validacion_2(titulo):
    titulo_p=""
    titulo=titulo_p
    titulo.strip()
    if len(titulo)==0 :
        titulo=titulo_p
        print("Esta mal el titulo")
        return False
    else:
        titulo=titulo_p
        return True
def validacion_3(genero):
    genero_p=""
    genero=genero_p
    genero.strip()
    if len(genero)==0 :
        genero=genero_p
        print("Esta mal el genero")
        return False
    else:
        genero=genero_p
        return True
def validacion_4(duracion):
    if duracion<=0:
        print("Esta mal la duracion")
        return False
    else:
        return True
def validacion_5(clasificacion):
    if clasificacion=="A" or clasificacion=="B" or clasificacion=="C":
        return True
    else:
        print("Esta mal")
        return False
def validacion_6(idioma):
    if len(idioma)==0:
        print("Esta mal el idioma")
        return False
    else:
        return True
def validacion_7(es_3d):
    if es_3d=="s" or es_3d=="n":
        if es_3d=="s":
            es_3d=True
        if es_3d=="n":
            es_3d=False
        return True
    else:
        print("Esta mal el 3D")
        return False
def validacion_8(precio):
    if precio<=0:
        print("Esta mal el precio")
        return False
    else:
        return True
def validacion_9(cupos):
    if cupos<0:
        print("Esta mal el cupo")
        return False
    else:
        return True

while True:
    print("""========== MENÚ PRINCIPAL ==========
1. Cupos por género
2. Búsqueda de películas por rango de precio
3. Actualizar precio de película
4. Agregar película
5. Eliminar película
6. Salir
=====================================""")
    try:
        opcion=int(input("Ingrese opcion: "))
        if opcion<=0 or opcion>6:
            print("Debe seleccionar una opción válida")
        elif opcion==1:
            genero=input("Ingrese genero a consultar: ").strip().lower()
            cupos_genero(genero)
        elif opcion==2:
            while True:
                try:
                    p_min=int(input("Ingrese precio mínimo: "))
                    p_max=int(input("Ingrese precio máximo: "))
                    busqueda_precio(p_min,p_max)
                    break
                except ValueError:
                    print("Debe ingresar valores enteros" )
        elif opcion==3:
            while True:
                try:
                    codigo_pelicula=input("Ingrese codigo de pelicula: ").strip().upper()
                    nuevo_precio=int(input("Ingrese nuevo precio: "))
                    if nuevo_precio>0:
                        actualizar_precio(codigo_pelicula,nuevo_precio)
                        if actualizar_precio(codigo_pelicula,nuevo_precio)==False:
                            print("El código no existe")
                        elif actualizar_precio(codigo_pelicula,nuevo_precio)==True:
                            print("Precio actualizado")
                        resp=input("¿Desea actualizar otro precio (s/n)?: ").strip().lower()
                        if resp=="s":
                            print("OK")
                        elif resp=="n":
                            print("Retornando a menu principal")
                            break
                    else:
                        print("Ingrese numero valido")
                except ValueError:
                    print("Ingrese un numero valido")
        elif opcion==4:
            codigo_pelicula=input("Ingrese codigo de la pelicula: ")
            titulo=input("Ingrese el titulo: ")
            genero=input("Ingrese el genero: ")
            duracion=int(input("Ingrese la duracion: "))
            clasificacion=input("Ingrese la clasificacion: ").strip().upper()
            idioma=input("Ingrese idioma: ").strip()
            es_3d=input("Ingrese si es 3D: ").strip().lower()
            precio=int(input("Ingrese el precio: "))
            cupos=int(input("Ingrese los cupos: "))
            if (validacion_1(codigo_pelicula) and validacion_2(titulo) and validacion_3(genero) and validacion_4(duracion) and validacion_5(clasificacion) and validacion_6(idioma) and validacion_7(es_3d) and validacion_8(precio) and validacion_9(cupos))==True:
                agregar_pelicula(codigo_pelicula,titulo,genero,duracion,clasificacion,idioma,es_3d,precio,cupos)
                print("Película agregada")
            else:
                print("Algo salio mal")
        elif opcion==5:
            codigo_pelicula=input("Ingrese el codigo de la pelicula: ")
            eliminar_pelicula(codigo_pelicula)
        elif opcion==6:
            print("Programa finalizado.")
            break
    except ValueError:
        print("Debe seleccionar una opción válida")