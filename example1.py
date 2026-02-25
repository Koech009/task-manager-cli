import argparse

parser = argparse.ArgumentParser(description="Simple greeting program")
parser.add_argument("name", help="Enter your name")
args = parser.parse_args()

print(f"Hello {args.name}")
