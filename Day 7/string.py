def split_and_join(line):
    # split the string into words
    words = line.split()
    # join with hyphen
    return "-".join(words)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
