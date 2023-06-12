from PIL import Image

def resize_image(size1, size2):

    image = Image.open('image-test.jpg')
    print(f"Current size [{image.size}")

    resized_image = image.resize((size1, size2))
    resized_image.save('image-test '+str(size1)+'-'+str(size2)+'px.jpeg')

def main():

    size1 = int(input('Enter Width px: '))
    size2 = int(input('Enter Length px: '))
    resize_image(size1, size2)

if __name__ == '__main__':
    main()