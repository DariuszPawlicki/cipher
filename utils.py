from pathlib import Path
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
from typing import Tuple, Union
from base64 import b64encode, b64decode



def generate_key_pair(bits: int):
    try:
        key = RSA.generate(bits)

        private_key = key.export_key("PEM")
        public_key = key.public_key().export_key("PEM")

        with open("private.pem", "w+") as file:
            file.write(private_key.decode("ascii"))
        
        with open("public.pem", "w+") as file:
            file.write(public_key.decode("ascii"))

    except Exception as err:
        print(err)


def load_key_pair() -> Union[Tuple[RSA.RsaKey, RSA.RsaKey], None]:
    if not Path("private.pem").is_file() or not Path("public.pem").is_file():
        print("\nCannot find public/private key file.\nGenerate keys first\n")
        return None
    else:
        with open("private.pem", "r") as file:
            private_key = RSA.import_key(file.read())
        
        with open("public.pem", "r") as file:
            public_key = RSA.import_key(file.read())
        
        return (private_key, public_key)
        

def get_file_content(file_path: str) -> str:
    with open(file_path, "r") as file:
        content = file.read()
    
    return content


def encrypt_file(file_path: str, public_key: RSA.RsaKey):
    content = b64encode(get_file_content(file_path).encode())

    cipher = PKCS1_v1_5.new(public_key)

    encrypted_content = b64encode(cipher.encrypt(content)).decode()

    with open(f"{Path(file_path).stem}_encrypted.txt", "w+") as file:
        file.write(encrypted_content)


def decrypt_file(file_path: str, private_key: RSA.RsaKey):
    content = b64decode(get_file_content(file_path).encode())

    cipher = PKCS1_v1_5.new(private_key)

    encrypted_content = b64decode(cipher.decrypt(content, 16)).decode()

    with open(f"{Path(file_path).stem}_decrypted.txt", "w+") as file:
        file.write(encrypted_content)