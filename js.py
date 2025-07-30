import json

# Cargar tu archivo JSON con la clave de servicio
with open("firebase_config.json") as f:
    data = json.load(f)

# Codificar correctamente la private_key (convertir los saltos de línea en \n)
data["private_key"] = data["private_key"].replace("\n", "\\n")

# Imprimir la cadena para copiar y pegar en Render
print(json.dumps(data))
