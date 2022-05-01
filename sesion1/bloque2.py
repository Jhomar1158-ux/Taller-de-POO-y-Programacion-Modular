class User:
    # Método mágico __init__
    def __init__(self, nombre, correo):
        # Declaramos nuestros atributos(características)
        self.nombre=nombre
        self.correo=correo
    # Método
    def hola(self):
        print("Holaa!")
    # Método de instancia
    def holaPersonalizado(self, edad):
        return f'Holaa {self.nombre}!! Tienes {edad} años!!'

# Instancia un objeto de tipo User<class>
objPaulo = User("Paulo", "paulo@gmail.com") #camelCase
objJhomar = User("Jhomar", "jhomar@gmail.com")
# Imprimimos el nombre de nuestro objeto
print(objPaulo.nombre)
print(objJhomar.nombre)

# Imprimimos el correo
print("Correo de Paulo: ")
print(objPaulo.correo)

resultadoHola=objJhomar.holaPersonalizado(22)
print(resultadoHola)


### Ejercicio
"""
Del ejercicio avanzado añade lo siguiente

- Crear un método para retirar dinero
- Crear un método para depositar dinero
- Crear un método para mostrar un balance (Nombre y Saldo)
- **Bonus: Crea un método para transferir dinero.**

"""
