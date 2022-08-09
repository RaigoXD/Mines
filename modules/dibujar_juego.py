'''
Modulo para dibujar todo lo que se ve en pantalla
'''
import os
import pygame

class Draw:
    '''
    Clase draw para dibujar todo lo que se ve en pantalla
    * tam_pixels: tamaño en pixeles de los cuadrados
    * tam_tablero: tamaño del tablero actual
    '''
    # Variables para las imagenes que se cargan
    imagen_casilla: pygame.Surface
    imagen_bandera: pygame.Surface
    imagen_bomba: pygame.Surface
    imagen_cero: pygame.Surface
    imagen_uno: pygame.Surface
    imagen_dos: pygame.Surface
    imagen_tres: pygame.Surface
    imagen_cuatro: pygame.Surface
    imagen_cinco: pygame.Surface
    imagen_seis: pygame.Surface
    imagen_siete: pygame.Surface
    imagen_ocho: pygame.Surface

    def __init__(self, tam_pixels, tam_tablero):
        self.tam_cuadros_pix = tam_pixels
        self.longitudes = tam_tablero

    def cargar_imagenes(self):    
        '''
        Cargo todas las imagenes necesarias para jugar
        '''
        root_code= os.path.dirname(os.path.abspath(__file__))    
        root_images = root_code + "/../Vainas_visuales/Buscaminas/"

        self.imagen_casilla = pygame.image.load(root_images + '/Fondo.png')
        self.imagen_casilla = pygame.transform.scale(self.imagen_casilla, (self.tam_cuadros_pix,self.tam_cuadros_pix))

        self.imagen_bandera = pygame.image.load(root_images+'/Bandera1.png')
        self.imagen_bandera = pygame.transform.scale(self.imagen_bandera, (self.tam_cuadros_pix,self.tam_cuadros_pix))

        self.imagen_bomba = pygame.image.load(root_images+'/Bomba.png')
        self.imagen_bomba = pygame.transform.scale(self.imagen_bomba, (self.tam_cuadros_pix,self.tam_cuadros_pix))

        self.imagen_cero = pygame.image.load(root_images+'/Nro0.png')
        self.imagen_cero = pygame.transform.scale(self.imagen_cero, (self.tam_cuadros_pix,self.tam_cuadros_pix))

        self.imagen_uno = pygame.image.load(root_images+'/Nro1.png')
        self.imagen_uno= pygame.transform.scale(self.imagen_uno, (self.tam_cuadros_pix,self.tam_cuadros_pix))

        self.imagen_dos = pygame.image.load(root_images+'/Nro2.png')
        self.imagen_dos = pygame.transform.scale(self.imagen_dos, (self.tam_cuadros_pix,self.tam_cuadros_pix))

        self.imagen_tres = pygame.image.load(root_images+'/Nro3.png')
        self.imagen_tres = pygame.transform.scale(self.imagen_tres, (self.tam_cuadros_pix,self.tam_cuadros_pix))

        self.imagen_cuatro = pygame.image.load(root_images+'/Nro4.png')
        self.imagen_cuatro = pygame.transform.scale(self.imagen_cuatro, (self.tam_cuadros_pix,self.tam_cuadros_pix))

        self.imagen_cinco = pygame.image.load(root_images+'/Nro5.png')
        self.imagen_cinco = pygame.transform.scale(self.imagen_cinco, (self.tam_cuadros_pix,self.tam_cuadros_pix))

        self.imagen_seis = pygame.image.load(root_images+'/Nro6.png')
        self.imagen_seis = pygame.transform.scale(self.imagen_seis, (self.tam_cuadros_pix,self.tam_cuadros_pix))

        self.imagen_siete = pygame.image.load(root_images+'/Nro7.png')
        self.imagen_siete = pygame.transform.scale(self.imagen_siete, (self.tam_cuadros_pix,self.tam_cuadros_pix))

        self.imagen_ocho = pygame.image.load(root_images+'/Nro8.png')
        self.imagen_ocho = pygame.transform.scale(self.imagen_ocho, (self.tam_cuadros_pix,self.tam_cuadros_pix))

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
        estado = False    
        pos = 0     
        #fuente = pygame.font.SysFont("Arial", 20, True).render("B",True,colores['Negro'])  # Creo una fuente

        for index, elem in enumerate(banderas):
            if elem[0] == fila and elem[1] == columna:
                estado = True
                pos = index
                break

        if estado:
            #pygame.draw.rect(Ventana, Colores['Rojo'],    # Pinto un bloque rojo para quitar banderas   <-  Antiguo codigo
            #                 ((RectX+TamCuadros*Columna)+4,(RectY+TamCuadros*Fila)+4, TamCuadros-4,TamCuadros-4)) 
            ventana.blit(self.imagen_casilla, (rect_x+tam_cuadros*columna, rect_y+tam_cuadros*fila))    
            banderas.pop(pos)    
        else:
            #Antiguo codigo -> #Ventana.blit(Fuente, ((RectX+TamCuadros*Columna)+(TamCuadros/2),(RectY+TamCuadros*Fila)+(TamCuadros/2)-10))   # Muestra el valor almacenado en la posicion dicha en Matriz
            ventana.blit(self.imagen_bandera, (rect_x+tam_cuadros*columna, rect_y+tam_cuadros*fila))           
            banderas.append([fila,columna])    


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
        if fila-1 >= 0 and columna-1 >= 0 and matriz[fila-1][columna-1] != 9:      
            self.descubrir_ficha(ventana,matriz,tam_cuadros,rect_x,rect_y,colores,fila-1,columna-1)   
            if matriz[fila-1][columna-1] == 0 and not visited[fila-1][columna-1]:    
                visited[fila][columna] = True   
                self.verificar_zeros(ventana,matriz, tam_cuadros, rect_x, rect_y, colores,fila-1,columna-1,visited)    

        if fila-1 >= 0 and matriz[fila-1][columna] != 9:      
            self.descubrir_ficha(ventana,matriz,tam_cuadros,rect_x,rect_y,colores,fila-1,columna)   
            if matriz[fila-1][columna] == 0 and not visited[fila-1][columna]:   
                visited[fila][columna] = True   
                self.verificar_zeros(ventana,matriz, tam_cuadros, rect_x, rect_y, colores,fila-1,columna,visited)     

        if fila-1 >= 0 and columna+1 < self.longitudes and matriz[fila-1][columna+1] != 9:   
            self.descubrir_ficha(ventana,matriz,tam_cuadros,rect_x,rect_y,colores,fila-1,columna+1)   
            if matriz[fila-1][columna+1] == 0 and not visited[fila-1][columna+1]:   
                visited[fila][columna] = True   
                self.verificar_zeros(ventana,matriz, tam_cuadros, rect_x, rect_y, colores,fila-1,columna+1,visited)    

        if columna-1 >=0 and matriz[fila][columna-1] != 9:    
            self.descubrir_ficha(ventana,matriz,tam_cuadros,rect_x,rect_y,colores,fila,columna-1)   
            if matriz[fila][columna-1] == 0 and not visited[fila][columna-1]:   
                visited[fila][columna] = True   
                self.verificar_zeros(ventana,matriz, tam_cuadros, rect_x, rect_y, colores,fila,columna-1,visited)    

        if columna+1 < self.longitudes and matriz[fila][columna+1] != 9:   
            self.descubrir_ficha(ventana,matriz,tam_cuadros,rect_x,rect_y,colores,fila,columna+1)   
            if matriz[fila][columna+1] == 0 and not visited[fila][columna+1]:   
                visited[fila][columna] = True   
                self.verificar_zeros(ventana,matriz, tam_cuadros, rect_x, rect_y, colores,fila,columna+1,visited)    

        if fila+1 < self.longitudes and columna-1 >= 0 and matriz[fila+1][columna-1] != 9:      
            self.descubrir_ficha(ventana,matriz,tam_cuadros,rect_x,rect_y,colores,fila+1,columna-1)    
            if matriz[fila+1][columna-1] == 0 and not visited[fila+1][columna-1]:   
                visited[fila][columna] = True   
                self.verificar_zeros(ventana,matriz, tam_cuadros, rect_x, rect_y, colores,fila+1,columna-1,visited)    

        if fila+1 < self.longitudes and matriz[fila+1][columna] != 9:      
            self.descubrir_ficha(ventana,matriz,tam_cuadros,rect_x,rect_y,colores,fila+1,columna)   
            if matriz[fila+1][columna] == 0 and not visited[fila+1][columna]:   
                visited[fila][columna] = True   
                self.verificar_zeros(ventana,matriz, tam_cuadros, rect_x, rect_y, colores,fila+1,columna,visited)    

        if fila+1 < self.longitudes and columna+1 < self.longitudes and matriz[fila+1][columna+1] != 9:   
            self.descubrir_ficha(ventana,matriz,tam_cuadros,rect_x,rect_y,colores,fila+1,columna+1)   
            if matriz[fila+1][columna+1] == 0 and visited[fila+1][columna+1]:   
                visited[fila][columna] = True   
                self.verificar_zeros(ventana,matriz, tam_cuadros, rect_x, rect_y, colores,fila+1,columna+1,visited)
