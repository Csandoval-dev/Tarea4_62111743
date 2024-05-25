from collections import deque

class Usuario:
    def __init__(self, id_usuario, nombre):
        self.id_usuario = id_usuario
        self.nombre = nombre

    def __str__(self):
        return f"ID: {self.id_usuario}, Nombre: {self.nombre}"

class ColaAtencion:
    def __init__(self):
        self.cola = deque()

    def ingresar_usuario(self, usuario):
        self.cola.append(usuario)
        print(f"Usuario {usuario} ha ingresado a la cola.")

    def atender_usuario(self):
        if self.cola:
            usuario = self.cola.popleft()
            print(f"Atendiendo a {usuario}")
            return usuario
        else:
            print("No hay usuarios en la cola para atender.")
            return None

    def mostrar_cola(self):
        if self.cola:
            print("Usuarios en espera:")
            for usuario in self.cola:
                print(usuario)
        else:
            print("No hay usuarios en espera.")

def main():
    cola_atencion = ColaAtencion()

    while True:
        print("\n--- Menú ---")
        print("1. Ingresar usuario")
        print("2. Atender usuario")
        print("3. Mostrar cola")
        print("4. Salir")

        opcion = input("Ingrese la opción deseada: ")

        if opcion == "1":
            id_usuario = input("Ingrese el ID del usuario: ")
            nombre = input("Ingrese el nombre del usuario: ")
            usuario = Usuario(id_usuario, nombre)
            cola_atencion.ingresar_usuario(usuario)
        elif opcion == "2":
            cola_atencion.atender_usuario()
        elif opcion == "3":
            cola_atencion.mostrar_cola()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    main()
