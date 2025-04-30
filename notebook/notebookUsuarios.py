import pandas as pd

usuariosDataFrame = pd.read_excel("./data/usuarios_sistema_completo.xlsx")

# print(usuariosDataFrame)
print(usuariosDataFrame.isnull().sum())

## FILTRO
# Necesito solo un listado de aprendices.
# Necesito un listado con instructores
# Necesito un listado de especialista en desarrollo web o sistema
# Necesito un listado de usuarios con direcciones solo en Medellín
# Necesito un listado de solo usuarios cuya direcciones terminen en sur
# Necesito un listado de especialista que contengan la palabra "Datos" en la especialidad
# Necesito una lista de nacidos antes de 1990
# Necesito un listado de instructores son ancianos
# Neceisto un listado de instructores nacidos en el nuevo milenio