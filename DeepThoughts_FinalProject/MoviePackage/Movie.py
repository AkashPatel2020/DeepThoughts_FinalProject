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
