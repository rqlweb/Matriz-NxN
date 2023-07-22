import unittest

#Funcion de suma de filas
def get_sum_rows( matriz ):
    
    # Creamos una lista para la suma de cada fila
    add_rows = []
    # Ciclo que recorre cada valor de la fila y suma sus valores
    for row in matriz:
        values_total = sum( row )
        add_rows.append( values_total )
    #Duelve una lista con la suma de los valores de cada fila
    return add_rows

#Funcion de suma de colummnas
def get_sum_columns(matriz):

    # Creamos una lista en la que se guarda la suma de cada columna
    add_columns = []
    # Obtenemos el tamaño de la matriz
    size_row = len( matriz )
    # Obtenemos el tamaño de columnas segun la primera fila
    size_column = len( matriz[0] )
    # Ciclo que realiza la suma de los valores de cada columna
    for index_column in range(size_column):
        #Variable que guarda la suma de las columnas y que se reinicia en cada vuelta
        columns_total = 0
        for index_row in range(size_row):
            columns_total += matriz[index_row][index_column]
        #Agregamos la suma de la columna 
        add_columns.extend([columns_total])
    #Duelve una lista con la suma de los valores de cada columna
    return add_columns

class Test(unittest.TestCase):  

    def test_rows_sum(self):
        
        matriz = [
            [4, 7, 9, 6],
            [1, 4, 9, 5],
            [2, 6, 8, 1],
            [8, 1, 5, 6]
        ]

        rows_total = get_sum_rows( matriz )
        self.assertEqual( rows_total, [26,19,17,20] )

    def test_row_unique( self ):

        single_row = [[2, 6, 8, 1]]
        row_total = get_sum_rows( single_row )
        self.assertEqual( row_total, [17] )

    def test_columns_sum(self):

        matriz = [
            [4, 7, 9, 6],
            [1, 4, 9, 5],
            [2, 6, 8, 1],
            [8, 1, 5, 6]
        ]

        columns_total = get_sum_columns( matriz )
        self.assertEqual( columns_total, [15,18,31,18] )

    def test_column_unique(self):
        single_column = [[9],[9],[8],[5]]
        column_total = get_sum_columns( single_column )
        self.assertEqual( column_total, [31] )


unittest.main()