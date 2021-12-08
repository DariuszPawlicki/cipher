import Crypto

from Crypto.PublicKey import RSA
from Crypto import Random
from typing import Tuple, Union



def generate_key_pair(bits: int) -> Union[Tuple, None]:
    try:
        key = RSA.generate(bits)

        private_key = key.export_key("PEM")
        public_key = key.public_key().export_key("PEM")

        return (private_key, public_key)

    except Exception as err:
        print(err)
        return


def get_file_content(file_path: str) -> str:
    with open(file_path, "r") as file:
        content = file.read()
    
    return content


def encrypt(file_path: str, public_key: RSA.RsaKey):
    content = get_file_content(file_path)

    content = str.encode(content)


def decrypt(file_path: str, private_key: RSA.RsaKey):
    pass