from parser import CommandProcessor

def main():
    cp = CommandProcessor()
    cp.execute_file("artifact.txt")

if __name__ == "__main__":
    main()
