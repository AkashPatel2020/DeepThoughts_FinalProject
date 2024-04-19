# Name:Akash Patel and Bill Nicholson
# email:patel5a5@mail.uc.edu, nichodlw@mial.uc.edu
# Assignment Title: Assignment 11 Final Project
# Due Date:04/23/2024
# Course: IS 3050
# Semester/Year: Fall 2024
# File Name: DeepThoughts_FinalProject
# Brief Description of this file: We have drypetd the a location and the movie title, and also got a picture showing our qoute
# Citations:ChatGpt 
# Anything else that's relevant:
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
im = load_image("../GroupPacakge/Baribe.jpg")
