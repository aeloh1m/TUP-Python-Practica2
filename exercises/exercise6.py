"""Type, Comprensión de Listas, Sorted y Filter."""

from re import I
from typing import List, Union


def numeros_al_final_basico(lista: List[Union[float, str]]) -> List[Union[float, str]]:  # noqa: E501
    """Toma una lista de enteros y strings y devuelve una lista con todos los
    elementos numéricos al final.

    Restricciones:
        - Utilizar un bucle FOR.
        - Utilizar la función type.
        - No utilizar índices.
    """
    newList = []

    for i in lista:
        if type(i) == int:
            newList.append(i)
        if type(i) == str:
            newList.insert(-6, i)
            
    return newList

print(numeros_al_final_basico([3, "a", 1, "b", 10, "j"]))

# NO MODIFICAR - INICIO
#assert numeros_al_final_basico([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]  # noqa: E501
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_comprension(lista: List[Union[float, str]]) -> List[Union[float, str]]:  # noqa: E501
    """Re-escribir utilizando comprensión de listas.

    Restricciones:
        - No utilizar bucles.
        - Utilizar dos comprensiones de listas.
    """
    newList = [i for i in lista if type(i) == str]
   
    newList_0 = [i for i in lista if type(i) == int]
    
    return newList + newList_0
    
print(numeros_al_final_comprension([3, "a", 1, "b", 10, "j"]))

# NO MODIFICAR - INICIO
assert numeros_al_final_comprension([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]  # noqa: E501
# NO MODIFICAR - FIN
