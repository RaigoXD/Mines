'''
Todo para dibujar los menus del juego
'''
import pygame
import os

ROOTCODE= os.path.dirname(os.path.abspath(__file__))  # Path del codigo
ROOTIMAGES = ROOTCODE + "/../Vainas_visuales/menus"

def dibujar_botones(ventana:pygame.Surface,pos:tuple,colores, txt1: str = "",  txt2: str = ""):
    '''
    Esta funcion dibuja los botones bonitos :)
    '''
    pos_2 = (pos[0]+9, pos[1]+1, pos[2]-10, pos[3]-10)

    txt_1 = pygame.font.SysFont("ubuntumono", 40, True).render(txt1,True,colores['Negro'])
    txt_2 = pygame.font.SysFont("ubuntumono", 40, True).render(txt2,True,colores['Negro'])

    pygame.draw.rect(ventana, colores['Gris'],pos,border_radius=30)
    pygame.draw.rect(ventana, colores['Verde2'],pos_2,border_radius=30)

    ventana.blit(txt_1, (pos[0]+(pos[2]/2)-40, pos[1]+(pos[3]/2)-50))
    ventana.blit(txt_2, (pos[0]+(pos[2]/2)-80, pos[1]+(pos[3]/2)))

def dibujar_main_menu(ventana: pygame.Surface, colores: dict):
    '''
    Dibuja todo el menu principal
    '''
    weigth = ventana.get_width()
    heigth = ventana.get_height()

    ventana.fill(colores['Beige']) # fondo

    pygame.draw.line(ventana, colores['Negro'], (0,150), (weigth, 150))
    pygame.draw.line(ventana, colores['Negro'], (weigth-200,0), (weigth-200, heigth))

    dibujar_botones(ventana,(50,170,350,250),colores, "8 X 8", "10 MINAS")  # botones
    dibujar_botones(ventana,(429,170,350,250), colores, "16 X 16", "40 MINAS")
    dibujar_botones(ventana,(50,460,350,250), colores, "24 x 24", "70 MINAS")
    dibujar_botones(ventana,(429,460,350,250), colores, "CREDITOS")

    title = pygame.font.SysFont("ubuntumono", 100, True).render("MINES",True,colores['Negro'])  # titulo
    ventana.blit(title, (50, 50))

    imagen_raigoza = pygame.image.load(ROOTIMAGES + '/ME.png')
    imagen_raigoza = pygame.transform.scale(imagen_raigoza,(250,250))
    ventana.blit(imagen_raigoza, (800, 10))  # imagen del author :)

    imagen_git = pygame.image.load(ROOTIMAGES + '/github.png')
    imagen_git = pygame.transform.scale(imagen_git, (190, 140))

    ventana.blit(imagen_git, (830, 620))

def main_menu(ventana: pygame.Surface, colores:dict):
    '''
    Controla el menu principal del juego
    '''
    weigth = ventana.get_width()
    heigth = ventana.get_height()
    
    
    dibujar_main_menu(ventana, colores)
    #Reloj del juego, frecuencia
    clock = pygame.time.Clock()
    terminar = False

    while not terminar:

        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                terminar = True
            if events.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    pos_x = pygame.mouse.get_pos()[0]  #posicion en x del click
                    pos_y = pygame.mouse.get_pos()[1]  # posicion en y del click
                    print(f"{pos_x}-{pos_y}")

        pygame.display.flip()
        clock.tick(60)

    print(f"{heigth}\n{weigth}")

