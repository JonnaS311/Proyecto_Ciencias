from Avl import Avl
from arbolBinario import ArbolBinario

if __name__ == '__main__':
    arbol = ArbolBinario()
    arbol.insertar(20,arbol.getRaiz())
    #arbol.insertar(40,arbol.getRaiz())
    arbol.insertar(10,arbol.getRaiz())
    arbol.insertar(5,arbol.getRaiz())
    arbol.insertar(15,arbol.getRaiz())
    arbol.insertar(13, arbol.getRaiz())
    #arbol.insertar(8, arbol.getRaiz())
    #arbol.insertar(12, arbol.getRaiz())
    #arbol.insertar(11, arbol.getRaiz())
    #arbol.insertar(15, arbol.getRaiz())
    #arbol.insertar(13, arbol.getRaiz())
    #arbol.insertar(35, arbol.getRaiz())
    #arbol.insertar(42, arbol.getRaiz())
    #arbol.insertar(6, arbol.getRaiz())

    arbol.balanceo(arbol.buscar(20,arbol.getRaiz()))
    print(arbol.getRaiz().getLeft().getRight().getParent().getValue())