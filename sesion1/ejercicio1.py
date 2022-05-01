### Ejercicio
"""
Del ejercicio avanzado añade lo siguiente

- Crear un método para retirar dinero
- Crear un método para depositar dinero
- Crear un método para mostrar un balance (Nombre y Saldo)
- **Bonus: Crea un método para transferir dinero.**
"""

class User:
    def __init__(self,nombre,dinero):
        self.dinero=dinero
        self.nombre=nombre
    def depositar(self, monto):
        # self.dinero = self.dinero + monto
        self.dinero+=monto
        print(self.dinero)

    def retirar(self, monto):
        self.dinero-=monto
        print(self.dinero)

    def mostrarBalance(self):
        return f'Usuario: {self.nombre} - Saldo: {self.dinero}'

objElias = User("Elias", 100)
# Depositamos 50 soles en la cuenta de mi usuario
objElias.depositar(50)
# objElias.depositar(5)
# Retiramos 4 soles para un helado
objElias.retirar(4)

# Mostramos el balance
respuestaBalance=objElias.mostrarBalance()
print(respuestaBalance)