# sample code for using arguments in case of calling python code from cmd.

import argparse

def main(args):

    print(f"file location: {args.argument_name}")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Argument description here.')
    parser.add_argument("--argument_name",
                        type=Path,
                        required=True,
                        help="help text")

    args = parser.parse_args()

    start = main(args)
