'''
 Modulo buscaminas
'''
import os
import numpy as np
import pygame

class Buscaminas:
    '''
    Clase buscaminas, todo lo necesario para jugar al juego
    '''

    # Variables para las imagenes que se cargan
    imagen_casilla = pygame.Surface
    imagen_bandera = pygame.Surface
    imagen_bomba = pygame.Surface
    imagen_cero = pygame.Surface
    imagen_uno = pygame.Surface
    imagen_dos = pygame.Surface
    imagen_tres = pygame.Surface
    imagen_cuatro = pygame.Surface
    imagen_cinco = pygame.Surface
    imagen_seis = pygame.Surface
    imagen_siete = pygame.Surface
    imagen_ocho = pygame.Surface

    def __init__(self,dificultad):
        self.longitudes = 8*dificultad  # Defino la longitud del tablero
        self.nro_minas = int # Numero de minas en el juego
        self.tam_cuadros_pix = int # Tamaño de los cuadros

        if dificultad == 1:  # dependiendo de la dificultad
            self.nro_minas = 10
        elif dificultad == 2:
            self.nro_minas = 40
        else:
            self.nro_minas = 70


    def set_tam_cuadros_pix(self, tam):
        '''
        defini el tamaño en pixeles de las casillas
        '''
        self.tam_cuadros_pix = tam


    def cargar_imagenes(self):  # Cargo las imagenes que utilizare a lo largo del juego
        '''
        Cargo todas las imagenes necesarias para jugar
        '''
        root_code= os.path.dirname(os.path.abspath(__file__))  # Path del codigo

        self.imagen_casilla = pygame.image.load(root_code+ "/Vainas_visuales/Buscaminas/Fondo.png")  # Busco la imagen de fondo de casillas
        self.imagen_casilla = pygame.transform.scale(self.imagen_casilla, (self.tam_cuadros_pix,self.tam_cuadros_pix))

        self.imagen_bandera = pygame.image.load(root_code+'/Vainas_visuales/Buscaminas/Bandera1.png') # Busco la image
        self.imagen_bandera = pygame.transform.scale(self.imagen_bandera, (self.tam_cuadros_pix,self.tam_cuadros_pix))

        self.imagen_bomba = pygame.image.load(root_code+'/Vainas_visuales/Buscaminas/Bomba.png')
        self.imagen_bomba = pygame.transform.scale(self.imagen_bomba, (self.tam_cuadros_pix,self.tam_cuadros_pix))

        self.imagen_cero = pygame.image.load(root_code+'/Vainas_visuales/Buscaminas/Nro0.png')
        self.imagen_cero = pygame.transform.scale(self.imagen_cero, (self.tam_cuadros_pix,self.tam_cuadros_pix))

        self.imagen_uno = pygame.image.load(root_code+'/Vainas_visuales/Buscaminas/Nro1.png')
        self.imagen_uno= pygame.transform.scale(self.imagen_uno, (self.tam_cuadros_pix,self.tam_cuadros_pix))

        self.imagen_dos = pygame.image.load(root_code+'/Vainas_visuales/Buscaminas/Nro2.png')
        self.imagen_dos = pygame.transform.scale(self.imagen_dos, (self.tam_cuadros_pix,self.tam_cuadros_pix))

        self.imagen_tres = pygame.image.load(root_code+'/Vainas_visuales/Buscaminas/Nro3.png')
        self.imagen_tres = pygame.transform.scale(self.imagen_tres, (self.tam_cuadros_pix,self.tam_cuadros_pix))

        self.imagen_cuatro = pygame.image.load(root_code+'/Vainas_visuales/Buscaminas/Nro4.png')
        self.imagen_cuatro = pygame.transform.scale(self.imagen_cuatro, (self.tam_cuadros_pix,self.tam_cuadros_pix))

        self.imagen_cinco = pygame.image.load(root_code+'/Vainas_visuales/Buscaminas/Nro5.png')
        self.imagen_cinco = pygame.transform.scale(self.imagen_cinco, (self.tam_cuadros_pix,self.tam_cuadros_pix))

        self.imagen_seis = pygame.image.load(root_code+'/Vainas_visuales/Buscaminas/Nro6.png')
        self.imagen_seis = pygame.transform.scale(self.imagen_seis, (self.tam_cuadros_pix,self.tam_cuadros_pix))

        self.imagen_siete = pygame.image.load(root_code+'/Vainas_visuales/Buscaminas/Nro7.png')
        self.imagen_siete = pygame.transform.scale(self.imagen_siete, (self.tam_cuadros_pix,self.tam_cuadros_pix))

        self.imagen_ocho = pygame.image.load(root_code+'/Vainas_visuales/Buscaminas/Nro8.png')
        self.imagen_ocho = pygame.transform.scale(self.imagen_ocho, (self.tam_cuadros_pix,self.tam_cuadros_pix))

    def generar_tabla(self):
        '''
        Genera el tablero del juego, sin minas
        '''
        matriz = np.zeros((self.longitudes,self.longitudes),dtype=int) # Defino el Tablero.
        return matriz
        #print(Matriz)
        
        
    def contar_minas(self,matriz):
        for filas in range(self.longitudes):
            for columnas in range(self.longitudes):
                if matriz[filas][columnas] != 9:
                    matriz[filas][columnas] = 0
                    if filas-1 >= 0 and columnas-1 >= 0 and matriz[filas-1][columnas-1] == 9:    #Verifico Arriba a la izquierda
                        matriz[filas][columnas] += 1

                    if filas-1 >= 0 and matriz[filas-1][columnas] == 9:    # Verifico Arriba
                        matriz[filas][columnas] += 1

                    if filas-1 >= 0 and columnas+1 < self.longitudes and matriz[filas-1][columnas+1] == 9: # Verifico arriba a la derecha
                        matriz[filas][columnas] += 1

                    if columnas-1 >=0 and matriz[filas][columnas-1] == 9:  #Verifico a la izquieda
                        matriz[filas][columnas] += 1

                    if columnas+1 < self.longitudes and matriz[filas][columnas+1] == 9: # Verifico a la derecha
                        matriz[filas][columnas] += 1

                    if filas+1 < self.longitudes and columnas-1 >= 0 and matriz[filas+1][columnas-1] == 9:    #Verifico abajo a la izquierda
                        matriz[filas][columnas] += 1

                    if filas+1 < self.longitudes and matriz[filas+1][columnas] == 9:    # Verifico abajo
                        matriz[filas][columnas] += 1

                    if filas+1 < self.longitudes and columnas+1 < self.longitudes and matriz[filas+1][columnas+1] == 9: # Verifico abajo a la derecha
                        matriz[filas][columnas] += 1

    def generar_minas(self,matriz,fila,columa):
        '''
        genera las minas en el tablero entregado
        '''
        contador_minas = 0
        while contador_minas < self.nro_minas:
            random_columna = np.random.randint(0,self.longitudes)
            random_fila = np.random.randint(0,self.longitudes)
            if (random_columna != columa and random_fila != fila and (abs(fila-random_fila) >= 2 or abs(columa-random_columna) >= 2)):  # se busca que la posicion del primer click este vacia y su alrededor
                if matriz[random_fila][random_columna] != 9:
                    matriz[random_fila][random_columna] = 9
                    contador_minas += 1
        self.contar_minas(matriz)

    def dibujar_cuadrados(self, ventana, tam_cuadros, rect_x, rect_y,RectL,Colores):
        '''
        Objetivo: Dibuja los cuadrados sobre los cuales se juega.
        * Ventana: pygame.display donde se dibujara.
        * TamCadros: int valor del tamaño de los cuadros
        * RectX: int Posicion en X del cuadro
        * RectY: int Posicion en Y del cuadro
        * RectL: int Tamaño del Rectangulo
        * Colores: Dict Diccionario con los colores
        '''

        # for i in range(self.Longitudes-1):  # Lineas Horizontales.
        #     #pygame.draw.rect(Ventana, Colores['Negro'], (RectX, RectY+(TamCuadros*(i+1)), RectL,4),border_radius=2)
        #     #pygame.draw.rect(Ventana, Colores['Negro'], (RectX+(TamCuadros*(i+1)), RectY, 4,RectL),border_radius=2)  # Antiguo codigo
        for i in range(self.longitudes):
            for k in range(self.longitudes):
                ventana.blit(self.imagen_casilla, (rect_x+(tam_cuadros*k), rect_y+(tam_cuadros*i)))

    def descubrir_ficha(self,ventana,matriz,tam_cuadros, rect_x,rect_y,colores,fila,columna): 
        '''
        Objetivo: Descubre la ficha seleccionada en la ventana por medio de los parametros Fila, Columna
        * Ventana: pygame.display donde se dibujara.
        * Matriz: np.array donde esta almacenado el Tablero
        * TamCadros: int valor del tamaño de los cuadros
        * RectX: int Posicion en X del cuadro
        * RectY: int Posicion en Y del cuadro
        * Colores: Dict Diccionario con los colores (Ya no se utiliza)
        * Fila: int Cordenadas en la matriz
        * Columna: int Cordenadas en la matriz
        ''' 
        if matriz[fila][columna] == 0:
            ventana.blit(self.imagen_cero, (rect_x+tam_cuadros*columna, rect_y+tam_cuadros*fila))
        elif matriz[fila][columna] == 1:
            ventana.blit(self.imagen_uno, (rect_x+tam_cuadros*columna, rect_y+tam_cuadros*fila))
        elif matriz[fila][columna] == 2:
            ventana.blit(self.imagen_dos, (rect_x+tam_cuadros*columna, rect_y+tam_cuadros*fila))
        elif matriz[fila][columna] == 3:
            ventana.blit(self.imagen_tres, (rect_x+tam_cuadros*columna, rect_y+tam_cuadros*fila))
        elif matriz[fila][columna] == 4:
            ventana.blit(self.imagen_cuatro, (rect_x+tam_cuadros*columna, rect_y+tam_cuadros*fila))
        elif matriz[fila][columna] == 5:
            ventana.blit(self.imagen_cinco, (rect_x+tam_cuadros*columna, rect_y+tam_cuadros*fila))
        elif matriz[fila][columna] == 6:
            ventana.blit(self.imagen_seis, (rect_x+tam_cuadros*columna, rect_y+tam_cuadros*fila))
        elif matriz[fila][columna] == 7:
            ventana.blit(self.imagen_siete, (rect_x+tam_cuadros*columna, rect_y+tam_cuadros*fila))
        elif matriz[fila][columna] == 8:
            ventana.blit(self.imagen_ocho, (rect_x+tam_cuadros*columna, rect_y+tam_cuadros*fila))
        elif matriz[fila][columna] == 9:
            ventana.blit(self.imagen_bomba, (rect_x+tam_cuadros*columna, rect_y+tam_cuadros*fila))

        # pygame.draw.rect(Ventana, Colores['Blanco'],
        #                  ((RectX+TamCuadros*Columna)+4,(RectY+TamCuadros*Fila)+4, TamCuadros-4,TamCuadros-4))
        #Antiguo Codigo  pygame.font.init()
        #Antiguo Codigo  Fuente = pygame.font.SysFont("Arial", 20, True).render(str(Matriz[Fila][Columna]),True,Colores['Negro'])
        #Antiguo Codigo #Ventana.blit(Fuente, ((RectX+TamCuadros*Columna)+(TamCuadros/2),(RectY+TamCuadros*Fila)+(TamCuadros/2)-10))   # Muestra el valor almacenado en la posicion dicha en Matriz


    def dibujar_banderas(self,ventana,tam_cuadros, rect_x,rect_y,colores,fila,columna,banderas):
        '''
        Objetivo: Coloca en la posicion seleccionada una bandera
        * Ventana: pygame.display donde se dibujara.
        * TamCadros: int valor del tamaño de los cuadros
        * RectX: int Posicion en X del cuadro
        * RectY: int Posicion en Y del cuadro
        * Colores: Dict Diccionario con los colores
        * Fila: int Cordenadas en la matriz
        * Columna: int Cordenadas en la matriz
        '''
        pygame.font.init()
        estado = False  # Si pongo bandera o quito
        pos = 0   # Indice a eliminar
        fuente = pygame.font.SysFont("Arial", 20, True).render("B",True,colores['Negro'])  # Creo una fuente

        for index, elem in enumerate(banderas):
            if elem[0] == fila and elem[1] == columna:
                estado = True
                pos = index
                break

        if estado:
            #pygame.draw.rect(Ventana, Colores['Rojo'],    # Pinto un bloque rojo para quitar banderas   <-  Antiguo codigo
            #                 ((RectX+TamCuadros*Columna)+4,(RectY+TamCuadros*Fila)+4, TamCuadros-4,TamCuadros-4)) 
            ventana.blit(self.imagen_casilla, (rect_x+tam_cuadros*columna, rect_y+tam_cuadros*fila))    
            banderas.pop(pos)  # Elimino la bandera de la lista  
        else:
            #Antiguo codigo -> #Ventana.blit(Fuente, ((RectX+TamCuadros*Columna)+(TamCuadros/2),(RectY+TamCuadros*Fila)+(TamCuadros/2)-10))   # Muestra el valor almacenado en la posicion dicha en Matriz
            ventana.blit(self.imagen_bandera, (rect_x+tam_cuadros*columna, rect_y+tam_cuadros*fila))           
            banderas.append([fila,columna])  # Agrago una vandera a la lista


    def verificar_zeros(self, ventana,matriz, tam_cuadros, rect_x, rect_y, colores, fila,columna,visited):
        '''
        Objetivo: Mostrar todos las fichas que rodean una ficha de valor 0 y si encuentra mas fichas con ese valor tambien las limpia
        * ventana: pygame.display donde se dibujara.
        * matriz: np.array Tablero del juego
        * tamCadros: int valor del tamaño de los cuadros
        * rect_x: int Posicion en X del cuadro
        * rect_y: int Posicion en Y del cuadro
        * colores: Dict Diccionario con los colores
        * fila: int Cordenadas en la matriz
        * columna: int Cordenadas en la matriz
        * visited: np.array un array lleno de falses, aquivalente a la matriz tablero
        '''
        if fila-1 >= 0 and columna-1 >= 0 and matriz[fila-1][columna-1] != 9:    #Verifico Arriba a la izquierda
            self.descubrir_ficha(ventana,matriz,tam_cuadros,rect_x,rect_y,colores,fila-1,columna-1) # DEscubro la ficha en esa posicion
            if matriz[fila-1][columna-1] == 0 and not visited[fila-1][columna-1]:  # Si existe un 0 y no ha sido visitado entro a destapar sus casillas tambien
                visited[fila][columna] = True #lo marco como visitado
                self.verificar_zeros(ventana,matriz, tam_cuadros, rect_x, rect_y, colores,fila-1,columna-1,visited)  # llamado recursivo para limpiar el nuevo 0

        if fila-1 >= 0 and matriz[fila-1][columna] != 9:    # Verifico Arriba
            self.descubrir_ficha(ventana,matriz,tam_cuadros,rect_x,rect_y,colores,fila-1,columna) # DEscubro la ficha en esa posicion
            if matriz[fila-1][columna] == 0 and not visited[fila-1][columna]: # Si existe un 0 y no ha sido visitado entro a destapar sus casillas tambien
                visited[fila][columna] = True #lo marco como visitado
                self.verificar_zeros(ventana,matriz, tam_cuadros, rect_x, rect_y, colores,fila-1,columna,visited)   # llamado recursivo para limpiar el nuevo 0

        if fila-1 >= 0 and columna+1 < self.longitudes and matriz[fila-1][columna+1] != 9: # Verifico arriba a la derecha
            self.descubrir_ficha(ventana,matriz,tam_cuadros,rect_x,rect_y,colores,fila-1,columna+1) # DEscubro la ficha en esa posicion
            if matriz[fila-1][columna+1] == 0 and not visited[fila-1][columna+1]: # Si existe un 0 y no ha sido visitado entro a destapar sus casillas tambien
                visited[fila][columna] = True #lo marco como visitado
                self.verificar_zeros(ventana,matriz, tam_cuadros, rect_x, rect_y, colores,fila-1,columna+1,visited)  # llamado recursivo para limpiar el nuevo 0

        if columna-1 >=0 and matriz[fila][columna-1] != 9:  #Verifico a la izquieda
            self.descubrir_ficha(ventana,matriz,tam_cuadros,rect_x,rect_y,colores,fila,columna-1) # DEscubro la ficha en esa posicion
            if matriz[fila][columna-1] == 0 and not visited[fila][columna-1]: # Si existe un 0 y no ha sido visitado entro a destapar sus casillas tambien
                visited[fila][columna] = True #lo marco como visitado
                self.verificar_zeros(ventana,matriz, tam_cuadros, rect_x, rect_y, colores,fila,columna-1,visited)  # llamado recursivo para limpiar el nuevo 0

        if columna+1 < self.longitudes and matriz[fila][columna+1] != 9: # Verifico a la derecha
            self.descubrir_ficha(ventana,matriz,tam_cuadros,rect_x,rect_y,colores,fila,columna+1) # DEscubro la ficha en esa posicion
            if matriz[fila][columna+1] == 0 and not visited[fila][columna+1]: # Si existe un 0 y no ha sido visitado entro a destapar sus casillas tambien
                visited[fila][columna] = True #lo marco como visitado
                self.verificar_zeros(ventana,matriz, tam_cuadros, rect_x, rect_y, colores,fila,columna+1,visited)  # llamado recursivo para limpiar el nuevo 0

        if fila+1 < self.longitudes and columna-1 >= 0 and matriz[fila+1][columna-1] != 9:    #Verifico abajo a la izquierda
            self.descubrir_ficha(ventana,matriz,tam_cuadros,rect_x,rect_y,colores,fila+1,columna-1)  # DEscubro la ficha en esa posicion
            if matriz[fila+1][columna-1] == 0 and not visited[fila+1][columna-1]: # Si existe un 0 y no ha sido visitado entro a destapar sus casillas tambien
                visited[fila][columna] = True #lo marco como visitado
                self.verificar_zeros(ventana,matriz, tam_cuadros, rect_x, rect_y, colores,fila+1,columna-1,visited)  # llamado recursivo para limpiar el nuevo 0

        if fila+1 < self.longitudes and matriz[fila+1][columna] != 9:    # Verifico abajo
            self.descubrir_ficha(ventana,matriz,tam_cuadros,rect_x,rect_y,colores,fila+1,columna) # DEscubro la ficha en esa posicion
            if matriz[fila+1][columna] == 0 and not visited[fila+1][columna]: # Si existe un 0 y no ha sido visitado entro a destapar sus casillas tambien
                visited[fila][columna] = True #lo marco como visitado
                self.verificar_zeros(ventana,matriz, tam_cuadros, rect_x, rect_y, colores,fila+1,columna,visited)  # llamado recursivo para limpiar el nuevo 0

        if fila+1 < self.longitudes and columna+1 < self.longitudes and matriz[fila+1][columna+1] != 9: # Verifico abajo a la derecha
            self.descubrir_ficha(ventana,matriz,tam_cuadros,rect_x,rect_y,colores,fila+1,columna+1) # DEscubro la ficha en esa posicion
            if matriz[fila+1][columna+1] == 0 and visited[fila+1][columna+1]: # Si existe un 0 y no ha sido visitado entro a destapar sus casillas tambien
                visited[fila][columna] = True #lo marco como visitado
                self.verificar_zeros(ventana,matriz, tam_cuadros, rect_x, rect_y, colores,fila+1,columna+1,visited)  # llamado recursivo para limpiar el nuevo 0
        return None
