import os
import numpy as np
import matplotlib.pyplot as plt
import csv

base_path = r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2"
start_frame = 192
end_frame = 292

"""skeleton_connections = [
    (0, 1), (1, 20), (20, 2), (2, 3),        # columna y cabeza
    (20, 4), (4, 5), (5, 6), (6, 7),         # brazo izquierdo
    (7, 21), (6, 22),                        # dedos izquierdo
    (20, 8), (8, 9), (9, 10), (10, 11),      # brazo derecho
    (11, 23), (10, 24),                      # dedos derecho
    (0, 12), (12, 13), (13, 14), (14, 15),   # pierna izquierda
    (0, 16), (16, 17), (17, 18), (18, 19)    # pierna derecha
]"""

skeleton_connections = [
    (0, 1), (1, 20), (20, 2), (2, 3),        # columna y cabeza
    (20, 4), (4, 5), (5, 6), (6, 7),         # brazo derecho
    (7, 21), (6, 22),                        # dedos derecho
    (20, 8), (8, 9), (9, 10), (10, 11),      # brazo izquierdo
    (11, 23), (10, 24),                      # dedos izquierdo
    (0, 12), (12, 13), (13, 14), (14, 15),   # pierna derecha
    (0, 16), (16, 17), (17, 18), (18, 19)    # pierna izquierda
]


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

def suavizar_joints(data, ventana=5):
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
    # plt.show()
    plt.close()

def calcular_distancias_especificas(joints):
    indices = [3, 4, 5, 6, 7, 8, 9, 10]
    distancias = [np.linalg.norm(joints[i] - joints[0]) for i in indices]
    return distancias

def calcular_velocidades(distancias, prev_distancias):
    velocidades = []
    if prev_distancias is None:
        return [0] * len(distancias)
    for i in range(len(distancias)):
        velocidad = distancias[i] - prev_distancias[i]
        velocidades.append(velocidad)
    return velocidades

subcarpeta = os.path.join(base_path, "6_Mar", "p3")
file_path = os.path.join(subcarpeta, "positionData.txt")

data = leer_position_data(file_path)
data_suavizada = suavizar_joints(data, ventana=5)

csv_path = os.path.join(subcarpeta, "distancias_y_velocidades_atornillar.csv")
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
        prev_distancias = distancias

print(f"\n Distancias y velocidades SUAVIZADAS guardadas en: {csv_path}")
