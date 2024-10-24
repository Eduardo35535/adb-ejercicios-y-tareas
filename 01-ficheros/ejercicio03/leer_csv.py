import csv

# Definir los datos para los registros
registros = [
    {"Tipo": "Nombre", "CP": "35002", "Municipio": "Las Palmas de Gran Canaria", "Isla": "Gran Canaria", "Provincia": "Las Palmas", "Calle": "Avenida Marítima"},
    {"Tipo": "Nombre", "CP": "38800", "Municipio": "San Sebastián de La Gomera", "Isla": "La Gomera", "Provincia": "Santa Cruz de Tenerife", "Calle": "Calle de la Luz"},
    {"Tipo": "Nombre", "CP": "38400", "Municipio": "Puerto de la Cruz", "Isla": "Tenerife", "Provincia": "Santa Cruz de Tenerife", "Calle": "Avenida de Los Majuelos"},
    {"Tipo": "Nombre", "CP": "38107", "Municipio": "La Laguna", "Isla": "Tenerife", "Provincia": "Santa Cruz de Tenerife", "Calle": "Calle León y Castillo"},
    {"Tipo": "Nombre", "CP": "35500", "Municipio": "Arrecife", "Isla": "Lanzarote", "Provincia": "Las Palmas", "Calle": "Calle Real"},
    {"Tipo": "Nombre", "CP": "38760", "Municipio": "Los Llanos de Aridane", "Isla": "La Palma", "Provincia": "Santa Cruz de Tenerife", "Calle": "Avenida Juan Carlos I"},
    {"Tipo": "Nombre", "CP": "35600", "Municipio": "Puerto del Rosario", "Isla": "Fuerteventura", "Provincia": "Las Palmas", "Calle": "Calle de la Constitución"},
    {"Tipo": "Nombre", "CP": "38820", "Municipio": "Hermigua", "Isla": "La Gomera", "Provincia": "Santa Cruz de Tenerife", "Calle": "Calle de la Playa"},
    {"Tipo": "Nombre", "CP": "38914", "Municipio": "Valverde", "Isla": "El Hierro", "Provincia": "Santa Cruz de Tenerife", "Calle": "Avenida de Las Playas"},
    {"Tipo": "Nombre", "CP": "35510", "Municipio": "Tías", "Isla": "Lanzarote", "Provincia": "Las Palmas", "Calle": "Calle de la Constitución"}
]

# Variables de configuración
nombre_fichero = 'direcciones.csv'  # Nombre del archivo CSV
delimitador = ';'  # Especificar el caracter usado como delimitador
copiar_cabecera = True  # Establecer a True para copiar la cabecera

# Abrir y escribir en el archivo CSV
with open(nombre_fichero, mode='w', newline='', encoding='utf-8') as fichero:
    # Definir los nombres de las columnas
    campos = ['Tipo', 'CP', 'Municipio', 'Isla', 'Provincia', 'Calle']
    
    # Crear el objeto escritor con el delimitador especificado
    escritor = csv.DictWriter(fichero, fieldnames=campos, delimiter=delimitador)
    
    # Escribir la cabecera si se ha especificado en la variable
    if copiar_cabecera:
        escritor.writeheader()
    
    # Escribir los registros en el archivo
    for registro in registros:
        escritor.writerow(registro)

print(f"Fichero '{nombre_fichero}' creado y registros insertados correctamente.")