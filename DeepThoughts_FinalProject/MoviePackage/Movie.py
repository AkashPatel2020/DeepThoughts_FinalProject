from cryptography.fernet import Fernet
# Function to decrypt the movie title
def decrypt_movie_title(encrypted_message, key):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message.encode()).decode('utf-8')
    return decrypted_message
