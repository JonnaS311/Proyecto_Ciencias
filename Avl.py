import arbolBinario as ab
class Avl(ab.ArbolBinario):
    # TODO: esta clase debe heredar CORRECTAMENTE de arbolBinario
    def __init__(self):
        pass

    def rotacionSI(self,nodo):
        iRaiz = nodo.getRight()
        if nodo.getParent() is not None:
            if nodo.getParent.getLeft() == nodo:
                nodo.getParent().setLeft(iRaiz)
                iRaiz.setParent(nodo.getParent())
            else:
                nodo.getParent().setRight(iRaiz)
                iRaiz.setParent(nodo.getParent())
        else:
            self.raiz = iRaiz
        nodo.setRight(iRaiz.getLeft())
        iRaiz.setLeft(nodo)

    def rotacionSD(self,nodo):
        dRaiz = nodo.getLeft()
        if nodo.getParent() is not None:
            if nodo.getParent().getLeft() == nodo:
                nodo.getParent().setLeft(dRaiz)
                dRaiz.setParent(nodo.getParent())
            else:
                nodo.getParent().setRight(dRaiz)
                dRaiz.setParent(nodo.getParent())
        else:
            self.raiz = dRaiz
        nodo.setLeft(dRaiz.getRight())
        dRaiz.setRight(nodo)

    def rotaciónDI(self,nodo):
        iRaiz = nodo.getRight().getLeft()
        # Cambio de hijos
        nodo.getRight().setLeft(iRaiz.getRight())
        if iRaiz.getRight() is not None:
            iRaiz.getRight().setParent(nodo.getRight())

        iRaiz.setRight(nodo.getRight())
        nodo.getRight().setParent(iRaiz)

        nodo.setRight(iRaiz)
        iRaiz.setParent(nodo)
        self.rotacionSI(nodo)

    def rotacionDD(self,nodo):
        dRaiz= nodo.getLeft().getRight()
        # Cambio hijos
        nodo.getLeft().setRight(dRaiz.getLeft())
        if dRaiz.getLeft() is not None:
            dRaiz.getLeft().setParent(nodo.getLeft())

        dRaiz.setLeft(nodo.getLeft())
        nodo.getLeft().setParent(dRaiz)

        nodo.setLeft(dRaiz)
        dRaiz.setParent(nodo)
        self.rotacionSD(nodo)
        pass