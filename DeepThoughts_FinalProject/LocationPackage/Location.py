import json
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

