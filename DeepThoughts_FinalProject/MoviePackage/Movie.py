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
from cryptography.fernet import Fernet

def decrypt_movie_title(encrypted_message, key):
    """
    Decrypts the encrypted movie title using the provided key.

    Parameters:
    - encrypted_message (str): The encrypted message to decrypt.
    - key (str): The key used for decryption.

    @Returns 
     : The decrypted movie title.
    """
    # Create a Fernet cipher object with the provided key
    f = Fernet(key)
    
    # Decrypt the encrypted message and decode it to UTF-8 format
    decrypted_message = f.decrypt(encrypted_message.encode()).decode('utf-8')
    
    # Return the decrypted movie title
    return decrypted_message
