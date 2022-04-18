from PIL import Image
img=Image.open("1.jpg")
black_white=img.convert("L")
black_white.save("result_img.jpg")