import argparse
parser = argparse.ArgumentParser(description="This is a sample program")

parser.add_argument('-a', action="store_true", default=False)
parser.add_argument('-b', action="store", dest="b")
parser.add_argument('-c', action="store", dest='C', type=int)

print parser.parse_args(['-a', '-bval', '-c', '3'])
