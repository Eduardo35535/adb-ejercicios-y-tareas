import csv

# Definir los datos para los registros
registros = [
    {"Producto": "Portátil Acer Aspire", "Categoría": "Electrónica", "Precio": "650 €", "Existencias": "20"},
    {"Producto": "Auriculares Sony", "Categoría": "Audio", "Precio": "300 €", "Existencias": "15"},
    {"Producto": "iPhone 14", "Categoría": "Telefonía", "Precio": "1100 €", "Existencias": "10"},
    {"Producto": "Lavadora LG 8kg", "Categoría": "Electrodomésticos", "Precio": "400 €", "Existencias": "8"},
    {"Producto": "Bicicleta de carretera", "Categoría": "Deportes", "Precio": "750 €", "Existencias": "12"},
    {"Producto": "Televisor inteligente Samsung de 55\"", "Categoría": "Televisión", "Precio": "900 €", "Existencias": "7"},
    {"Producto": "Cama King Size", "Categoría": "Muebles", "Precio": "1200 €", "Existencias": "5"},
    {"Producto": "Mesa de comedor", "Categoría": "Hogar", "Precio": "350 €", "Existencias": "6"},
    {"Producto": "Zapatos deportivos Nike", "Categoría": "Moda", "Precio": "80 €", "Existencias": "50"},
    {"Producto": "Cafetera Nespresso", "Categoría": "Cocina", "Precio": "150 €", "Existencias": "25"}
]

# Variables de configuración
nombre_fichero = 'productos.csv'  # Nombre del archivo CSV
delimitador = '.'                  # Especificar el carácter usado como delimitador
copiar_cabecera = False            # Establecer a False para no copiar la cabecera

# Abrir y escribir en el archivo CSV
with open(nombre_fichero, mode='w', newline='', encoding='utf-8') as fichero:
    # Crear el objeto escritor con el delimitador especificado
    escritor = csv.DictWriter(fichero, fieldnames=registros[0].keys(), delimiter=delimitador)
    
    # Escribir los registros en el archivo sin cabecera
    for registro in registros:
        escritor.writerow(registro)

print(f"Fichero '{nombre_fichero}' creado y registros insertados correctamente.")
