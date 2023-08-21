import sys
def main():
    check_lines()
    try:
        folder = open(sys.argv[1] , "r")
        lines=folder.readlines()
    except:
        sys.exit("File does not exist")
    count = 0
    for line in lines:
        if check_line_lines(line) == False:
            count +=1
    print(count)

def check_lines():
    if len(sys.argv)<2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv)>2:
        sys.exit("Too many command-line arguments")

    if ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")
def check_line_lines(line):
    if line.isspace():
        return True
    if line.lstrip().startswith("#"):
        return True
    return False
if __name__ == "__main__":
    main()