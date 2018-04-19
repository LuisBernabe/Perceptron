import numpy as  np
import random

class perceptron:
    #global weights;

    def __init__(self,NumEntradas):
        """
                NumEntradas: para genererar los pesos aleatorios
        """
        self.weights=list(random.uniform(-0.5,0.5) for i in range(NumEntradas+1))
        self.lr=0.3 #taza de aprendizaje
        self.umbral= random.uniform(-0.5,0.5)
        print ("\nPesos aleatorios:", self.weights)



    def escalon(self,n):
    	if n >= 0:
    		return 1
    	else:
    		return 0

    def guess(self,inputs):
        """
        funcion que se encarga de realiza la suma y aplicar la funcion de activacion
        return      el valor de la funcion de activacion
        """
        sum=0.00
        for i in range(len(self.weights)-1):
            sum+=self.weights[i]*inputs[i]#-self.umbral
        sum+=self.weights[i+1]
        output= self.escalon(sum)
        return output


    def corrige(self, inputs, target):
        """
        entrenamiento de nuestro perceptron. Se ncarga de coregir lo valores de error

            inputs      es una tupla que es un ejemplar de la forma (x1,x2....,xn)
            target      target es el objetivo esperado en base a nuestra entrada
        """
        aprox=self.guess(inputs) #obtengo el valor de la funcion de activacion
        error=target-aprox #obtengo el error

        for i in range(len(self.weights)-1):
            self.weights[i]=self.weights[i] + (error * inputs[i] * self.lr)
        self.weights[i+1]=self.weights[i+1]+(error * self.lr)
        print ("\n")



    def entrenamiento(self,conj,valores):
        """
            Metodo que revisa si los valores de las entradas coinciden con las dadas en el entrenamiento
            y coincide con el resultado de la funcion escalon de estas entradas, de lo contrario
            manda a corregir los valores.

            conj conjunto de todas las entradas para entrenar
            valores conjunto de los valores dados por cada entrada
        """
        i=0
        while i < len(conj):
            estimado=self.guess(conj[i])
            if (estimado != valores[i]):
                print ("\nEl valor esperado de ",conj[i]," es: ",valores[i],"y se obtuvo",estimado)
                print ("******CORRIGE PESOS***********\npesos anteriores:",self.weights)
                self.corrige(conj[i],valores[i])
                print ("Pesos actuales",self.weights,"\n******************************\n")
                i= - 1
            else:
                print ("Se obtuvo el valor deseado de la entrada",conj[i],"con salida",valores[i])

            i=i+1
