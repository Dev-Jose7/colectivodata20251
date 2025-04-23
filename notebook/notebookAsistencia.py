import pandas as pd

asistenciaDataFrame = pd.read_csv("./data/asistencia_estudiantes_completo.csv")
## Leyendo los datos de asistencias
# print(asistenciaDataFrame)

## Obteniendo información básica del dataframe
# print(asistenciaDataFrame.info())
# print(asistenciaDataFrame.tail())
# print(asistenciaDataFrame.head())
# print(asistenciaDataFrame.describe())
# print(asistenciaDataFrame.isnull().sum())
# print(asistenciaDataFrame["estado"].value_counts())
print(asistenciaDataFrame["estrato"].value_counts().head(2))