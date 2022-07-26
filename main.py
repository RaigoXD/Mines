'''
    Modulo principal para el juego
'''
import pygame
import numpy as np
from modules.mines import Buscaminas
from modules.dibujar import Draw

pygame.init()
pygame.font.init()

#Constantes en el juego  (no usado, esperando)
COLORES = {
    'Amarillo' : np.array([248,248,5]), 'Blanco' : np.array([255,255,255]), 'Rosado' : np.array([250,5,250]),
    'Rojo' : np.array([255,0,0]), 'Gris' : np.array([131,131,131]), 'Verde' : np.array([5,250,6]),
    'Negro' : np.array([0,0,0]), 'Azul' : np.array([4,4,251]), 'Cian' : np.array([4,251,251])
    }

#Dimensiones de la ventana del juego y su  deficion como pygame.display
VENTANAX = 1024  # Dimensiones de la ventana en X
VENTANAY = 768  # Dimensiones de la ventana en Y

# Dimensiones y pocisiones del rectangulo
POSRECTX = (VENTANAX/2 - (VENTANAY-100)/2) # Posicion en X del cuadrado
POSRECTY = 50  # Posicion en Y del cuadrado
LONGITUDRECT = VENTANAY - 100  # longuitud del cuadrado

FLAGS = pygame.SHOWN | pygame.SCALED #| pygame.FULLSCREEN # Atributos especiales de la ventana :)

def is_inside(pos_x, pos_y) -> bool:
    '''
    Esta dentro del cuadrado del juego?
    '''
    return pos_x > POSRECTX and pos_x < POSRECTX+LONGITUDRECT-5 and pos_y > 50 and pos_y < 50+LONGITUDRECT-5


def buscaminas_j(ventana_juego, modo):
    '''
        funcion para iniciar a jugar el juego de buscaminas
    '''
    #Infomacion del buscaminas
    obj_buscaminas = Buscaminas(modo)  # Objeto Buscaminas
    tablero = obj_buscaminas.generar_tabla() # Genero el mapa sobre el cual voy a jugar.
    cuadrados = obj_buscaminas.longitudes # Cantidad de cuadros actual :)
    tam_cuadros = LONGITUDRECT / cuadrados  # Tamaño de los cuadros del buscaminas
    obj_buscaminas.set_tam_cuadros_pix(tam_cuadros)  # iniciliazo el atributo TamCuadrosPix
    #Objeto Draw para dibujar todo en el juego
    draw_obj = Draw(tam_cuadros,cuadrados)
    draw_obj.cargar_imagenes() # Cargo las imagenes con las que se jugara el buscaminas
    print(tablero)
    # definicion del color y el dibujo inicial
    ventana_juego.fill(COLORES['Gris'])   # Pinto el fondo de color Blanco
    draw_obj.dibujar_cuadrados(ventana_juego, tam_cuadros, POSRECTX,POSRECTY,LONGITUDRECT,COLORES) # Dibujo las lineas del juego
    #Defino el reloj para la frecuencia del juego
    clock = pygame.time.Clock()
    #Para eventor importantes
    terminar = False
    primer_click = True
    #Mensajes de Ganar y perder
    txt_perder = pygame.font.SysFont("Arial", 100, True).render("Perdiste",True,COLORES['Negro'])
    txt_ganar = pygame.font.SysFont("Arial", 100, True).render("Ganaste",True,COLORES['Amarillo'])
    # Variables del juego, Banderas, etc
    banderas = []  # Banderas Puestas
    casillas_descubiertas = 0  # Casillas descubiertas

    while not terminar: # Ciclo principal del juego
        for events in pygame.event.get():  # Este evento controla el boton de cerrar de la ventana.

            if events.type == pygame.QUIT:  # si cierra el juego
                terminar = True
            
            if events.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]: #Si el Boton izquierdo del mouse fue precionado
                    pos_x = pygame.mouse.get_pos()[0]  #posicion en x del click
                    pos_y = pygame.mouse.get_pos()[1]  # posicion en y del click
                    if is_inside(pos_x, pos_y): # si esta dentro de los limites del cuadro
                        columna = int((pos_x - POSRECTX) // tam_cuadros)  # Calculo las posiciones en Columnas 
                        fila = int((pos_y - POSRECTY) // tam_cuadros)  # Calculo las posiciones en Filas
                        
                        print(casillas_descubiertas)
                        
                        if primer_click:
                            tablero = obj_buscaminas.generar_tabla()
                            obj_buscaminas.generar_minas(tablero,fila,columna)
                            primer_click = False
                            print(tablero)

                        draw_obj.descubrir_ficha(ventana_juego,   #Descubro la Ficha donde se dio click
                                                    tablero,
                                                    tam_cuadros,POSRECTX,POSRECTY,COLORES,fila,columna)
                        
                        if tablero[fila][columna] == 9:  # Si es una mina fin del juego :)
                            ventana_juego.blit(txt_perder, (VENTANAX/2-100, VENTANAY/2-100))
                            terminar = True

                        if tablero[fila][columna] == 0:
                            visited = tablero > 20
                            draw_obj.verificar_zeros(ventana_juego,      #Descubro las Fichas al lado de ese 0
                                                        tablero,
                                                        tam_cuadros,POSRECTX,POSRECTY,COLORES,fila,columna,visited)

                        if casillas_descubiertas == (cuadrados*cuadrados) - obj_buscaminas.nro_minas:  #Ganar (arreglar esta horrible XD)
                            ventana_juego.blit(txt_ganar, (VENTANAX/2-100, VENTANAY/2-100))
                            terminar = True

                if pygame.mouse.get_pressed()[2]:  # Si el boton derecho del mouse fue precionado
                    pos_x = pygame.mouse.get_pos()[0]  #posicion en x del click
                    pos_y = pygame.mouse.get_pos()[1]  # posicion en y del click
                    if is_inside(pos_x,pos_y): # si esta dentro de los limites del cuadro
                        columna = int((pos_x - POSRECTX) // tam_cuadros)  # Calculo las posiciones en Columnas 
                        fila = int((pos_y - POSRECTY) // tam_cuadros)  # Calculo las posiciones en Filas

                        #print("(" + str(Columna) + "," + str(Fila)+ ")")
                        #print(Banderas)
                        draw_obj.dibujar_banderas(ventana_juego,  # Coloco una Bandera
                                                      tam_cuadros,POSRECTX, POSRECTY,COLORES,fila,columna,banderas)

        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':

    ventana = pygame.display.set_mode((VENTANAX,VENTANAY),
                                            FLAGS) # Ventana del juego
    pygame.display.set_caption("Mines")  # Cambio el nombre de la ventana

    buscaminas_j(ventana, 1)
