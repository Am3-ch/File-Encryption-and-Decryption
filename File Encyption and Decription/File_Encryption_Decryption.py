from cryptography.fernet import Fernet

#key = Fernet.generate_key()

#============= Encryption ===========================:)
def encrypt(file):
    with open('myKey.key','rb') as myKey:
        key = myKey.read()

    key_object = Fernet(key)
    
    with open(file, 'rb') as plain_file:
        plain_text = plain_file.read()

    encrypted_text = key_object.encrypt(plain_text)

    with open('enc_' + file, 'wb') as enc_file:
        enc_file.write(encrypted_text)

#=================== Decryption ======================:)
def decrypt(file):
    # Our key
    with open('myKey.key','rb') as myKey:
        key = myKey.read()

    key_object = Fernet(key)

    # the file we will be reading from
    with open(file, 'rb') as encrypted_file:
        new_encrypted_text = encrypted_file.read()
        decrypted_text = key_object.decrypt(new_encrypted_text)

    # The file we will be writing to
    with open('decrypted_'+ file, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_text)


#================= Time for magic and safety ==============================:)
while True:  
    print("==========================================================================")  
    print(">>     Hello, welcome to Fernet file encryption/decrypton!!    <<")
    print("==========================================================================")
    option = input("Please pick an option, enter \ne) for encrytion \nd) for decryption\n:> " )
    if option == "e":
        plain_text_file = input("Enter file name that you want to encrypt: ")
        encrypt(plain_text_file)
        print("File encrypted successifuly!!")
        break
    elif option == "d":
        encrypted_text_file = input("Enter file name that you want to decrypt: ")
        decrypt(encrypted_text_file)
        print("File dencrypted successifuly!!")
        break
    else:
        print("Please enter a valid option")
