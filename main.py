import argparse
import os

from RSA_encryption import *



parser = argparse.ArgumentParser(prog="cipher")

sub_parsers = parser.add_subparsers()

key_parser = sub_parsers.add_parser("key", help="Generate key of given length")

key_parser.add_argument("length", type=int, help="Length of key in bits")

parser.add_argument("path", type=str, help="Path to file to encrypt/decrypt")
parser.add_argument("-e", "--encrypt", action="store_true")
parser.add_argument("-d", "--decrypt", action="store_true")

args = parser.parse_args()

print(args.length)

if os.path.exists(args.path):

    if args.encrypt or args.decrypt:

        key_pair = generate_key_pair(args.generate_key)

        if key_pair:

            private_key, public_key = key_pair

            if args.encrypt:
                encrypt(args.path, public_key)

            elif args.decrypt:
                decrypt(args.path, private_key)

        else:
            print("Cannot generate private and public key,\nprobably due to given key length")

    else:
        print("Please specify what You want to do with file: encrypt/decrypt")

else:
    print("Given path doesn't exists")