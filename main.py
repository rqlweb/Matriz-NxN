
import random

print("Crear una Matriz de NxN");

# Funcion para la suma de las filas de la matriz 
def get_sum_rows( matriz ):
    
    # Creamos una lista para la suma de cada fila
    add_rows = []
    # Ciclo que recorre cada valor de la fila y suma sus valores
    for row in matriz:
        values_total = sum( row )
        add_rows.append( values_total )
    #Duelve una lista con la suma de los valores de cada fila
    return add_rows

# Funcion para la suma de las columnas de la matriz 
def get_sum_columns(matriz):

    # Creamos una lista en la que se guarda la suma de cada columna
    add_columns = []
    # Obtenemos el tamaño de la matriz
    size_row = len( matriz )
    # Obtenemos el tamaño de columnas segun la primera fila
    size_column = len( matriz[0] )
    # Ciclo que realiza la suma de los valores de cada columna considerando ambos indices
    for index_column in range(size_column):
        #Variable que guarda la suma de las columnas y que se reinicia en cada vuelta
        columns_total = 0
        for index_row in range(size_row):
            columns_total += matriz[index_row][index_column]
        #Agregamos la suma de la columna 
        add_columns.extend([columns_total])
    #Duelve una lista con la suma de los valores de cada columna
    return add_columns


#Flujo para interactuar las funciones con el usuario 
while True:
    
    try:
        # Obtener el valor suministrado por el usuario 
        user_input = input("Ingresa un número para el tamaño de la matriz")
        
        # Pasar la entrada a un dato tipo number
        matriz_size = int(user_input)

        # validar que el numero ingresado sea positivo y mayor a cero 
        if matriz_size > 0:

            print(f"La matriz tendra un tamaño de: {matriz_size}x{matriz_size}")
            # Variable que guardara las filas y columnas 
            matriz = []

            # Un ciclo para crear las filas
            for row_size in range(matriz_size):

                row = []
                # Un ciclo para agregar los valores de cada columna dentro de la fila
                for column_size in range(matriz_size):
                    random_number = random.randint( 0,9 )
                    row.append( random_number )
                # Agregar la fila con sus valores dentro de la matriz
                matriz.append(row)

            # Cliclo para imprimir los valores de la matriz
            for row in matriz:
                print(row)    

            # Variable que guarda el resultado de la funcion que devuelve la suma de las filas
            rows_total = get_sum_rows(matriz)   
            print("------------------------------")
            print(f"La suma de las filas:\n{rows_total}")

            # Variable en la que se guarda el resultado de la funcion que suma las colummnas
            columns_total = get_sum_columns(matriz)
            print("------------------------------")
            print(f"La suma de las columnas:\n{columns_total}")
        
        else:
            print("Debes ingresar un número mayor a cero")
        
    except ValueError:

        print("Debes ingresar solo números")


