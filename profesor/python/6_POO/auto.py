class Auto:
    # Propiedades - atributos - variables globales dentro de la propia clase
    marca = ""
    color = ""
    combustible = ""
    asientos = ""
    numero_ruedas = ""
    encendido = False

    # Metodos - funciones que puede realizar mi auto. - Acciones que hace el objeto.

    # Funcion constructor - inicializa el objeto siempre se escribe igual
    # todas las funciones dentro de una clase reciben como parametro el propio objeto (self). Representa el propio objeto
    def __init__(self, color, marca, tipo_combustible, numero):
        self.marca = marca
        self.color = color
        self.numero_ruedas = numero
        self.combustible = tipo_combustible

    def arrancar(self):
        self.encendido = True
        print('Coche arrancado')

    # una funcion de clase que cambia una propiedad se setter
    def cambiar_color(self, color_nuevo):
        self.color = color_nuevo


ferrari = Auto('rojo', 'ferrari', 'gasolina', 4)
topolino = Auto('vino', 'Fiat', 'diesel', 4)
print(ferrari.encendido)
ferrari.arrancar()
print(ferrari.encendido)
ferrari.cambiar_color('amarillo')
print(ferrari.color)
