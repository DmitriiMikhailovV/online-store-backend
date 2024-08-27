import os
import base64


def convert_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def process_images_in_directory(directory_path):
    for filename in os.listdir(directory_path):
        if filename.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".bmp")):
            image_path = os.path.join(directory_path, filename)
            image_base64 = convert_image_to_base64(image_path)
            text_file_path = os.path.join(
                directory_path, f"{os.path.splitext(filename)[0]}.txt"
            )
            with open(text_file_path, "w") as text_file:
                text_file.write(image_base64)
            print(
                f"Created {text_file_path} with Base64 encoding of {filename}"
            )


directory_path = "media/product_images"
process_images_in_directory(directory_path)
