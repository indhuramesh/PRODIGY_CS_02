from PIL import Image

def encrypt_image(image_path, key):
    try:
        img = Image.open(image_path)
        width, height = img.size
        encrypted_pixels = []
        
        for y in range(height):
            for x in range(width):
                pixel = img.getpixel((x, y))
                encrypted_pixel = tuple((p + key) % 256 for p in pixel)
                encrypted_pixels.append(encrypted_pixel)
        
        encrypted_img = Image.new(img.mode, img.size)
        encrypted_img.putdata(encrypted_pixels)
        encrypted_img.save("encrypted_image.png")
        print("Image encrypted successfully!")
    except Exception as e:
        print("An error occurred:", e)

def decrypt_image(encrypted_image_path, key):
    try:
        img = Image.open(encrypted_image_path)
        width, height = img.size
        decrypted_pixels = []
        
        for y in range(height):
            for x in range(width):
                pixel = img.getpixel((x, y))
                decrypted_pixel = tuple((p - key) % 256 for p in pixel)
                decrypted_pixels.append(decrypted_pixel)
        
        decrypted_img = Image.new(img.mode, img.size)
        decrypted_img.putdata(decrypted_pixels)
        decrypted_img.save("decrypted_image.png")
        print("Image decrypted successfully!")
    except Exception as e:
        print("An error occurred:", e)

def main():
    while True:
        choice = input("Choose 'E' for encryption, 'D' for decryption, or 'Q' to quit: ").upper()
        if choice == 'Q':
            print("Exiting program.")
            break
        elif choice == 'E':
            image_path = input("Enter the path of the image to encrypt: ")
            key = int(input("Enter the encryption key: "))
            encrypt_image(image_path, key)
        elif choice == 'D':
            encrypted_image_path = input("Enter the path of the encrypted image to decrypt: ")
            key = int(input("Enter the decryption key: "))
            decrypt_image(encrypted_image_path, key)
        else:
            print("Invalid choice. Please enter 'E', 'D', or 'Q'.")


if __name__ == "__main__":
    main()
