import json  # Import the JSON module to work with JSON data
from cryptography.fernet import Fernet  # Import Fernet from the cryptography module for encryption/decryption
from PIL import Image  # Import Image module from the Python Imaging Library (PIL) for image processing

# Function to decrypt the location data
def decrypt_location(encrypted_data_file, english_file):
    # Open and load the encrypted location data from the JSON file
    with open(encrypted_data_file, 'r') as f:
        encrypted_data = json.load(f)

    # Open and read the English dictionary file
    with open(english_file, 'r', encoding='utf-8') as f:
        english_words = f.readlines()

    decrypted_location = ''
    # Decrypt each index to get the corresponding word from the English dictionary
    for index in encrypted_data:
        word_index = int(index) - 1
        decrypted_location += english_words[word_index].strip() + ' '

    return decrypted_location.strip()  # Return the decrypted location

# Function to decrypt the movie title
def decrypt_movie_title(encrypted_message, key):
    # Initialize the Fernet cipher with the provided key
    f = Fernet(key)
    # Decrypt the encrypted message using the Fernet cipher and decode it
    decrypted_message = f.decrypt(encrypted_message.encode()).decode('utf-8')
    return decrypted_message  # Return the decrypted movie title

# Function to display the group photo
def display_group_photo(photo_path):
    # Open the image file using PIL
    image = Image.open(photo_path)
    # Display the image
    image.show()

def main():
    # Decrypt the location data and print it
    location = decrypt_location("EncryptedGroupHints.json", "UCEnglish.txt")
    print("Decrypted Location:", location)

    # Decrypt the movie title
    with open("TeamsAndEncryptedMessagesForDistribution.json", 'r') as f:
        encrypted_data = json.load(f)
    encrypted_title = encrypted_data["YourTeamName"]  # Replace "YourTeamName" with your actual team name
    key = b'your_key_here'  # Replace with the actual key
    movie_title = decrypt_movie_title(encrypted_title, key)
    print("Decrypted Movie Title:", movie_title)

    # Display the group photo
    display_group_photo("group_photo.jpg")

if __name__ == "__main__":
    main()  # Execute the main function when the script is run directly