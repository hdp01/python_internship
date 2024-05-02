from image_processing import load_image, grayscale_image, save_image, invert_image, resize_image

def main():
    # Load an image
    image = load_image("images/porche.jpg")
    
    # Invert the image
    inverted_image = invert_image(image)
    
    # Resize the image to a new size
    new_size = (200, 200)
    resized_image = resize_image(inverted_image, new_size)

    # Convert the image to grayscale
    grayscale_image1 = grayscale_image(resized_image)

    # Save the processed image
    save_image("images/porche123.jpg", grayscale_image1)

if __name__ == "__main__":
    main()