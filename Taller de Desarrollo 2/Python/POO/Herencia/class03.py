# Taller de Desarrollo 2
# Sesion: 08 de Septiembre del 2023
# Introduccion a POO con Clases
# Archivo "class03.py"
# Identificador: Realizar un programa que tenga una clase Persona con las siguientes características. La clase tendrá como atributos el nombre y la edad de una persona. Implementar los métodos necesarios para inicializar los atributos, mostrar los datos e indicar si la persona es mayor de edad o no.
# Alfredo Lopez Mendez

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre;
        self.edad = edad;
        
    def datos(self):
        print("Nombre: ", self.nombre);
        print("Edad: ", self.edad);
        
    def mayorEdad(self):
        if self.edad > 18:
            print(self.nombre + " es mayor de edad por tener ", self.edad, " años\n");
        else:
            print(self.nombre + " es menor de edad por tener ", self.edad, " años\n")
            
persona = Persona("Owen", 23);
persona.datos();
persona.mayorEdad();

persona = Persona("Alan", 17);
persona.datos();
persona.mayorEdad();

