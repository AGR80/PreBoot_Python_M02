def sumaTodos(a):
    resultado = 0
    for i in range(0, a):
        resultado += i
        
    return resultado



def sumaTodosLosCuadrados(limitTo):
    resultado = 0
    for i in range(limitTo+1):
        resultado += i*i
        
    return resultado
        
print(sumaTodos(100))
print(sumaTodosLosCuadrados(3))


  
        
        
        