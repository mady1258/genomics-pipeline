import argparse, os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)
    with open(os.path.join(args.output, "dummy.txt"), "w") as f:
        f.write("PATRIC data placeholder\n")

if __name__ == "__main__":
    main()
