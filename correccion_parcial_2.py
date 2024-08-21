#desarrollar un programa que determine si en una lista no existen elementos repetido

def elementos_repetidos(lista):
    
    a = set(lista)
    
    
    if len(lista) != len(a):
        
        return "Existen elemtos repetidos"
    
    else:
        
        return "No existen elemtos repetidos"


a = [1,2,3,4,5,5]

print(elementos_repetidos(a))


#desarrollar un programa que deteremine si en una lista se encuentra una cadena de caracteres con dos o mas vocales. sila cadena existe debe imprimirla y si no existe bebe imprimir "no existe"

def contar_vocales(lista):
    
    for cadena in lista:
    
        if cadena.count("a") + cadena.count("e") + cadena.count("i") + cadena.count("o") + cadena.count("u") >= 2:
        
             print(f"La cadena {cadena} tiene dos o más vocales")
    
    else:
        
        print("No existe")
        
lista = ["perro", "mil", "si"]

contar_vocales(lista)

#desarrollar un programa que dadas dos listas determine que elemento tiene la primera lista que no tenga la segunda lista

def elementos_unicos(lis1, lis2):
  
    c2 = set(lis2)
    
    uni = [i for i in lis1 if i not in c2]
    
    return print(f"los elementos que no están en la segunda lista: {uni}")


lista = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

elementos_unicos(lista, lista2)

#desarrollar un algoritmo que calcule el promedio de un arreglo de reales

def promedio_reales(lis):
    
    s = 0
    
    for i in lis:
        
        s += i
        
    print("el promedio del arreglo es", s/len(lis))
    

a = [1 ,2 ,3 ,4 ,5]
    
promedio_reales(a)   

#desarrollar un algoritmo que determine la mediana de un arreglo de enteros.

def mediana_arreglo(a):
    
    
    print("la mediana del arreglo es:", int((len(a)+1)/2)) 
    

h = [1,2,3,4,5,6,7,8,9,10,11]

mediana_arreglo(h)


