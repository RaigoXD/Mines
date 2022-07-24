'''
 Modulo buscaminas
'''
import numpy as np

class Buscaminas:
    '''
    Clase buscaminas, todo lo necesario para jugar al juego
    '''


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



    def generar_tabla(self):
        '''
        Genera el tablero del juego, sin minas
        '''
        matriz = np.zeros((self.longitudes,self.longitudes),dtype=int) # Defino el Tablero.
        return matriz
        #print(Matriz)


    def contar_minas(self,matriz):
        '''
        Genera los numeros en la matriz de minas
        '''
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

    def set_tam_cuadros_pix(self, tam):
        '''
        define el tamaño en pixeles de las casillas
        '''
        self.tam_cuadros_pix = tam

    
    