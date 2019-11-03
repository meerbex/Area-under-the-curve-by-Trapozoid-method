from matplotlib import pyplot as plt
import numpy as np

# Finding area
def trapozoidsum(function,n,a,b):
  summ = 0
  deltaX = (b-a)/float(n)
  for i in range(0,n):
    xi = a + i*deltaX
    xi_1 = a + (i+1)*deltaX
    summ += (function(xi)+function(xi_1))/2 * deltaX
  return(summ)

# Graphing
def graphing(function,n,a,b):
  x = np.linspace(a-2,b+2,100)
  ranged = np.linspace(a,b,100)
  plt.plot(x,function(x),color="blue", label= "x^2")
  deltaX = (b-a)/float(n)
  plt.fill_between(ranged, function(ranged), color='yellow', label = "Real-area")
  for i in range(0,n):
    xi = a + i*deltaX
    xi_1 = a + (i+1)*deltaX
    xaxis = [xi,xi, xi_1, xi_1]
    yaxis = [0,function(xi),function(xi_1),0]
    plt.plot(xaxis,yaxis, color="black")    
    x2axis = np.linspace(xi,xi_1,100)
    function2 = lambda s:(((function(xi) - function(xi_1))/(xi - xi_1))*(s - xi)) + function(xi)
    plt.plot(x2axis,function(x2axis), color="blue")
    plt.fill_between(x2axis, function(x2axis), function2(x2axis),  color="red") 
  plt.fill(0,function(0), color="red", label= "Error")  
  plt.title("Finding approximate area under the courve")
  plt.xlabel("X - axis")
  plt.ylabel("Y - axis")
  plt.legend()

  plt.show()


def function(x):
  return eval(expr)



expr = (input("Enter an expression "))
start = int(input("Enter a starting point "))
end = int(input("Enter an ending point "))
tr = int(input("Enter a number of trapozoids "))
print (trapozoidsum(function, tr, start, end))
graphing(function, tr, start, end)




