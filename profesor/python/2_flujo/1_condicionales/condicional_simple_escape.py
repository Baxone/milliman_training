mark = 3.5

# uso incorrecto de una secuencia de escape.
if mark >= 5 and mark <= 10:
    print('aprobado')
else:
    print('suspenso')

# uso correcto, podemos usar secuencia de escape siempre y cuando la condicion se binaria.
estado_factura = "pagada"

if estado_factura == "pagada":
    print('gracias por tu compra')
else:
    print('no se ha podido realizar el pago, queda pendiente')
