"""
    Modulo principal para el juego
"""
import os
import pygame
import numpy as np

from modules.menu import main_menu
from modules.mines import Buscaminas
from modules.dibujar_juego import Draw

pygame.init()
pygame.font.init()

# Constantes en el juego  (no usado, esperando)
COLORES = {
    "Amarillo": np.array([248, 248, 5]),
    "Blanco": np.array([255, 255, 255]),
    "Rosado": np.array([250, 5, 250]),
    "Rojo": np.array([255, 0, 0]),
    "Gris": np.array([131, 131, 131]),
    "Verde": np.array([5, 250, 6]),
    "Negro": np.array([0, 0, 0]),
    "Azul": np.array([4, 4, 251]),
    "Cian": np.array([4, 251, 251]),
    "Beige": np.array([255, 255, 221]),
    "Azul2": np.array([120, 194, 194]),
    "Verde2": np.array([183, 191, 153]),
}

# CONSTANTES VENTANA
ANCHOVENTANA = 1024
ALTOVENTANA = 768


POSICIONRECTX = ANCHOVENTANA / 2 - (ALTOVENTANA - 100) / 2
POSICIONRECTY = 50
LONGITUDRECT = ALTOVENTANA - 100

ROOTCODE = os.path.dirname(os.path.abspath(__file__))
ROOTIMAGES = ROOTCODE + "/Vainas_visuales/icons"


FLAGS = (
    pygame.SHOWN | pygame.SCALED
)  # | pygame.FULLSCREEN # Atributos especiales de la ventana :)


def is_inside(pos_x, pos_y) -> bool:
    """
    Esta dentro del cuadrado del juego?
    """
    return (
        pos_x > POSICIONRECTX
        and pos_x < POSICIONRECTX + LONGITUDRECT - 5
        and pos_y > 50
        and pos_y < 50 + LONGITUDRECT - 5
    )


def buscaminas_j(ventana_juego, modo):
    """
    funcion para iniciar a jugar el juego de buscaminas
    """
    # Infomacion del buscaminas
    obj_buscaminas = Buscaminas(modo)
    tablero = obj_buscaminas.generar_tabla()
    numero_cuadrados = obj_buscaminas.longitudes
    tamanio_cuadros = (LONGITUDRECT / numero_cuadrados)
    obj_buscaminas.set_tam_cuadros_pix(tamanio_cuadros)

    draw_obj = Draw(tamanio_cuadros, numero_cuadrados)
    draw_obj.cargar_imagenes()
    print(tablero)

    ventana_juego.fill(COLORES["Beige"])

    draw_obj.dibujar_cuadrados(
        ventana_juego, tamanio_cuadros, POSICIONRECTX, POSICIONRECTY, LONGITUDRECT, COLORES
    )

    clock = pygame.time.Clock()

    terminar_juego = False
    primer_click = True

    txt_perder = pygame.font.SysFont("Arial", 100, True).render(
        "Perdiste", True, COLORES["Negro"]
    )
    txt_ganar = pygame.font.SysFont("Arial", 100, True).render(
        "Ganaste", True, COLORES["Amarillo"]
    )

    banderas_ubicadas = []
    casillas_descubiertas = 0

    while not terminar_juego:
        for events in pygame.event.get():

            if events.type == pygame.QUIT:
                terminar_juego = True

            if events.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:    
                    pos_x = pygame.mouse.get_pos()[0]
                    pos_y = pygame.mouse.get_pos()[1]
                    if is_inside(pos_x, pos_y):    
                        columna = int(
                            (pos_x - POSICIONRECTX) // tamanio_cuadros
                        )
                        fila = int(
                            (pos_y - POSICIONRECTY) // tamanio_cuadros
                        )

                        print(casillas_descubiertas)

                        if primer_click:
                            tablero = obj_buscaminas.generar_tabla()
                            obj_buscaminas.generar_minas(tablero, fila, columna)
                            primer_click = False
                            print(tablero)

                        draw_obj.descubrir_ficha(
                            ventana_juego,
                            tablero,
                            tamanio_cuadros,
                            POSICIONRECTX,
                            POSICIONRECTY,
                            COLORES,
                            fila,
                            columna,
                        )

                        if tablero[fila][columna] == 9:
                            ventana_juego.blit(
                                txt_perder,
                                (ANCHOVENTANA / 2 - 100, ALTOVENTANA / 2 - 100),
                            )
                            terminar_juego = True

                        if tablero[fila][columna] == 0:
                            visited = tablero > 20
                            draw_obj.verificar_zeros(
                                ventana_juego,
                                tablero,
                                tamanio_cuadros,
                                POSICIONRECTX,
                                POSICIONRECTY,
                                COLORES,
                                fila,
                                columna,
                                visited,
                            )

                        if (casillas_descubiertas == (numero_cuadrados * numero_cuadrados)- obj_buscaminas.nro_minas):
                            ventana_juego.blit(
                                txt_ganar,
                                (ANCHOVENTANA / 2 - 100, ALTOVENTANA / 2 - 100),
                            )
                            terminar_juego = True

                if pygame.mouse.get_pressed()[2]:
                    pos_x = pygame.mouse.get_pos()[0]
                    pos_y = pygame.mouse.get_pos()[1]
                    if is_inside(pos_x, pos_y):
                        columna = int(
                            (pos_x - POSICIONRECTX) // tamanio_cuadros
                        )
                        fila = int(
                            (pos_y - POSICIONRECTY) // tamanio_cuadros
                        )

                        draw_obj.dibujar_banderas(
                            ventana_juego,
                            tamanio_cuadros,
                            POSICIONRECTX,
                            POSICIONRECTY,
                            COLORES,
                            fila,
                            columna,
                            banderas_ubicadas,
                        )

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":

    ventana = pygame.display.set_mode(
        (ANCHOVENTANA, ALTOVENTANA), FLAGS
    )

    pygame.display.set_caption("Mines")
    icon = pygame.image.load(ROOTIMAGES + "/explosion.png")
    pygame.display.set_icon(icon)

    dificultad = main_menu(ventana, COLORES)
    if dificultad != 0:
        buscaminas_j(ventana, dificultad)
