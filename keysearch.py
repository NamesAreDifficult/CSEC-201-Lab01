"""
Lab 1 Part 1: Brute Forth Key Search
Authors: 
CSEC faculty
Put your name here
"""

from cryptography.fernet import Fernet
import base64  
import time

def key_search(message, enc_message):
    """
    Brute force key source search
    A key source string is a sequence of 32 ascii characters 
    from which a symmetric key (used for both encryption and 
    decryption) is generated. 
    To reduce the search time complexity for the lab, the 
    first 29 characters have been set to "A"*29. You only 
    need to find the last three charactgers whose ascii code 
    is in the range 65-126.  
    Parameters:
    message: original plaintex
    enc_message: ciphertext to be decrypted
    Return:
    The key source string used to encrypt/decrypt message 
    """
    for i1 in range(65, 127): 
        for i2 in range(65, 127):
            for i3 in range(65, 127):    
                key_source = "A"*29 + chr(i1)+chr(i2)+chr(i3)   
                dec_message = decrypt(enc_message, key_source)
                if dec_message == message.encode():
                    return key_source
    return 'no key source found'

def encrypt(message, key_source):
    # Generate a key for encryption
    key = base64.urlsafe_b64encode(key_source.encode()) 
    # Create an instance the Fernet class with the key
    fernet = Fernet(key)
    # Use the instance to encrypt message 
    enc_message = fernet.encrypt(message.encode())
   
    return enc_message

def decrypt(enc_message, key_source):
    # Generate a key for decryption
    key = base64.urlsafe_b64encode(key_source.encode())

    # Create an instance the Fernet class with the key
    fernet = Fernet(key)

    # Use the instance to decrypt message 
    # If successfully decrypted you will receive the original 
    # plaintext as the result, 
    # otherwise an exception will be raised. 
 
    dec_message = fernet.decrypt(enc_message) 
    return dec_message
    
# Demonstrate how the encryption and decryption functions are used
def enc_dec():
    key_source = 'A'*29+'abc'  # Any string of length 32 should work
    message = "Hello, Welcome to CSEC 201!"

    enc_message = encrypt(message, key_source) 
    print(f"enc_message = {enc_message}")
    
    dec_message = decrypt(enc_message, key_source)
    print(f"dec_message = {dec_message}")


if __name__ == "__main__":
    
    enc_dec() 

    """
    Once you undestand encryption/decryption have the time to experiment,
    1. Comment out the call to enc_dec() 
    2. Uncomment the following lines to start lab 1 part 1
    """

    # message = "Hello, Welcome to CSEC 201!"
    # enc_message = b'gAAAAABhC01A7xgSLLzoZ_DD-WtMtmawT4dwB-R2UOmsBowJqBOS0HWjx42rcIVFx_3bMdtJlH0zLFVLdTx3mx5F8K1I3k0ykoYX5M0eeZuJgeff82KPoGY='
    # print('Slow search starts...')
    # start = time.perf_counter()
    # key_source = key_search(message, enc_message)
    # print(f"key source found is {key_source}")
    # end = time.perf_counter()
    # print(f'Slow search is done in {round(end-start, 2)} seconds')
  
