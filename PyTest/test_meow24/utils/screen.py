from PIL import Image, ImageChops

def compare_img(img1_path,img2_path):
    img1 = Image.open(img1_path)
    img2 = Image.open(img2_path)
    
    diff = ImageChops.difference(img1,img2)
    print(diff)
    
    if diff.getbbox() == None:
        return True
    else:
        return False