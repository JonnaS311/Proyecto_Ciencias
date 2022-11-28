from Avl import Avl
from arbolBinario import ArbolBinario

if __name__ == '__main__':
    arbol = Avl()
    arbol.insertar(15,arbol.getRaiz())
    #arbol.insertar(20,arbol.getRaiz())
    arbol.insertar(9,arbol.getRaiz())
    arbol.insertar(5,arbol.getRaiz())
    #arbol.insertar(10,arbol.getRaiz())
    #arbol.insertar(14,arbol.getRaiz())
    #arbol.insertar(13, arbol.getRaiz())
    #arbol.insertar(17, arbol.getRaiz())
    #arbol.insertar(64, arbol.getRaiz())
    #arbol.insertar(26, arbol.getRaiz())
    #arbol.insertar(72, arbol.getRaiz())

    #arbol.rotacionSD(arbol.getRaiz())
    print(arbol.buscar(15,arbol.getRaiz()).getBalanceF())
    print(arbol.inorden(arbol.getRaiz()))
    print(arbol.preorden(arbol.getRaiz()))
    print(arbol.postorden(arbol.getRaiz()))