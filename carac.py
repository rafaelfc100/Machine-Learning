import pandas as pd
import os

# Ruta al archivo de entrada
input_csv_path = r"C:\Users\rafae\Desktop\aprendizaje\PF_Frias_Cortez_Rafael_Alejandro\Luis Leonardo\files\distancias_y_velocidades_3_ventanas_sentarse_3_.csv"

# Leer el CSV usando codificación compatible
df = pd.read_csv(input_csv_path, encoding='latin1')

# Eliminar columna Frame si existe
if 'Frame' in df.columns:
    df = df.drop(columns=['Frame'])

# Diccionario para guardar características
features = {}

# Para cada columna (distancia o velocidad), calcular características
for col in df.columns:
    series = df[col]
    features[f'{col}_mean'] = series.mean()
    features[f'{col}_var'] = series.var()
    features[f'{col}_min'] = series.min()
    features[f'{col}_max'] = series.max()

# Convertir a DataFrame con una sola fila
features_df = pd.DataFrame([features])

# Ruta de salida
output_csv_path = os.path.join(os.path.dirname(input_csv_path), 'caracteristicass_3_ventanas_sentarse_3.csv')


# Guardar el nuevo CSV
features_df.to_csv(output_csv_path, index=False)
print(f"Características guardadas en: {output_csv_path}")
