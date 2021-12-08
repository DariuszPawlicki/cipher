import click
import os

from RSA_encryption import *



@click.group()
def main():
    pass


@main.command()
@click.option("-e", "--encrypt", is_flag=True, help="Encrypts specified file and writes it's content to new file.")
@click.option("-d", "--decrypt", is_flag=True, help="Decrypts specified file and writes it's content to new file.")
@click.argument("path", type=str)
def exec(encrypt, decrypt, path):

    if os.path.exists(path):

        if encrypt:
            pass
        elif decrypt:
            pass
        else:
            pass

    else:
        print("Given file doesn't exists")


@main.command()
@click.argument("length", type=int)
def key(length):
    pass


if __name__ == "__main__":
    main()