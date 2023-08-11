def main(filename='words.txt'):
    fin = open(filename)
    for line in fin:
        word = line.strip()
        if len(word) > 20:
            print(line)

if __name__ == '__main__':
    main()