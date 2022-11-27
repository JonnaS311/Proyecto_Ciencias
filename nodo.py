class Nodo:

    def __init__(self, value):
        self.__value = value
        self.__right = None
        self.__left = None
        self.__parent = None
        self.__balanceF = 0

    def setParent(self,nodo):
        self.__parent = nodo

    def getParent(self):
        return self.__parent

    def setRight(self,nodo):
        self.__right = nodo

    def getRight(self):
        return self.__right

    def setLeft(self,nodo):
        self.__left = nodo

    def getLeft(self):
        return self.__left

    def getValue(self):
        return self.__value

    def getBalanceF(self):
        return self.__balanceF

    def setBalanceF(self,num):
        self.__balanceF = num