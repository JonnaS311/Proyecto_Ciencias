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
            self.isBalanceable = True
            return nodoF
        else:
            if value <= nodo.getValue():
                tmp = self.insertar(value, nodo.getLeft())
                if tmp is not None:
                    nodo.setLeft(tmp)
                    nodo.getLeft().setParent(nodo)
                    if self.isBalanceable:
                        self._FactorEquilibrio(nodo.getLeft())
                        self.isBalanceable = False
            else:
                tmp = self.insertar(value, nodo.getRight())
                if tmp is not None:
                    nodo.setRight(tmp)
                    nodo.getRight().setParent(nodo)
                    if self.isBalanceable:
                        self._FactorEquilibrio(nodo.getRight())
                        self.isBalanceable = False
            if self.isBalanceable:
                return nodo
            return

    def eliminar(self, raiz):
            # Eliminación de un Nodo hoja
            if raiz.getLeft() is None and raiz.getRight() is None:
                if raiz.getParent() is not None:
                    tmp = raiz.getParent()
                    if raiz.getParent().getLeft() == raiz: raiz.getParent().setLeft(None)
                    else: raiz.getParent().setRight(None)
                    self._FactorEquilibrio(tmp)
                return
            else:
                if raiz.getLeft() is not None and raiz.getRight() is None:
                    # si solo tiene hijo izquierdo
                    tmp = raiz.getLeft()
                    if raiz.getParent().getLeft() == raiz:
                        raiz.getParent().setLeft(raiz.getLeft())
                        raiz.getLeft().setParent(raiz.getParent())
                    else:
                        raiz.getParent().setRight(raiz.getLeft())
                        raiz.getLeft().setParent(raiz.getParent())
                    self._FactorEquilibrio(tmp)
                    return
                elif raiz.getLeft() is None and raiz.getRight() is not None:
                    # si solo tiene hijo derecho
                    tmp = raiz.getRight()
                    if raiz.getParent().getLeft() == raiz:
                        raiz.getParent().setLeft(raiz.getRight())
                        raiz.getRight().setParent(raiz.getParent())
                    else:
                        raiz.getParent().setRight(raiz.getRight())
                        raiz.getRight().setParent(raiz.getParent())
                    self._FactorEquilibrio(tmp)
                    return
                else:
                    # tiene dos hijos
                    candidato = raiz.getLeft()
                    notRight = False
                    tmp = None
                    while candidato.getRight() is not None:
                        candidato = candidato.getRight()
                        notRight = True
                        tmp = candidato.getParent()
                    if tmp is None:
                        tmp = candidato
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
                    self._FactorEquilibrio(tmp)
                    return

    def _FactorEquilibrio(self, nodo):
        if nodo.getRight() is not None and nodo.getLeft() is None:
            nodo.setBalanceF(self.getAltura(nodo.getRight()))
        elif  nodo.getRight() is None and nodo.getLeft() is not None:
            nodo.setBalanceF(-self.getAltura(nodo.getLeft()))
        elif  nodo.getRight() is not None and nodo.getLeft() is not None:
            nodo.setBalanceF(self.getAltura(nodo.getRight())-self.getAltura(nodo.getLeft()))
        else:
            nodo.setBalanceF(0)

        if nodo.getBalanceF() == 2 or nodo.getBalanceF() == -2:
            isBalanceado =  self.balancear(nodo)
            if isBalanceado == False:
                if nodo.getLeft() is None:
                    self.rotacionSI(nodo)
                elif nodo.getRight() is None:
                    self.rotacionSD(nodo)
                elif self.getAltura(nodo.getLeft()) > self.getAltura(nodo.getRight()):
                    self.rotacionSD(nodo)
                else:
                    self.rotacionSI(nodo)
        else:
            if nodo.getParent() is not None:
                return self._FactorEquilibrio(nodo.getParent())


    def balancear(self, nodo):
        if nodo.getBalanceF() == -2 and nodo.getLeft().getBalanceF() == -1:
            self.rotacionSD(nodo)
            return True
        elif nodo.getBalanceF() == 2 and nodo.getRight().getBalanceF() == 1:
            self.rotacionSI(nodo)
            return True
        elif nodo.getBalanceF() == -2 and nodo.getLeft().getBalanceF() == 1:
            self.rotacionDI(nodo)
            return True
        elif nodo.getBalanceF() == 2 and nodo.getRight().getBalanceF() == -1:
            self.rotacionDD(nodo)
            return True
        return False

    def rotacionSI(self, nodo):
        iRaiz = nodo.getRight()
        if nodo.getParent() is not None:
            if nodo.getParent().getLeft() == nodo:
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
        if iRaiz.getLeft() is not None:
            iRaiz.getLeft().setParent(nodo)
        iRaiz.setLeft(nodo)
        nodo.setBalanceF(nodo.getBalanceF() - 1 - max(iRaiz.getBalanceF(), 0))
        iRaiz.setBalanceF(iRaiz.getBalanceF() - 1 + min(nodo.getBalanceF(), 0))

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
        nodo.setBalanceF(nodo.getBalanceF() + 1 - min(dRaiz.getBalanceF(), 0))
        dRaiz.setBalanceF(dRaiz.getBalanceF() + 1 + max(nodo.getBalanceF(), 0))

    def rotacionDD(self, nodo):
        iRaiz = nodo.getRight().getLeft()
        # Cambio de hijos
        nodo.getRight().setLeft(iRaiz.getRight())
        if iRaiz.getRight() is not None:
            iRaiz.getRight().setParent(nodo.getRight())

        iRaiz.setRight(nodo.getRight())
        nodo.getRight().setParent(iRaiz)

        nodo.setRight(iRaiz)
        iRaiz.setParent(nodo)
        iRaiz.getRight().setBalanceF(iRaiz.getRight().getBalanceF() + 1 - min(iRaiz.getBalanceF(), 0))
        iRaiz.setBalanceF(iRaiz.getBalanceF() + 1 + max(iRaiz.getRight().getBalanceF(), 0))
        self.rotacionSI(nodo)

    def rotacionDI(self, nodo):
        dRaiz = nodo.getLeft().getRight()
        # Cambio hijos
        nodo.getLeft().setRight(dRaiz.getLeft())
        if dRaiz.getLeft() is not None:
            dRaiz.getLeft().setParent(nodo.getLeft())

        dRaiz.setLeft(nodo.getLeft())
        nodo.getLeft().setParent(dRaiz)

        nodo.setLeft(dRaiz)
        dRaiz.setParent(nodo)
        dRaiz.getLeft().setBalanceF(dRaiz.getLeft().getBalanceF() - 1 - max(dRaiz.getBalanceF(), 0))
        dRaiz.setBalanceF(dRaiz.getBalanceF() - 1 + min(dRaiz.getLeft().getBalanceF(), 0))
        self.rotacionSD(nodo)
