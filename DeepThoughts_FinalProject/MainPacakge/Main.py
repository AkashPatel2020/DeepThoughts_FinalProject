import json
from LocationPackage.Location import*
from MoviePackage.Movie import*
from GroupPacakge.Groupic import*
from cryptography.fernet import Fernet
from PIL import Image


def main():
    # Decrypt the location data and print it
    location = decrypt_location("EncryptedGroupHints Spring 2024 Section 002.json", "UCEnglish.txt")
    print("Decrypted Location:", location)

    # Decrypt the movie title
    with open("TeamsAndEncryptedMessagesForDistribution - 002.json", 'r') as f:
        encrypted_data = json.load(f)
    encrypted_title = encrypted_data["Deep Thought"][0]  # Assuming it's a list, access the first element
    key = "t7WyuS-VCj3eb9HE0OHPhva2b30FSid88Z5nSiYUo0c="
    movie_title = decrypt_movie_title(encrypted_title, key)
    print("Decrypted Movie Title:", movie_title)

    
 
    # Load the image
    image = load_image("../GroupPacakge/birds.jpg")

    # Check if image loaded successfully
    if image:
        # Display the image
        image.show()
   

   
   

if __name__ == "__main__":
    main()