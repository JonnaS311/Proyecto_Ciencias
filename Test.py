import AvlAdapter

if __name__ == '__main__':
    arbol = AvlAdapter.AvlAdapter()
    arbol.insertar(15)
    arbol.insertar(9)
    arbol.insertar(5)
    arbol.insertar(10)
    arbol.insertar(3)
    arbol.insertar(8)
    arbol.insertar(2)
    arbol.insertar(20)
    arbol.insertar(6)
    arbol.insertar(11)
    arbol.insertar(18)
    arbol.insertar(22)

    arbol.eliminar(9)

    arbol.insertar(16)
    arbol.insertar(17)
    arbol.insertar(19)
    arbol.insertar(26)
    arbol.insertar(32)
    arbol.insertar(50)
    print(arbol.preorden())

    arbol.eliminar(5)
    arbol.eliminar(20)
    arbol.eliminar(15)
    arbol.eliminar(11)
    arbol.eliminar(8)
    arbol.eliminar(50)

    arbol.eliminar(32)
    arbol.eliminar(18)
    arbol.eliminar(17)
    arbol.eliminar(16)
    arbol.eliminar(10)
    arbol.eliminar(6)
    arbol.eliminar(3)
    arbol.eliminar(22)
    arbol.eliminar(19)
    arbol.eliminar(2)
    arbol.eliminar(26)
    print(arbol.preorden())