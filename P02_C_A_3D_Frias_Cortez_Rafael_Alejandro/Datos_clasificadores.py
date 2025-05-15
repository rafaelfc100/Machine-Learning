import pandas as pd
import os

rutas = [
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\1_Mi\p1\caracteristicas_Mi_p1_atornillar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\1_Mi\p1\caracteristicas_Mi_p1_martillar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\1_Mi\p1\caracteristicas_Mi_p1_taladrar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\1_Mi\p2\caracteristicas_Mi_p2_atornillar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\1_Mi\p2\caracteristicas_Mi_p2_martillar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\1_Mi\p2\caracteristicas_Mi_p2_taladrar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\1_Mi\p3\caracteristicas_Mi_p3_atornillar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\1_Mi\p3\caracteristicas_Mi_p3_martillar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\1_Mi\p3\caracteristicas_Mi_p3_taladrar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\2_Su\p1\caracteristicas_Su_p1_atornillar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\2_Su\p1\caracteristicas_Su_p1_martillar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\2_Su\p1\caracteristicas_Su_p1_taladrar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\2_Su\p2\caracteristicas_Su_p2_atornillar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\2_Su\p2\caracteristicas_Su_p2_martillar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\2_Su\p2\caracteristicas_Su_p2_taladrar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\2_Su\p3\caracteristicas_Su_p3_atornillar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\2_Su\p3\caracteristicas_Su_p3_martillar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\2_Su\p3\caracteristicas_Su_p3_taladrar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\3_An\p1\caracteristicas_An_p1_atornillar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\3_An\p1\caracteristicas_An_p1_martillar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\3_An\p1\caracteristicas_An_p1_taladrar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\3_An\p2\caracteristicas_An_p2_atornillar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\3_An\p2\caracteristicas_An_p2_martillar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\3_An\p2\caracteristicas_An_p2_taladrar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\3_An\p3\caracteristicas_An_p3_atornillar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\3_An\p3\caracteristicas_An_p3_martillar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\3_An\p3\caracteristicas_An_p3_taladrar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\4_Di\p1\caracteristicas_Di_p1_atornillar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\4_Di\p1\caracteristicas_Di_p1_martillar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\4_Di\p1\caracteristicas_Di_p1_taladrar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\4_Di\p2\caracteristicas_Di_p2_atornillar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\4_Di\p2\caracteristicas_Di_p2_martillar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\4_Di\p2\caracteristicas_Di_p2_taladrar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\4_Di\p3\caracteristicas_Di_p3_atornillar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\4_Di\p3\caracteristicas_Di_p3_martillar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\4_Di\p3\caracteristicas_Di_p3_taladrar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\5_Ma\p1\caracteristicas_Ma_p1_atornillar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\5_Ma\p1\caracteristicas_Ma_p1_martillar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\5_Ma\p1\caracteristicas_Ma_p1_taladrar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\5_Ma\p2\caracteristicas_Ma_p2_atornillar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\5_Ma\p2\caracteristicas_Ma_p2_martillar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\5_Ma\p2\caracteristicas_Ma_p2_taladrar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\5_Ma\p3\caracteristicas_Ma_p3_atornillar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\5_Ma\p3\caracteristicas_Ma_p3_martillar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\5_Ma\p3\caracteristicas_Ma_p3_taladrar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\6_Mar\p1\caracteristicas_Mar_p1_atornillar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\6_Mar\p1\caracteristicas_Mar_p1_martillar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\6_Mar\p1\caracteristicas_Mar_p1_taladrar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\6_Mar\p2\caracteristicas_Mar_p2_atornillar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\6_Mar\p2\caracteristicas_Mar_p2_martillar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\6_Mar\p2\caracteristicas_Mar_p2_taladrar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\6_Mar\p3\caracteristicas_Mar_p3_atornillar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\6_Mar\p3\caracteristicas_Mar_p3_martillar.csv",
r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\6_Mar\p3\caracteristicas_Mar_p3_taladrar.csv"
]

df_total = []

for ruta in rutas:
    df = pd.read_csv(ruta)

    nombre_archivo = os.path.basename(ruta) 
    partes = nombre_archivo.replace(".csv", "").split("_")

    persona = partes[1]      # Mi, Su, An, etc.
    repeticion = partes[2]   # p1, p2, p3
    actividad = partes[3]    # atornillar, martillar, taladrar


    df["persona"] = persona
    df["repeticion"] = repeticion
    df["actividad"] = actividad

    df_total.append(df)

df_final = pd.concat(df_total, ignore_index=True)
salida = r"C:\Users\rafae\Desktop\aprendizaje\Joints_Practica2\caracteristicas_completo_filtro.csv"
df_final.to_csv(salida, index=False)
print("CSV combinado guardado en:", salida)
