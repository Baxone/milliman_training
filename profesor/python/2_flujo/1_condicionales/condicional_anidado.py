mark = float(input('Dime tu nota: '))

# recordar por favor que siempre es buena practica empezar por la condiciones mas restrictivas.

if mark >= 0 and mark < 5:
    print('suspenso')
elif mark >= 5 and mark <= 10:
    print('aprobados')
else:
    print('nota no valida')

if mark >= 0 and mark < 5:
    print('suspenso')
elif mark >= 5 and mark < 6:
    print('suficiente')
elif mark >= 6 and mark < 7:
    print('bien')
elif mark >= 7 and mark < 9:
    print('notable')
elif mark >= 9 and mark <= 10:
    print('sobresaliente')
else:
    print('nota no valida')
