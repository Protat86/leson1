import sys

def print_square(number):
    try:
        number = int(number)
        print(f"Квадрат числа {number} дорівнює {number ** 2}")
    except ValueError:
        print("Будь ласка, введіть коректне ціле число.")

def print_help():
    help_message = """
usage: square.py number [-h]

positional arguments:
  number         display a square of a given number

options:
  -h | --help    show this help message and exit
"""
    print(help_message)

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print_help()
    else:
        print_square(sys.argv[1])
