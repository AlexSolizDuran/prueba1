from miweb.nodo import nodo

class arbol:
    def __init__(self,dato):
        self.raiz=nodo(dato)

    def __agregar_recur(self,nodo,dato):
        if dato<nodo.dato:
            if nodo.izq is None:
                nodo.izq = nodo(dato)
            else:
                self.__agregar_recur(nodo.izq,dato)
        else:
            if nodo.der is None:
                nodo.der = nodo(dato)
            else:
                self.__agregar_recur(nodo.der,dato)
    
    def __inorden_recursivo(self,nodo):
        if nodo is not None:
            self.__inorden_recursivo(nodo.izq)
            print(nodo.dato,end=", ")
            self.__inorden_recursivo(nodo.der)

    def __preorden_recursivo(self,nodo):
        if nodo is not None:
            print(nodo.dato,end=", ")
            self.__preorden_recursivo(nodo.izq)
            self.__preorden_recursivo(nodo.der)

    def __postorden_recursivo(self,nodo):
        if nodo is not None:
            self.__postorden_recursivo(nodo.izq)
            self.__postorden_recursivo(nodo.der)
            print(nodo.dato,end=", ")