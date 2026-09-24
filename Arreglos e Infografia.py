import random
import time

# Parámetros del problema
NUM_ALUMNOS = 500
NUM_MATERIAS = 6

# 1. Crear la matriz (Alumnos x Materias) con datos aleatorios de calificaciones (5 a 10)
matriz_alumnos = [
    [random.randint(5, 10) for _ in range(NUM_MATERIAS)]
    for _ in range(NUM_ALUMNOS)
]

# 2. Función para buscar al alumno 321 y la materia 5
# Convertimos de índice base 1 (humano) a base 0 (Python):
def buscar_calificacion(matriz, id_alumno, id_materia):
    return matriz[id_alumno - 1][id_materia - 1]

# 3. Medición del tiempo de ejecución
inicio = time.perf_counter()

# Ejecutamos la búsqueda repetidamente para medir un tiempo representativo
for _ in range(1_000_000):
    calificacion = buscar_calificacion(matriz_alumnos, id_alumno=321, id_materia=5)

tiempo_total = time.perf_counter() - inicio

print(f"Calificación del alumno 321 en la materia 5: {calificacion}")
print(f"Tiempo de ejecución (1,000,000 búsquedas): {tiempo_total:.6f} segundos")


# --- Prueba con grandes volúmenes de datos ---
def probar_con_volumen(alumnos, materias):
    matriz_grande = [
        [random.randint(5, 10) for _ in range(materias)]
        for _ in range(alumnos)
    ]
    
    t_inicio = time.perf_counter()
    val = buscar_calificacion(matriz_grande, id_alumno=321, id_materia=5)
    t_fin = time.perf_counter() - t_inicio
    
    print(f"\nMatriz de {alumnos} alumnos x {materias} materias:")
    print(f"Acceso a la posición: {t_fin:.8f} segundos")

# Pruebas adicionales
probar_con_volumen(1000, 100)
probar_con_volumen(10000, 500)
probar_con_volumen(100000, 10000)