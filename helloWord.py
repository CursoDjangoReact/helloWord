def welcome_message():
    name = input("Por favor ingrese su nombre: ")
    ciudad = input("¿De dónde eres? ")
    atencion = input("¿Qué fue lo que más te llamó la atención del curso? ")
    print("Bienvenido,", name, "al curso de Django y React!")
    print("Esperamos que disfrutes tu estadía en", ciudad, "y que aprendas mucho sobre", atencion)

if __name__ == "__main__":
    welcome_message()