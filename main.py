'''
    Modulo principal para el juego
'''
import pygame
from clases import *

Colores = {
    'Amarillo' : np.array([248,248,5]), 'Blanco' : np.array([255,255,255]), 'Rosado' : np.array([250,5,250]),
    'Rojo' : np.array([255,0,0]), 'Gris' : np.array([131,131,131]), 'Verde' : np.array([5,250,6]),
    'Negro' : np.array([0,0,0]), 'Azul' : np.array([4,4,251]), 'Cian' : np.array([4,251,251])
    }

pygame.init()
pygame.font.init()


#Dimensiones de la ventana del juego y su  deficion como pygame.display
ventana_x = 1280  # Dimensiones de la ventana en X
ventana_y = 800  # Dimensiones de la ventana en Y
    
# Dimensiones y pocisiones del rectangulo
rect_x = (ventana_x/2 - (ventana_y-100)/2) # Posicion en X del cuadrado 
rect_y = 50  # Posicion en Y del cuadrado
rect_l = ventana_y - 100  # longuitud del cuadrado

flags = pygame.SHOWN | pygame.SCALED #| pygame.FULLSCREEN # Atributos especiales de la ventana :)
Ventana_Juego = pygame.display.set_mode((ventana_x,ventana_y),
                                        flags) # Ventana del juego


def buscaminas_j():
    '''
        funcion para iniciar a jugar el juego de buscaminas
    '''
    #Infomacion del buscaminas
    modo = 1# Dioficultad del juego
    obj_buscaminas = Buscaminas(modo)  # Objeto Buscaminas
    tablero = obj_buscaminas.generar_tabla() # Genero el mapa sobre el cual voy a jugar.
    #ObjBuscaminas.GenerarMinas(Tablero)
    cuadrados = obj_buscaminas.longitudes # Cantidad de cuadros actual :)
    tam_cuadros = rect_l / cuadrados  # Tamaño de los cuadros del buscaminas 
    obj_buscaminas.set_tam_cuadros_pix(tam_cuadros)  # iniciliazo el atributo TamCuadrosPix
    obj_buscaminas.cargar_imagenes() # Cargo las imagenes con las que se jugara el buscaminas 
    num_bombas = obj_buscaminas.nro_minas

    print(tablero)
    # definicion de la ventana del juego
    Ventana_Juego.fill(Colores['Blanco'])   # Pinto el fondo de color Blanco

    obj_buscaminas.dibujar_cuadrados(Ventana_Juego, tam_cuadros, rect_x,rect_y,rect_l,Colores) # Dibujo las lineas del juego

    #Defino el reloj para la frecuencia del juego
    clock = pygame.time.Clock()

    terminar = False

    primer_click = True
    pos_x = int # Posiciones del Click
    pos_y = int # Posiciones del click
    fila = int # Posicione en la Matriz Fila
    columna = int # posicion en la Matriz Columna
    txt_perder = pygame.font.SysFont("Arial", 100, True).render("Perdiste",True,Colores['Negro'])
    txt_ganar = pygame.font.SysFont("Arial", 100, True).render("Ganaste",True,Colores['Amarillo'])
    banderas = []  # Banderas Puestas
    casillas_descubiertas = 0

    while not terminar: # Ciclo principal del juego
        for events in pygame.event.get():  # Este evento controla el boton de cerrar de la ventana.
            if events.type == pygame.QUIT:
                terminar = True

            if events.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]: #Si el Boton izquierdo del mouse fue precionado
                    pos_x = pygame.mouse.get_pos()[0]  #posicion en x del click
                    pos_y = pygame.mouse.get_pos()[1]  # posicion en y del click
                    if pos_x > rect_x and pos_x < rect_x+rect_l-5 and pos_y > 50 and pos_y < 50+rect_l-5: # si esta dentro de los limites del cuadro
                        columna = int((pos_x - rect_x) // tam_cuadros)  # Calculo las posiciones en Columnas 
                        fila = int((pos_y - rect_y) // tam_cuadros)  # Calculo las posiciones en Filas
                        print(casillas_descubiertas)
                        if primer_click is True:
                            tablero = obj_buscaminas.generar_tabla()
                            obj_buscaminas.generar_minas(tablero,fila,columna)
                            primer_click = False
                            print(tablero)

                        obj_buscaminas.descubrir_ficha(Ventana_Juego,   #Descubro la Ficha donde se dio click
                                                    tablero,
                                                    tam_cuadros,rect_x,rect_y,Colores,fila,columna)
                        
                        if tablero[fila][columna] == 9:  # Si es una mina fin del juego :)
                            Ventana_Juego.blit(txt_perder, (ventana_x/2-100, ventana_y/2-100))
                            terminar = True

                        if tablero[fila][columna] == 0:
                            visited = tablero > 20
                            obj_buscaminas.verificar_zeros(Ventana_Juego,      #Descubro las Fichas al lado de ese 0
                                                        tablero,
                                                        tam_cuadros,rect_x,rect_y,Colores,fila,columna,visited)

                        if casillas_descubiertas == (cuadrados*cuadrados) - num_bombas:
                            Ventana_Juego.blit(txt_ganar, (ventana_x/2-100, ventana_y/2-100))
                            terminar = True

                if pygame.mouse.get_pressed()[2]:  # Si el boton derecho del mouse fue precionado
                    pos_x = pygame.mouse.get_pos()[0]  #posicion en x del click
                    pos_y = pygame.mouse.get_pos()[1]  # posicion en y del click
                    if pos_x >= rect_x and pos_x <= rect_x+rect_l and pos_y >= 50 and pos_y <= 50+rect_l: # si esta dentro de los limites del cuadro
                        columna = int((pos_x - rect_x) // tam_cuadros)  # Calculo las posiciones en Columnas 
                        fila = int((pos_y - rect_y) // tam_cuadros)  # Calculo las posiciones en Filas

                        #print("(" + str(Columna) + "," + str(Fila)+ ")")
                        #print(Banderas)
                        obj_buscaminas.dibujar_banderas(Ventana_Juego,  # Coloco una Bandera
                                                      tam_cuadros,rect_x, rect_y,Colores,fila,columna,banderas)

        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    buscaminas_j()