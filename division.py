#Las excepciones nos permiten gestionar errores en tiempo de ejecución
try:
    val1=int(input('Valor 1 = '))
    val2=int(input('Valor 2 = '))
   
    div=val1/val2
    print ('División: ', div)

except ZeroDivisionError:
    print('Error aritmético')
except ValueError:
    print('Valor Inesperado para los valores')
finally:
    print('Uppps Hubo un Error')    