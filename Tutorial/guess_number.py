import argparse as ap

while True:
    parser = ap.ArgumentParser()
    parser.add_argument("-n", "--name", metavar="name", required=True)
    args = parser.parse_args()
    print(f"{args.name}, guess which number I'm thinking of. 1, 2, or 3?")
