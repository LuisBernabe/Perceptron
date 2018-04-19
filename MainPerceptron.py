import Perceptron

p= Perceptron.perceptron(3)
testPrueba=[[0,0,0],[0,0,1],[1,0,1],[1,1,1]]
test=[[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]]
valAnd=[0,0,0,0,0,0,0,1]
valOr=[0,1,1,1,1,1,1,1]

opcion=input("Que compuerta desea probar, And u Or? [A|O]\n")

if opcion == 'A':
    p.entrenamiento(test,valAnd)
elif opcion=='O':
    p.entrenamiento(test,valOr)
print ("Entrenamiento realizado")

print ("\n******************TESTING*******************")
res=0
tst=[]
for i in range(len(test)):
    res=p.guess(test[i])
    tst=test[i]
    print ("Entrada ",test[i]," Salida: "+str(res) )

entradass=input("Ingresa los tres valores correspondientes en el siguiente orden: [x1,x2,x3] (los valores son 0 o 1)\n")
entradas=[float (i) for i in entradass.split(',')]
print (entradas)
print ("\n******************PRUEBA INTERACTIVA*******************")
print ("para la entrada ", entradas," el resultado es: ",p.guess(entradas) )
