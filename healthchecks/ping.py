#!/usr/bin/env python

import argparse
import socket
import urllib.request
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument("url", type=str, help="Url to ping.")


def main(args):
    try:
        with urllib.request.urlopen(args.url, timeout=10) as _:
            print(datetime.now())
    except socket.error as error_:
        print(f"Ping failed: {error_}")


if __name__ == "__main__":
    main(parser.parse_args())
