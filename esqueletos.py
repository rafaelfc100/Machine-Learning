import os
import numpy as np
import matplotlib.pyplot as plt
import csv

# Ruta base de los datos
base_path = r"C:\Users\rafae\Desktop\aprendizaje\PF_Frias_Cortez_Rafael_Alejandro"
start_frame = 100
end_frame = 101

# Conexiones del esqueleto (según el modelo de Kinect)
skeleton_connections = [
    (0, 1), (1, 20), (20, 2), (2, 3),        # columna y cabeza
    (20, 4), (4, 5), (5, 6), (6, 7),         # brazo derecho
    (7, 21), (6, 22),                        # dedos derecho
    (20, 8), (8, 9), (9, 10), (10, 11),      # brazo izquierdo
    (11, 23), (10, 24),                      # dedos izquierdo
    (0, 12), (12, 13), (13, 14), (14, 15),   # pierna derecha
    (0, 16), (16, 17), (17, 18), (18, 19)    # pierna izquierda
]

# Leer archivo de posiciones
def leer_position_data(file_path):
    data = []
    with open(file_path, 'r') as f:
        for line in f:
            parts = line.strip().split()
            frame_idx = int(parts[0])
            coords = list(map(float, parts[1:]))
            joints = np.array(coords).reshape(-1, 3)
            data.append((frame_idx, joints))
    return data

# Suavizado por promedio móvil
def suavizar_joints(data, ventana=3):
    datos_suavizados = []
    n_frames = len(data)
    for i in range(n_frames):
        inicio = max(0, i - ventana // 2)
        fin = min(n_frames, i + ventana // 2 + 1)
        suma = np.zeros_like(data[0][1])
        for j in range(inicio, fin):
            suma += data[j][1]
        promedio = suma / (fin - inicio)
        datos_suavizados.append((data[i][0], promedio))
    return datos_suavizados

# Visualización 2D (opcional)
def visualizar_esqueleto_2D(joints, conexiones, frame_idx):
    plt.figure(figsize=(6, 8))
    for i, j in conexiones:
        if i < len(joints) and j < len(joints):
            x = [joints[i][0], joints[j][0]]
            y = [joints[i][1], joints[j][1]]
            plt.plot(x, y, 'k-', linewidth=2)
    x_coords = joints[:, 0]
    y_coords = joints[:, 1]
    plt.scatter(x_coords, y_coords, c='red', s=40)
    for idx, (x, y) in enumerate(zip(x_coords, y_coords)):
        plt.text(x, y, str(idx), fontsize=9)
    plt.show()
    plt.close()

# Distancias desde pelvis (joint 0) a otras partes del cuerpo
def calcular_distancias_especificas(joints):
    indices = [3, 4, 5, 6, 7, 8, 9, 10]
    distancias = [np.linalg.norm(joints[i] - joints[0]) for i in indices]
    return distancias

# Velocidades por frame
def calcular_velocidades(distancias, prev_distancias):
    if prev_distancias is None:
        return [0] * len(distancias)
    return [distancias[i] - prev_distancias[i] for i in range(len(distancias))]

# Ruta a los datos
subcarpeta = os.path.join(base_path, "Luis Leonardo", "files")
file_path = os.path.join(subcarpeta, "capturedData.txt")

# Leer y aplicar 3 pasadas de suavizado con ventana de 3
data = leer_position_data(file_path)
data_suavizada = suavizar_joints(data, ventana=3)
data_suavizada = suavizar_joints(data_suavizada, ventana=3)
data_suavizada = suavizar_joints(data_suavizada, ventana=3)

# Crear CSV de salida
csv_path = os.path.join(subcarpeta, "distancias_y_velocidades_3_ventanas_sentarse_3_.csv")
with open(csv_path, mode='w', newline='') as f:
    writer = csv.writer(f)
    header = ["Frame", "Codo_Izq", "Codo_Der", "Muñeca_Izq", "Muñeca_Der",
              "Rodilla_Izq", "Rodilla_Der", "Talon_Izq", "Talon_Der",
              "Vel_Codo_Izq", "Vel_Codo_Der", "Vel_Muñeca_Izq", "Vel_Muñeca_Der",
              "Vel_Rodilla_Izq", "Vel_Rodilla_Der", "Vel_Talon_Izq", "Vel_Talon_Der"]
    writer.writerow(header)

    prev_distancias = None
    for frame_idx in range(start_frame, end_frame + 1):
        joints = data_suavizada[frame_idx][1]
        distancias = calcular_distancias_especificas(joints)
        velocidades = calcular_velocidades(distancias, prev_distancias)
        writer.writerow([frame_idx] + distancias + velocidades)
        visualizar_esqueleto_2D(joints, skeleton_connections, frame_idx)  # opcional
        prev_distancias = distancias

print(f"\nDistancias y velocidades SUAVIZADAS guardadas en: {csv_path}")
