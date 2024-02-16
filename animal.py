import sys
def default():
    print("Hello")

def dog():
    print("Bark")

def main():
    if sys.argv[1]=='dog':
        print("dog")

if __name__ == '__main__':
    main()
