import pandas as pd
import os

input_csv_path = r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\6_Mar\p3\distancias_y_velocidades_taladrar.csv"

df = pd.read_csv(input_csv_path, encoding='latin1')
 
if 'Frame' in df.columns:
    df = df.drop(columns=['Frame'])

# diccionario para las caracteristicas
features = {}

# calculo de las caracteristicas
for col in df.columns:
    series = df[col]
    features[f'{col}_mean'] = series.mean()
    features[f'{col}_var'] = series.var()
    features[f'{col}_min'] = series.min()
    features[f'{col}_max'] = series.max()

features_df = pd.DataFrame([features])

output_csv_path = os.path.join(os.path.dirname(input_csv_path), 'caracteristicas_taladrar.csv')

features_df.to_csv(output_csv_path, index=False)
print(f"Características guardadas en: {output_csv_path}")
