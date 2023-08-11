import os

def list_files(dirname):
    all_files = []
    for file in os.listdir(dirname):
        full_path = os.path.join(dirname, file)
        if os.path.isfile(full_path):
            all_files.append(full_path)
        else:
            all_files.extend(list_files(full_path))

    return all_files

def check_files(all_files):
    dict_duplicate = {}
    for file in all_files:
        if file.endswith(".txt"):
            cmd = 'md5sum ' + file
            fp = os.popen(cmd)
            res = fp.read()
            stat = fp.close()
            if res in dict_duplicate:
                dict_duplicate[res].append(file)
            else:
                dict_duplicate[res] = [file]
    return dict_duplicate

cwd = os.getcwd()
all_files = list_files(cwd)
for item in check_files(all_files):
    print(item)
