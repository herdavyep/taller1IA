
# coding: utf-8

# In[88]:


print ("MEDIANA")
array = [2,4,6,8,1,3,5,7,9,1,2,2]   
array.sort()
print(array)
if cantidad % 2 == 0:
    
    mediana = (array[cantidad//2-1] + array[cantidad//2] )//2  
else:
    mediana = array[cantidad//2]

print ("Mediana es = ",mediana)


# In[89]:


print ("MODA")
array.sort()
print(array)
CantidadFrecuencia = 0
for i in array:                                                                 
    encontrado = array.count(i)                                                
    if encontrado > CantidadFrecuencia:                                              
        CantidadFrecuencia = encontrado                                              

moda = []  

for i in array:                                                                 
    encontrado = array.count(i)                                                

    if encontrado == CantidadFrecuencia and i not in moda:                          
        moda.append(i)
       
print ("moda es = ", moda)  



# In[90]:


print ("PROMEDIO")
suma =  sum(array)
cantidad = len(array)
promedio = suma/cantidad  

print (cantidad,"elementos que suman",suma, "y promediandolos dan como resultado es = ",promedio)


# In[91]:


def sumaDatos(datos):
    total = 0
    for grado in datos:
        total += grado
    return total

def promedioDatos(datos):
    suma_datos = sumaDatos(datos)
    promedio = float(suma_datos) / len(datos)
    return promedio

def varianzaDatos(datos, promedio):
    sumatoria = 0
    for dato in datos:
        sumatoria += (promedio - float(dato)) ** 2
    variance = float(sumatoria) / len(array)
    return variance

print("varianza es = ",varianzaDatos(array, promedioDatos(array)))

