import numpy as  np
import random

class perceptron:
    #global weights;

    def __init__(self,NumEntradas):
        """
                NumEntradas: para genererar los pesos aleatorios
        """
        self.weights=list(random.uniform(-0.5,0.5) for i in range(NumEntradas))
        self.lr=0.3 #taza de aprendizaje
        self.umbral= random.uniform(-0.5,0.5)
        print "\nPesos aleatorios:"+ str(self.weights)



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
        for i in range(len(self.weights)):
            sum+=self.weights[i]*inputs[i]-self.umbral
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

        if(inputs[0] == 0 and target== 0 and error == 1):
             self.umbral = self.weights[0] + self.umbral
        elif (inputs[0] == 0 and target == 0 and error == -1):
            self.umbral = self.weights[0] - self.umbral
        elif(inputs[1] == 0 and target == 0 and error == 1):
            self.umbral = self.weights[1] + self.umbral
        elif (inputs[1] == 0 and target == 0 and error == -1):
            self.umbral = self.weights[1] - self.umbral
        elif(inputs[2] == 0 and target == 0 and error == 1):
             self.umbral = self.weights[2] + self.umbral
        elif (inputs[2] == 0 and target == 0 and error == -1):
            self.umbral = self.weights[2] - self.umbral


        for i in range(len(self.weights)):
            self.weights[i]=self.weights[i] + (error * inputs[i]) + self.lr

        print "\n"



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
            estimado=p.guess(conj[i])
            if (estimado != valores[i]):
                print "\nEl valor esperado de ",conj[i]," es: ",valores[i],"y se obtuvo",estimado
                print "******CORRIGE PESOS***********\npesos anteriores:",self.weights
                self.corrige(conj[i],valores[i])
                print "Pesos actuales",self.weights,"\n******************************\n"
                i= - 1
            else:
                print "Se obtuvo el valor deseado de la entrada",conj[i],"con salida",valores[i]

            i=i+1




p= perceptron(3)
testPrueba=[[0,0,0],[0,0,1],[1,0,1],[1,1,1]]
test=[[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]]
valAnd=[0,0,0,0,0,0,0,1]
valOr=[0,1,1,1,1,1,1,1]

opcion=raw_input("Que compuerta desea probar, And u Or? [A|O]\n")

if opcion == 'A':
    p.entrenamiento(test,valAnd)
elif opcion=='O':
    p.entrenamiento(test,valOr)
print "Entrenamiento realizado"

print "\n******************TESTING*******************"
res=0
tst=[]
for i in range(len(test)):
    res=p.guess(test[i])
    tst=test[i]
    print "Entrada ",test[i]," Salida: "+str(res)

entradas=input("Ingresa los tres valores correspondientes en el siguiente orden: [x1,x2,x3] (los valores son 0 o 1)\n")
print "\n******************PRUEBA INTERACTIVA*******************"
print "para la entrada ", list(entradas)," el resultado es: ",p.guess(list(entradas))
