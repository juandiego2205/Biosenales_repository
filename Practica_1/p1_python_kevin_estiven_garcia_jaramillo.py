# -*- coding: utf-8 -*-
"""P1_Python_Kevin_Estiven_Garcia_Jaramillo.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ULxw3zprOh7_kYwDM6KG07gNAh9l8pHz

#**Practica_1**

## **A) Creación de Vectores:**
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
a=np.array([3.1,1,-0.5,-3.2,6])
b=np.array([1,3,2.2,5.1,1])
print("el vector a es:\n" +str(a));
print("\nel vector b es:\n" +str(b));

"""##**B) Producto Escalar a.b**
se implementa una función de la libreria de numpy llamada numpy.dot, que permite la multiplicación escalar entre dos arreglos, en este caso vectores

"""

esc=np.dot(a,b)
print("el resultado de la multiplicación escalar es\n"+str(esc))

"""##**C) Multiplicación Punto a Punto de a.b:**

"""

C=a*b
print(C)

"""##**D) Construcción de matriz**"""

A=np.array([[2,-1,-3],[4,1.5,-2.5],[7.3,-0.9,0.2]])
print(A)

"""##**E) Transpuesta de la Matriz**"""

AT=A.transpose()
print(AT)

"""## **F) Comandos de Numpy:**
**Numpy.ones (shape, dtype=None, order='C', *, device=None, like=None)**

crea un arreglo, vector o matriz unicamente de unos
- shape: forma del arreglo
- dtype: tipo de arreglo
"""

F1=np.ones((5,),dtype=int)
print(F1)

"""**numpy.round(a, decimals=0, out=None)**
- a: dato de entrada
- decimals: Número de decimales a las que se redondeará (valor predeterminado: 0). Si el número de decimales es negativo, especifica el número de posiciones a la izquierda del punto decimal.

"""

F2=np.round(115.3456,-2)
print(F2)
F3=np.round(115.3456,2)
print(F3)

"""**numpy.ceil(x):** busca el entero mas cercano por arriba es decir si el numero es 1.1, su valor seria el 2"""

ac=np.ceil(a)
print("Vector anterior: "+str(a))
print("Vector redondeado: "+str(ac))

"""**numpy.floor(x):** busca el entero mas cercano por abajo es decir si el numero es 1.1, su valor seria el 1"""

af=np.floor(a)
print("Vector anterior: "+str(a))
print("Vector redondeado: "+str(af))

"""##**G) Acceso a la Primera fila y tercera columna de la matriz**"""

ANew=A[0][2]
print(ANew)

"""##**H) Segunda Fila de matriz**"""

ANew2=A[1]
print(ANew2)

"""##**I) Dimensiones de Matriz**"""

Dim=np.ndim(A)
print(Dim)

"""##**J) Primera Función**"""

n=np.arange(0,101)
Y=np.sin(np.pi*0.12*n)

"""##**K) Segunda Función**"""

Y2=np.cos(2*np.pi*0.03*n)

"""##**L) Suma y Producto de Funciones**"""

S=Y+Y2
T=Y*Y2

"""##**M) Grafica de Funciones Y y Y2**"""

plt.figure()
plt.plot(Y,color="red")
plt.plot(Y2,color="blue")
plt.legend(["Y","Y2"])
plt.grid()
plt.title("Gráficas de Y y Y2")
plt.ylabel("Y[n]")
plt.xlabel("[n]")
plt.show()

"""##**N) Grafica de Suma (s[n]) y producto (t[n])**"""

plt.figure()
plt.plot(S,color="green")
plt.plot(T,color="orange")
plt.legend(["s","t"])
plt.grid()
plt.title("Gráficas de s y t")
plt.ylabel("Y[n]")
plt.xlabel("[n]")
plt.show()

"""##**Reto**"""

notas=[]
nombre=input("Ingrese el nombre del alumno: ")
numNotas=int(input("Ingrese el numero de notas: "))
for i in range(numNotas):
  nota=float(input("Ingrese la nota: "))
  notas.append(nota)
nots=np.array(notas)
estudiante={nombre:nots}
def notasCurso (estudiante):
  desviacion=estudiante[nombre].std()
  media=estudiante[nombre].mean()
  maximo=estudiante[nombre].max()
  minimo=estudiante[nombre].min()
  datos=[minimo,maximo,media,desviacion]
  return datos
indice=["Minimo","Maximo","Media","Desviación"]
informacion=pd.Series(notasCurso(estudiante),index=indice)
df = informacion.to_frame(name=nombre)
info2 =df.style.background_gradient(cmap="Blues")
print("")
info2