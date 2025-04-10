from PIL import Image
import os

def encrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    pixels = image.load()

    width, height = image.size
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y][:3]  # Ignore alpha if present
            pixels[x, y] = (
                (r + key) % 256,
                (g + key) % 256,
                (b + key) % 256
            )
    image.save(output_path)
    print(f"Encrypted image saved as {output_path}")

def decrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    pixels = image.load()

    width, height = image.size
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y][:3]
            pixels[x, y] = (
                (r - key) % 256,
                (g - key) % 256,
                (b - key) % 256
            )
    image.save(output_path)
    print(f"Decrypted image saved as {output_path}")

def main():
    print("Image Encryption Tool")
    action = input("Choose action (encrypt/decrypt): ").strip().lower()
    input_path = input("Enter input image path: ").strip()
    output_path = input("Enter output image path: ").strip()
    key = int(input("Enter encryption key (number): "))

    if not os.path.exists(input_path):
        print("Error: File not found.")
        return

    if action == "encrypt":
        encrypt_image(input_path, output_path, key)
    elif action == "decrypt":
        decrypt_image(input_path, output_path, key)
    else:
        print("Invalid action. Use 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
