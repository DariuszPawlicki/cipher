import click

from pathlib import Path
from utils import *



@click.group()
def main():
    pass


@main.command()
@click.option("-e", "--encrypt", is_flag=True, help="Encrypts specified file and writes it's content to a new file.")
@click.option("-d", "--decrypt", is_flag=True, help="Decrypts specified file and writes it's content to a new file.")
@click.argument("path", type=str)
def exec(encrypt, decrypt, path):

    if Path(path).is_file():
        keys = load_key_pair()

        if not keys:
            return
        
        private_key, public_key = keys

        if encrypt:
            encrypt_file(path, public_key)
        elif decrypt:
            decrypt_file(path, private_key)
        else:
            print("\nChoose what to do with file: encrypt/decrypt\n")

    else:
        print("\nGiven file doesn't exists\n")


@main.command()
@click.argument("length", type=int)
def key(length):
    generate_key_pair(length)


if __name__ == "__main__":
    main()