def main():
    #escribe tu código abajo de esta línea
    Mat1 = float(input("ingresa calificacion de materia: "))
    Mat2 = float(input("ingresa calificacion de materia: "))
    Mat3 = float(input("ingresa calificacion de materia: "))
    Mat4 = float(input("ingresa calificacion de materia: "))
    promedio = (Mat1 + Mat2 + Mat3 + Mat4)/4

    print("el promedio general es: " + str(promedio))

if __name__ == '__main__':
    main()
