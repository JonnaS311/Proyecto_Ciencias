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
            nodoF = self.agregarNodo(value)
            return nodoF
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

    def eliminar(self, raiz):
        # Eliminación de un Nodo hoja
        if raiz.getLeft() is None and raiz.getRight() is None:
            if raiz.getParent() is not None:
                if raiz.getParent().getLeft() == raiz:
                    raiz.getParent().setLeft(None)
                else:
                    raiz.getParent().setRight(None)
            else:
                self.setRaiz(None)
            return
        else:
            if raiz.getLeft() is not None and raiz.getRight() is None:
                # si solo tiene hijo izquierdo
                if raiz.getParent() is not None:
                    if raiz.getParent().getLeft() == raiz:
                        raiz.getParent().setLeft(raiz.getLeft())
                        raiz.getLeft().setParent(raiz.getParent())
                    else:
                        raiz.getParent().setRight(raiz.getLeft())
                        raiz.getLeft().setParent(raiz.getParent())
                else:
                    raiz.getLeft().setParent(None)
                    self.setRaiz(raiz.getLeft())
                return
            elif raiz.getLeft() is None and raiz.getRight() is not None:
                # si solo tiene hijo derecho
                if raiz.getParent() is not None:
                    if raiz.getParent().getLeft() == raiz:
                        raiz.getParent().setLeft(raiz.getRight())
                        raiz.getRight().setParent(raiz.getParent())
                    else:
                        raiz.getParent().setRight(raiz.getRight())
                        raiz.getRight().setParent(raiz.getParent())
                else:
                    raiz.getRight().setParent(None)
                    self.setRaiz(raiz.getRight())
                return
            else:
                # tiene dos hijos
                candidato = raiz.getLeft()
                notRight = False
                while candidato.getRight() is not None:
                    candidato = candidato.getRight()
                    notRight = True
                raiz.getRight().setParent(candidato)
                raiz.getLeft().setParent(candidato)
                if candidato.getLeft() is not None:
                    candidato.getParent().setRight(candidato.getLeft())
                    candidato.getLeft().setParent(candidato.getParent())
                else:
                    candidato.getParent().setRight(None)
                if notRight:
                    candidato.setLeft(raiz.getLeft())
                candidato.setRight(raiz.getRight())
                if raiz.getParent() is not None:
                    candidato.setParent(raiz.getParent())
                    if raiz.getParent().getLeft() == raiz:
                        raiz.getParent().setLeft(candidato)
                    else:
                        raiz.getParent().setRight(candidato)
                else:
                    self.raiz = candidato
                    candidato.setParent(None)
                return

    def getAltura(self,nodo,nivel=1):
        nivelL,nivelR = 0,0
        if nodo.getLeft() is not None:
            nivelL = self.getAltura(nodo.getLeft(),nivel+1)
        if nodo.getRight() is not None:
            nivelR = self.getAltura(nodo.getRight(),nivel+1)

        if nivelL > nivelR:
            return nivelL
        elif nivelR > nivelL:
            return nivelR
        elif nivelL == nivelR and nivelL != 0:
            return nivelL
        else:
            return nivel

    def preorden(self, nodo, lista=None) -> list:
        if lista is None:
            lista = []
        if nodo is not None:
            lista.append(nodo.getValue())
            if nodo.getLeft() is not None: self.preorden(nodo.getLeft(), lista)
            if nodo.getRight() is not None: self.preorden(nodo.getRight(), lista)
        return lista

    def inorden(self, nodo, lista=None) -> list:
        if lista is None:
            lista = []
        if nodo is not None:
            if nodo.getLeft() is not None:
                self.inorden(nodo.getLeft(), lista)
                lista.append(nodo.getValue())
                if nodo.getRight() is not None:
                    self.inorden(nodo.getRight(), lista)
            else:
                lista.append(nodo.getValue())
                if nodo.getRight() is not None:
                    self.inorden(nodo.getRight(), lista)

        return lista

    def postorden(self, nodo, lista=None) -> list:
        if lista is None:
            lista = []
        if nodo is not None:
            if nodo.getLeft() is not None: self.postorden(nodo.getLeft(), lista)
            if nodo.getRight() is not None: self.postorden(nodo.getRight(), lista)
            lista.append(nodo.getValue())
        return lista

    def getRaiz(self):
        return self.raiz

    def setRaiz(self, raiz):
        self.raiz = raiz
