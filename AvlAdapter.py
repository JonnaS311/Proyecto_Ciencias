import Avl


class AvlAdapter:
    def __init__(self):
        self.avl = Avl.Avl()

    def insertar(self,value):
        self.avl.insertar(value,self.avl.getRaiz())

    def buscar(self,value):
        return self.avl.buscar(value,self.avl.getRaiz())

    def eliminar(self,value):
        self.avl.eliminar(self.avl.buscar(value,self.getRaiz()))

    def getNivel(self,value):
       return self.avl.getAltura(self.avl.buscar(value,self.avl.getRaiz()))

    def preorden(self)->list:
        return self.avl.preorden(self.avl.getRaiz())

    def postorden(self)->list:
        return self.avl.postorden(self.avl.getRaiz())

    def inorden(self)->list:
        return self.avl.inorden(self.avl.getRaiz())


    def getRaiz(self):
        return self.avl.getRaiz()