print("Se cuentan con 2 funciones: basic_ops y array_ops")
print("basic_ops(primer dato, segundo dato, operación)")
print("array_ops(primer array, segundo array, operación)")
print("Las operaciones se identificaran con un número")
print("Solo ingrese números enteros")
print("Solo ingrese números entre -127 y 127")
print(" Suma digite 1")
print(" Resta digite 2")
print(" AND digite 3")
print(" OR digite 4")
# Metodo basic_ops


def basic_ops(primer_dato, segundo_dato, operación):
    # Metodo basic_ops
    # A continuacion se pondran los posibles errores de este metodo
    # Si los números ingresados al método no son entero
    if isinstance(primer_dato, int) is False:
        # revisa que el primer dato sea entero
        return "Error dato no es un entero"
    if isinstance(segundo_dato, int) is False:
        # revisa que el primer dato sea entero
        return "Error dato no es un entero"
    # Si los números ingresados son mayores a 127, o menores a -127
    if ((primer_dato > 127) | (primer_dato < -127)):
        # revisa que el primer dato este entre 127 y -127
        return "Error dato fuera de rango"
    if ((segundo_dato > 127) | (segundo_dato < -127)):
        # revisa que el primer dato este entre 127 y -127
        return "Error dato fuera de rango"
    # Si operacion invalida
    if ((operación != 1) & (operación != 2)):
        if ((operación != 3) & (operación != 4)):
            return "Error operación no válida"
    # A continuacion se llevara a cabo el calculo de las operaciones
    # en el caso de no existir un error
    if operación == 1:
        resultado = primer_dato + segundo_dato
    if operación == 2:
        resultado = primer_dato - segundo_dato
    if operación == 3:
        resultado = primer_dato & segundo_dato
    if operación == 4:
        resultado = primer_dato | segundo_dato
    return resultado
# Metodo array_ops


def array_ops(primer_array, segundo_array, operación):
    # definicion de variables requeridas para este metodo:
    tamaño1 = len(primer_array)
    # se obtiene el tamaño del primer array
    tamaño2 = len(segundo_array)
    # se obtiene el tamaño del segundo array
    i = 0
    # sera el contador para el ciclo while
    # Array de Salida
    array_final = []
    if (tamaño1 != tamaño2):
        # Comprueba si los array tienen el mismo tamaño para realizar
        # la operación
        return "Error el tamaño de los array son distintos"
    else:
        while i < tamaño1:
            # se tomaran los datos del array para realizar la operacion
            # requerida con el metodo basic_ops
            dato1 = primer_array[i]
            dato2 = segundo_array[i]
            # se llamara a la función basic_ops
            datofinal = basic_ops(dato1, dato2, operación)
            # verificar que dato final sea un número, ya que si esto no
            # se cumple la funcion basic ops debe dar un error.
            # por lo tanto si se genera un error el programa finalizara
            # en ese caso.
            if isinstance(datofinal, int) is False:
                return datofinal
            else:
                array_final.append(datofinal)
                # El dato obtenido se
                # introducira en el array final
                i = i + 1
                # se aumentara el contador para recorrer todas
                # las posiciones del array
        return array_final
