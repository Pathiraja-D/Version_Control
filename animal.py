import sys
def default():
    print("Hello")

def dog():
    print("Bark")

def cat():
    print("Hello Cat")

def main():
    if sys.argv[1]=='dog':
        print("dog")
    elif sys.srgv[1]=='cat'
	print("cat")
    else:
	default()
if __name__ == '__main__':
    main()
