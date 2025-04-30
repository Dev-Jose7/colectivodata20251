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
# print(asistenciaDataFrame["estrato"].value_counts().head(2))

## FILTRO O CONSULTAS DETALLADAS
# Necesito encontrar los estudiantes que asistieron
# Necesito encontrar los estudiantes que faltaron
# Necesito encontrar los estudiantes que llegaron tarde, es decir que justificarón la inasistencia
# Necesito encontrar los estudiantes de estrato 1
# Necesito encontrar los estudiantes de estratos altos
# Necesito encontrar estudiantes que llegan en metro
# Necesito encontrar estudiantes que llegarón en bicicleta
# Necesito encontrrar todos los estudiantes menos los que llegarón a pie
# Necesito todos los registros de asistencia de Junio
# Necesito todos los estudiantes que usan transportes ecologicos
# Necesito los que usan bus y son de estrato alto
# Necesito los que usan bus y son de estrato bajo
# Necesito estudiantes que caminan para llegar a clase

## CONTEOS POR AGRUPACIONES
# Necesito el conteo de registros por estado de asistencia 
# Necesito obtener el número de registro por estrato
# Necesito la agrupar cantidad de estudiante por medio de transporte
# Necesito el promedio del estrato por estado de asistencia
# Máximo estrato por estado
# Minimo estrato por estado
# Necesito un conteo de asistencia por grupo y estado

