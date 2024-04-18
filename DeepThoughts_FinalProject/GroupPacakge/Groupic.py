from PIL import Image

def load_image(filename):
    '''
    Load an image file from disk
    @param: filename The file to load
    @return: the image object or None if an error occurred
    '''
    try:
        myimage = Image.open(filename)
    except:
        # If an exception occurs, return None
        return None
    myimage.load()
    return myimage

# Open an image file. The default path is where this python module is
im = load_image("../GroupPacakge/birds.jpg")
if im:
    print(im.width, im.height, im.mode, im.format)
else:
    print("Failed to open image")