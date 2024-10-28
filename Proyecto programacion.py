import os
from datetime import datetime, timedelta

# Defino la clase Alumno para el inicio de sesión
class Alumno:
    # Constructor para inicializar los atributos
    def __init__(self, usuario, contrasena, carrera):
        self.usuario = usuario
        self.contrasena = contrasena
        self.carrera = carrera

    # Método para registrar un nuevo usuario
    @staticmethod
    def registrar():
        usuario = input("Ingrese su usuario: ")
        contrasena = input("Ingrese su contraseña: ")
        carrera = input("Ingrese su carrera: ")
        return Alumno(usuario, contrasena, carrera)

    # Método para iniciar sesión
    def iniciar_sesion(self):
        while True:
            usuario = input("Ingrese su usuario: ")
            contrasena = input("Ingrese su contraseña: ")
            if usuario == self.usuario and contrasena == self.contrasena:
                os.system("cls")  # Para Windows usa 'cls'
                print(f"Bienvenido {self.usuario} a créditos a un click.")
                break
            else:
                print("Usuario o contraseña incorrectos. Intente de nuevo.")

# Función para limpiar la pantalla y mostrar el menú
def menu():
    os.system("cls")  # Para Windows usa 'cls'
    print("Bienvenidos a créditos a un click, por favor seleccione una opción:")
    print("\t1- Planificación Personalizada")
    print("\t2- Visualizar el calendario académico")
    print("\t3- Consulta de materias y créditos cursados")
    print("\t4- Enviar alertas sobre eventos importantes")
    print("\t5- Análisis de rendimiento académico")
    print("\t0- Salir")

# Función para guardar los datos del alumno en un archivo
def guardar_datos(alumno):
    with open('proyecto_programacion.txt', 'w') as archivo:
        archivo.write(f"{alumno.usuario}\n")
        archivo.write(f"{alumno.contrasena}\n")
        archivo.write(f"{alumno.carrera}\n")

# Función para cargar los datos del alumno desde un archivo
def cargar_datos():
    try:
        with open('proyecto_programacion.txt', 'r') as archivo:
            usuario = archivo.readline().strip()
            contrasena = archivo.readline().strip()
            carrera = archivo.readline().strip()
            return Alumno(usuario, contrasena, carrera)
    except FileNotFoundError:
        return None  # Retorna None si el archivo no existe

# Datos del pensum de Ingeniería Biomédica
pensum = {
    1: [("Álgebra Lineal", 3), ("Biología Estructural", 2), ("Cálculo Diferencial", 4), ("Expresión", 4),
        ("Fundamentos de Programación", 3), ("Laboratorio Biología Estructural", 0), ("Seminario de Ingeniería I", 2)],
    2: [("Biología Celular y Molecular", 2), ("Cálculo Integral", 4), ("Dibujo de Ingeniería", 2), ("Identidad", 3),
        ("Laboratorio Biología Celular y Molecular", 0), ("Laboratorio de Mecánica", 0), ("Mecánica y Laboratorio", 3),
        ("Programación de Computadores", 3)],
    3: [("Bioquímica", 2), ("Cálculo en Varias Variables", 3), ("Creatividad", 3), ("Dibujo Asistido por Computador", 2),
        ("Electromagnetismo y Laboratorio", 3), ("Estadística General", 3), ("Laboratorio Bioquímica", 0),
        ("Laboratorio de Electromagnetismo", 0), ("Seminario de Ingeniería II", 2)],
    4: [("Circuitos Eléctricos", 3), ("Ecuaciones Diferenciales", 3), ("Electiva Sociohumanística", 3),
        ("Laboratorio Circuitos Eléctricos", 0), ("Laboratorio Morfofisiología Biomédica I", 0),
        ("Laboratorio Termofluidos", 0), ("Morfofisiología Biomédica I", 3 ),
        ("Taller de Deportes, Recreación y Cultura", 1), ("Taller de Desarrollo Humano", 1), ("Termof luidos", 3)],
    5: [("Actividades Libres de Recreación, Deporte y Cultura y de Desarrollo Humano", 2), ("Biomateriales", 3),
        ("Electiva Sociohumanística", 3), ("Electrónica Análoga", 3), ("Inteligencia Artificial y Ciencia de Datos", 2),
        ("Laboratorio Biomateriales", 0), ("Laboratorio de Electrónica Análoga", 0),
        ("Laboratorio Morfofisiología Biomédica II", 0), ("Laboratorio Sistemas Embebidos", 0),
        ("Morfofisiología Biomédica II", 3), ("Sistemas Embebidos", 2)],
    6: [("Biomecánica Deportiva", 2), ("Electiva de Contexto", 3), ("Electrónica de Potencia", 2),
        ("Equipos Médicos Básicos", 2), ("Imágenes Biomédicas", 2), ("Ingeniería Clínica", 3),
        ("Laboratorio Biomecánica Deportiva", 0), ("Laboratorio Electrónica de Potencia", 0),
        ("Laboratorio Equipos Médicos Básicos", 0), ("Laboratorio Ingeniería Clínica", 0),
        ("Procesamiento de Señales Biomédicas", 2), ("Tissue Engineering", 2),
        ("Tissue Engineering Laboratory", 0)],
    7: [("Biomecánica Clínica", 2), ("Electiva Profundización", 3), ("Equipos de Monitoreo y Diagnóstico Médico", 2),
        ("Ingeniería Hospitalaria", 3), ("Instrumentación Biomédica", 3), ("Laboratorio Biomecánica Clínica", 0),
        ("Laboratorio Equipos de Monitoreo y Diagnóstico Médico", 0), ("Laboratorio Ingeniería Hospitalaria", 0),
        ("Laboratorio Instrumentación Biomédica", 0), ("Tele-Robótica Médica", 3)],
    8: [("Diseño en Medicina Personalizada", 3), ("Electiva de Contexto", 3), ("Electiva Profundización", 9),
        ("Equipos Médicos Avanzados", 2), ("Laboratorio Equipos Médicos Avanzados", 0)],
    9: [("Práctica Académica", 12), ("Proyecto de Diseño en Medicina Personalizada", 2)],
}

# Función para planificar el horario
def planificacion_personalizada(alumno):
    while True:
        os.system("cls")  # Para Windows usa 'cls'
        print(f"Planificación Personalizada para {alumno.carrera}")
        semestre = int(input("Ingrese el semestre (1-9): "))
        if semestre in pensum:
            print(f"\nMaterias del {semestre}º Semestre:")
            for materia, creditos in pensum[semestre]:
                print(f"- {materia}: {creditos} créditos")
            input("\nPulsa una tecla para continuar...")
            break
        else:
            print("Semestre no válido. Intente de nuevo.")

# Función para visualizar el calendario académico
def visualizar_calendario_academico():
    os.system("cls")  # Para Windows usa 'cls'
    fecha_str = input("Ingrese la fecha de inicio del semestre (YYYY-MM-DD): ")
    try:
        # Convertir la fecha de entrada en formato año-mes-día
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d")

        # Definir el inicio y fin del semestre
        inicio_semestre = fecha  # Usar la fecha ingresada como inicio
        fin_semestre = inicio_semestre + timedelta(weeks=18)  # Semestre de 18 semanas

        # Calcular las fechas de parciales (cada 9 semanas)
        fechas_parciales = [
            inicio_semestre + timedelta(weeks=9),
            inicio_semestre + timedelta(weeks=18)
        ]

        # Mostrar resultados
        print(f"\nInicio del semestre: {inicio_semestre.strftime('%Y-%m-%d')}")
        print(f"Fin del semestre: {fin_semestre.strftime('%Y-%m-%d')}")
        print("Fechas de parciales:")
        for i, fecha_parcial in enumerate(fechas_parciales, start=1):
            print(f"Parcial {i}: {fecha_parcial.strftime('%Y-%m-%d')}")
    except ValueError:
        print("Formato de fecha incorrecto. Use YYYY-MM-DD.")

    input("\nPulsa una tecla para continuar...")

# Función para consultar materias y créditos cursados
def consulta_materias_creditos(alumno):
    os.system("cls")  # Para Windows usa 'cls'
    semestre = int(input("Ingrese el semestre actual (1-9): "))
    if semestre in pensum:
        print(f"\nMaterias cursadas hasta el {semestre}º Semestre:")
        total_creditos = 0
        for sem in range(1, semestre+1):
            print(f"\n{sem}º Semestre:")
            for materia, creditos in pensum[sem]:
                print(f"- {materia}: {creditos} créditos")
                total_creditos += creditos
        print(f"\nTotal de Créditos Cursados: {total_creditos}")
    else:
        print("Semestre no válido.")
    input("\nPulsa una tecla para continuar...")

# Función para enviar alertas sobre eventos importantes
# Lista para almacenar las alertas
alertas = []

# Función para enviar alertas sobre eventos importantes
def enviar_alertas():
    while True:
        os.system("cls")  # Para Windows usa 'cls'
        print("Enviar Alertas sobre Eventos Importantes")
        print("1. Agregar una nueva alerta")
        print("2. Ver alertas existentes")
        print("0. Volver al menú principal")

        opcion = input("Seleccione una opción >> ")

        if opcion == "1":
            alerta = input("Ingrese la alerta: ")
            alertas.append(alerta)
            print("Alerta agregada con éxito.")
            input("Pulsa una tecla para continuar...")
        elif opcion == "2":
            if alertas:
                print("Alertas existentes:")
                for i, alerta in enumerate(alertas, 1):
                    print(f"{i}. {alerta}")
            else:
                print("No hay alertas registradas.")
            input("Pulsa una tecla para continuar...")
        elif opcion == "0":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
            input("Pulsa una tecla para continuar...")

# Función para análisis de rendimiento académico
def analizar_rendimiento(calificaciones):
    if not calificaciones:  # Verifica si la lista está vacía
        print("No hay calificaciones disponibles para analizar.")
        return

    # Calcular el promedio de calificaciones
    promedio = sum(calificaciones) / len(calificaciones)

    # Clasificar el rendimiento
    if promedio >= 4.0:
        rendimiento = "Bueno"
    elif promedio >= 2.5:
        rendimiento = "Regular"
    else:
        rendimiento = "Malo"

    # Mostrar resultados
    print(f"Promedio de calificaciones: {promedio:.2f}")
    print(f"Rendimiento académico: {rendimiento}")

# Función para análisis de rendimiento académico
def analisis_rendimiento_academico():
    os.system("cls")  # Para Windows usa 'cls'
    print("Análisis de rendimiento académico.")

    calificaciones_str = input("Ingrese las calificaciones separadas por comas (0 a 5): ")
    try:
        calificaciones = list(map(float, calificaciones_str.split(',')))  # Convertir a lista de flotantes
        # Verificar que las calificaciones estén en el rango 0 a 5
        if any(cal < 0 or cal > 5 for cal in calificaciones):
            print("Por favor, asegúrese de que todas las calificaciones estén entre 0 y 5.")
            return
        analizar_rendimiento(calificaciones)
    except ValueError:
        print("Por favor, ingrese las calificaciones en un formato válido (números separados por comas).")

    input("Pulsa una tecla para continuar...")

# Cargar datos del alumno desde archivo
alumno = cargar_datos()

if alumno is None:
    # Registro del alumno
    alumno = Alumno.registrar()
    guardar_datos(alumno)
else:
    # Inicio de sesión del alumno
    alumno.iniciar_sesion()

# Bucle del menú principal
while True:
    menu()
    opcion = input("Ingresa un número >> ")
    if opcion == "1":
        planificacion_personalizada(alumno)
    elif opcion == "2":
        visualizar_calendario_academico()
    elif opcion == "3":
        consulta_materias_creditos(alumno)
    elif opcion == "4":
        enviar_alertas()
    elif opcion == "5":
        analisis_rendimiento_academico()
    elif opcion == "0":
        break
    else:
        print("No has pulsado ninguna opción correcta.")
        input("Pulsa una tecla para continuar...")


