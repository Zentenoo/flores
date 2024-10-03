from PIL import Image

def remove_background(image_path, output_path):
    # Abre la imagen
    image = Image.open(image_path)

    # Convierte la imagen a RGBA (por si acaso no tiene canal alfa)
    image = image.convert("RGBA")

    # Obtiene los datos de la imagen
    data = image.getdata()

    # Define el color de fondo (en este caso el verde con RGB (92, 139, 126))
    background_color = (92, 139, 126, 255)  # Color a eliminar

    new_data = []
    for item in data:
        # Si el píxel coincide con el color del fondo, lo hace transparente
        if item == background_color:
            new_data.append((255, 255, 255, 0))  # Píxel transparente
        else:
            new_data.append(item)

    # Aplica los nuevos datos a la imagen
    image.putdata(new_data)

    # Guarda la imagen con fondo transparente
    image.save(output_path, "PNG")
    print(f"Imagen guardada sin fondo en: {output_path}")

# Usa la función
input_image_path = "C:/Users/PC/OneDrive/Escritorio/tulipan/14-31-36-345_512.png"  # Cambia esta ruta por la de tu imagen
output_image_path = "C:/Users/PC/OneDrive/Escritorio/tulipan/imagen_sin_fondo.png"  # Cambia esta ruta para guardar la imagen
remove_background(input_image_path, output_image_path)
