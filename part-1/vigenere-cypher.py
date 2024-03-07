text = 'mrttaqrhknsw ih puggrur'
custom_key = 'happycoding'

# a cypher which changes the encryption offset of a letter based on a key
def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            # define the offset based on the index of the key_char being used
            offset = alphabet.index(key_char)
            # define the index variable based on the index of the character we are working with in the alphabet string
            index = alphabet.find(char)
            # defining the new_index by adding the offset to the index modulated by the length of the alphabet string
            # the direction value will cause the offset to be added (encrypted) or subtracted (decrypted) from the index
            new_index = (index + offset*direction) % len(alphabet)
            # adding the encrypted/decrypted character to the final_message variable
            final_message += alphabet[new_index]
    
    return final_message

def encrypt(message, key):
    return vigenere(message, key)
    
def decrypt(message, key):
    return vigenere(message, key, -1)

print(f'\nEncrypted text: {text}')
print(f'Key: {custom_key}')
decryption = decrypt(text, custom_key)
print(f'\nDecrypted text: {decryption}\n')