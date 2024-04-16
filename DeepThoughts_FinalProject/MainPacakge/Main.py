import json
from cryptography.fernet import Fernet
from PIL import Image

# Function to decrypt the location data
def decrypt_location(encrypted_data_file, english_file):
    with open(encrypted_data_file, 'r') as f:
        encrypted_data = json.load(f)
    myLoc = encrypted_data["Deep Thought"]
    with open(english_file, 'r', encoding='utf-8') as f:
        english_words = f.readlines()
    decrypted_location = ''
    for index in myLoc:
        word_index = int(index)
        decrypted_location += english_words[word_index].strip() + ' '
    return decrypted_location.strip()

# Function to decrypt the movie title
def decrypt_movie_title(encrypted_message, key):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message.encode()).decode('utf-8')
    return decrypted_message

# Function to display the group photo
def display_group_photo(photo_path):
    image = Image.open(photo_path)
    image.show()

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

    # Display the group photo
    display_group_photo("group_photo.jpg")

if __name__ == "__main__":
    main()