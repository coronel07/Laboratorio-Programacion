class Alumno:
    def __init__(self, nombre, apellido, edad, curso):
        self.nombre = nombre.capitalize()  
        self.apellido = apellido.capitalize() 
        self.edad = edad 
        self.curso = curso
    
    def programar(self):
        print(f"El alumno {self.nombre} está programando")


nombre = input("Ingresar tu nombre:")
apellido = input("Ingresa tu apellido:")
edad = input("Ingresa tu nombre:")
curso = input("Ingresa tu curso:")


alumno1 = Alumno(nombre, apellido, edad, curso)


alumno1.programar()
