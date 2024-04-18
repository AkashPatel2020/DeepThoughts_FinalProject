# Function to display the group photo
def display_group_photo(photo_path):
    image = Image.open(photo_path)
    image.show()
