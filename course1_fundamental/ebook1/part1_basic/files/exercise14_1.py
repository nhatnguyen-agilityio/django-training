def sed(str, replace_str, filename1, filename2):
    try:
        fin = open(filename1, "r")
        fout = open(filename2, "w")
        for line in fin:
            line = line.replace(str, replace_str)
            fout.write(line)
        fin.close()
        fout.close()
    except:
        print("Something went wrong!")

string1 = "long"
replace_str = "short"
file1 = "chapter14.txt"
file2 = "out_file.txt"
sed(string1, replace_str, file1, file2)
            