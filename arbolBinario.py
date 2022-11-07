import nodo


class ArbolBinario:

    def __init__(self):
        self.raiz = None

    @staticmethod
    def agregarNodo(value):
        return nodo.Nodo(value)

    def insertar(self, value, nodo):
        if self.raiz is None:
            self.raiz = self.agregarNodo(value)
            return
        if nodo is None:
            return self.agregarNodo(value)
        else:
            if value <= nodo.getValue():
                nodo.setLeft(self.insertar(value, nodo.getLeft()))
                nodo.getLeft().setParent(nodo)
            else:
                nodo.setRight(self.insertar(value, nodo.getRight()))
                nodo.getRight().setParent(nodo)
            return nodo

    def buscar(self, index, raiz):
        if raiz is None:
            return
        else:
            if index == raiz.getValue():
                return raiz
            elif index < raiz.getValue():
                return self.buscar(index, raiz.getLeft())
            else:
                return self.buscar(index, raiz.getRight())

    def eliminar(self, nodo, raiz: nodo.Nodo):
        if nodo == raiz:
            # Eliminación de un Nodo hoja
            if raiz.getLeft() is None and raiz.getRight() is None:
                if raiz.getParent().getLeft() == raiz:
                    raiz.getParent().setLeft(None)
                else:
                    raiz.getParent().setRight(None)
                return
            else:
                if raiz.getLeft() is not None and raiz.getRight() is None:
                    # si solo tiene hijo izquierdo
                    if raiz.getParent().getLeft() == raiz:
                        raiz.getParent().setLeft(raiz.getLeft())
                        raiz.getLeft().setParent(raiz.getParent())
                    else:
                        raiz.getParent().setRight(raiz.getLeft())
                        raiz.getLeft().setParent(raiz.getParent())
                    return
                elif raiz.getLeft() is None and raiz.getRight() is not None:
                    # si solo tiene hijo derecho
                    if raiz.getParent().getLeft() == raiz:
                        raiz.getParent().setLeft(raiz.getRight())
                        raiz.getRight().setParent(raiz.getParent())
                    else:
                        raiz.getParent().setRight(raiz.getRight())
                        raiz.getRight().setParent(raiz.getParent())
                    return
                else:
                    # tiene dos hijos
                    candidato = raiz.getLeft()
                    while candidato.getRight() is not None:
                        candidato = candidato.getRight()
                    raiz.getRight().setParent(candidato)
                    raiz.getLeft().setParent(candidato)
                    candidato.getParent().setRight(candidato.getLeft())
                    candidato.setLeft(raiz.getLeft())
                    candidato.setRight(raiz.getRight())
                    if raiz.getParent() is not None:
                        if raiz.getParent().getLeft() == raiz:
                            raiz.getParent().setLeft(candidato)
                        else:
                            raiz.getParent().setRight(candidato)
                    return
        elif raiz is not None and nodo is not None:
            if nodo.getValue() <= raiz.getValue():
                self.eliminar(nodo, raiz.getLeft())
            else:
                self.eliminar(nodo, raiz.getRight())
        return

    def getRaiz(self):
        return self.raiz
