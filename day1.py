import numpy as np
if __name__ == '__main__':
    path_input_txt = r"C:\Workspace\adventofcode\d1\input.txt"
    output = np.genfromtxt(path_input_txt, dtype=str,
                     encoding='utf-8', delimiter="\n\n")

    a_file = open(path_input_txt, 'r')
    string_with_breaks = a_file.read()
    a_file.close()
    string_without_line_breaks = string_with_breaks.replace('\n\n',',,')
    string_without_line_breaks = string_without_line_breaks.replace('\n','-')

    b = str.split(string_without_line_breaks,',,')
    line_count_kst= []
    for item in list(b):
        line_count = item.split('-')
        temp_count = 0
        for count in line_count:
            try:
                temp_count+=int(count)
            except:
                continue
        line_count_kst.append(temp_count)
    line_count_kst = sorted(line_count_kst)
    print(sum(line_count_kst[-3:]))