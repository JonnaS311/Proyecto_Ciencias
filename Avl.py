import arbolBinario as Ab


class Avl(Ab.ArbolBinario):

    def __init__(self):
        super().__init__()
        self.isBalanceable = False

    def insertar(self, value, nodo):
        if self.raiz is None:
            self.raiz = self.agregarNodo(value)
            return
        if nodo is None:
            nodoF = self.agregarNodo(value)
            # true
            self.isBalanceable = True
            return nodoF
        else:
            if value <= nodo.getValue():
                tmp = self.insertar(value, nodo.getLeft())
                if tmp is not None:
                    nodo.setLeft(tmp)
                    nodo.getLeft().setParent(nodo)
                    if self.isBalanceable:
                        self.FactorEquilibrio(nodo.getLeft())
                        self.isBalanceable = False
            else:
                tmp = self.insertar(value, nodo.getRight())
                if tmp is not None:
                    nodo.setRight(tmp)
                    nodo.getRight().setParent(nodo)
                    if self.isBalanceable:
                        self.FactorEquilibrio(nodo.getRight())
                        self.isBalanceable = False
            if self.isBalanceable:
                return nodo
            return

    def FactorEquilibrio(self, nodo):
        if nodo.getBalanceF() > 1 or nodo.getBalanceF() < -1:
            self.balancear(nodo)
            return
        if nodo.getParent() is not None:
            if nodo.getParent().getLeft() == nodo:
                nodo.getParent().setBalanceF(nodo.getParent().getBalanceF() - 1)
            elif nodo.getParent().getRight() == nodo:
                nodo.getParent().setBalanceF(nodo.getParent().getBalanceF() + 1)
        if nodo.getParent() is not None and nodo.getParent().getBalanceF() != 0:
            self.FactorEquilibrio(nodo.getParent())

    def balancear(self, nodo):
        if nodo.getBalanceF() == -2 and nodo.getLeft().getBalanceF() == -1:
            self.rotacionSD(nodo)
        elif nodo.getBalanceF() == 2 and nodo.getRight().getBalanceF() == 1:
            self.rotacionSI(nodo)
        elif nodo.getBalanceF() == -2 and nodo.getRight().getBalanceF() == 1:
            self.rotacionDI(nodo)
        elif nodo.getBalanceF() == 2 and nodo.getRight().getBalanceF() == -1:
            self.rotacionDD(nodo)

    def rotacionSI(self, nodo):
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
            iRaiz.setParent(None)
        nodo.setParent(iRaiz)
        nodo.setRight(iRaiz.getLeft())
        if iRaiz.getRight() is not None:
            iRaiz.getRight().setParent(nodo)
        iRaiz.setLeft(nodo)

    def rotacionSD(self, nodo):
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
            dRaiz.setParent(None)
        nodo.setParent(dRaiz)
        nodo.setLeft(dRaiz.getRight())
        if dRaiz.getRight() is not None:
            dRaiz.getRight().setParent(nodo)
        dRaiz.setRight(nodo)

    def rotacionDI(self, nodo):
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

    def rotacionDD(self, nodo):
        dRaiz = nodo.getLeft().getRight()
        # Cambio hijos
        nodo.getLeft().setRight(dRaiz.getLeft())
        if dRaiz.getLeft() is not None:
            dRaiz.getLeft().setParent(nodo.getLeft())

        dRaiz.setLeft(nodo.getLeft())
        nodo.getLeft().setParent(dRaiz)

        nodo.setLeft(dRaiz)
        dRaiz.setParent(nodo)
        self.rotacionSD(nodo)
