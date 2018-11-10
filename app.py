import sys
from pks_app.reverse_hash import reverse_hash


if __name__ == '__main__':
    try:
        arg = int(sys.argv[1])
        print(reverse_hash(arg))
    except (TypeError, ValueError):
        print('Argument should be of Integer type')
