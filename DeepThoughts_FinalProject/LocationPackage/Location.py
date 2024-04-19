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
import json

def decrypt_location(encrypted_data_file, english_file):
    """
    Decrypts the location data using the provided encrypted data file and English words file.

    Parameters:
    - encrypted_data_file (str): The path to the JSON file containing encrypted data.
    - english_file (str): The path to the file containing English words.

    @Returns:
    decrypted_location (str): The decrypted location.
    """
    # Load encrypted data from file
    with open(encrypted_data_file, 'r') as f:
        encrypted_data = json.load(f)
    
    # Extract encrypted location data
    myLoc = encrypted_data["Deep Thought"]
    
    # Read English words from file
    with open(english_file, 'r', encoding='utf-8') as f:
        english_words = f.readlines()
    
    decrypted_location = ''
    # Decrypt each index in myLoc
    for index in myLoc:
        word_index = int(index)
        decrypted_location += english_words[word_index].strip() + ' '
    
    # Return decrypted location
    return decrypted_location.strip()

