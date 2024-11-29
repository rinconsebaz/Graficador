import matplotlib.pyplot as plt
import numpy as np

# Datos originales
x_original = [
    7.46, 7.46, 7.46, 7.51, 7.53, 7.61, 7.60, 7.60, 7.64, 7.64, 7.66, 7.70,
    7.71, 7.72, 7.71, 7.70, 7.68, 7.67, 7.65, 7.62, 7.59, 7.56, 7.51, 7.53,
    7.50, 7.57, 7.48
]
y_original = [
    7.3, 7.3, 7.3, 7.3, 7.28, 7.21, 7.13, 7.9, 7.01, 6.92, 6.81, 6.79, 6.60,
    6.45, 6.30, 6.12, 5.98, 5.74, 5.54, 5.37, 5.14, 4.95, 4.75, 4.54, 4.30,
    4.19, 4.81, 3.87, 3.71, 3.66, 3.42, 3.32, 3.24, 3.19, 3.07, 3.05, 3.03,
    3.02, 3.2, 3.0
]

# Crear una secuencia interpolada de 250 elementos
target_length = 250
x_interpolated = np.interp(
    np.linspace(0, len(x_original) - 1, target_length),
    np.arange(len(x_original)),
    x_original
)
y_interpolated = np.interp(
    np.linspace(0, len(y_original) - 1, target_length),
    np.arange(len(y_original)),
    y_original
)
z_interpolated = [3.5] * target_length  # z es constante

# Crear una cuadrícula para graficar la superficie
x_grid = np.linspace(min(x_interpolated), max(x_interpolated), 50)
y_grid = np.linspace(min(y_interpolated), max(y_interpolated), 50)
x_mesh, y_mesh = np.meshgrid(x_grid, y_grid)

# Simular una distribución para z (capacitancia o potencial)
z_mesh = np.sin(x_mesh) + np.cos(y_mesh) + 3.5  # Esta función es un ejemplo

# Crear gráfico de superficie
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surface = ax.plot_surface(
    x_mesh, y_mesh, z_mesh, cmap='viridis', edgecolor='none'
)

# Etiquetas y título
ax.set_xlabel('Capacitancia en Eje X ')
ax.set_ylabel('Capacitancia en Eje Y ')
ax.set_zlabel('Capacitancia (pF)')
plt.title("Distribución de Capacitancia en el Plano")
fig.colorbar(surface, ax=ax, shrink=0.5, aspect=10, label='Capacitancia (pF)')

# Mostrar la gráfica
plt.show()

# Función interactiva para agregar o quitar datos
def interactive_3d_plot():
    """
    Maneja una sesión interactiva para agregar o quitar puntos del gráfico.
    """
    x = default_data["x"][:]
    y = default_data["y"][:]
    z = default_data["z"][:]

    while True:
        # Graficar los datos actuales
        plot_3d(x, y, z)
        
        print("\nOpciones:")
        print("1. Agregar un punto")
        print("2. Eliminar un punto")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            try:
                # Pedir coordenadas del nuevo punto
                new_x = float(input("Ingrese la coordenada X: "))
                new_y = float(input("Ingrese la coordenada Y: "))
                new_z = 3.5  # z es constante
                x.append(new_x)
                y.append(new_y)
                z.append(new_z)
                print("Punto agregado con éxito.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese números válidos.")
        
        elif opcion == "2":
            try:
                # Mostrar los puntos actuales
                for i, (xi, yi, zi) in enumerate(zip(x, y, z)):
                    print(f"{i}: ({xi}, {yi}, {zi})")
                index = int(input("Ingrese el índice del punto a eliminar: "))
                if 0 <= index < len(x):
                    x.pop(index)
                    y.pop(index)
                    z.pop(index)
                    print("Punto eliminado con éxito.")
                else:
                    print("Índice fuera de rango.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número válido.")
        
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione 1, 2 o 3.")

# Ejecutar la función interactiva
interactive_3d_plot()  # Descomentar para ejecución interactiva
