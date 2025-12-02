# condicional abreviado: es un condicional simple con secuencia de escape (binario). Si dentro de mi condicion una varible toma valores distintos entonces puedo convertirlo en un condicional abreviado.

light_status = False
msg = ""

"""
if not light_status:
    msg = 'No esta encendida'
else:
    msg = 'Esta encendida'
"""
# operador ternario, una variables cambia su valor en los dos lado de la condicion.

msg = 'apagado'if not light_status else 'encendido'

print(msg)
