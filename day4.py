if __name__ == '__main__':
    path_input_txt = r"C:\Workspace\adventofcode\day4.txt"
    # Part 1
    a_file = open(path_input_txt, 'r')
    list_of_items = a_file.read()
    a_file.close()
    list_of_items = list_of_items.split('\n')
    count_num_overlap = 0
    count_num_overlap_part2 = 0
    for item in list_of_items:
        if item == '':
            continue
        split_by_comma =item.split(',')
        range1 = split_by_comma[0]
        range2 = split_by_comma[1]
        first_digit = int(range1.split('-')[0])
        second_digit = int(range1.split('-')[1])
        range2_first_digit = int(range2.split('-')[0])
        range2_second_digit = int(range2.split('-')[1])
        # part 1
        if range2_first_digit in range(first_digit, second_digit+1) and range2_second_digit in range(first_digit, second_digit+1):
            count_num_overlap+=1
        elif first_digit in range(range2_first_digit, range2_second_digit+1) and second_digit in range(range2_first_digit, range2_second_digit+1):
            count_num_overlap+=1
        # part 2
        if range2_first_digit in range(first_digit,second_digit+1):
            count_num_overlap_part2+=1
            continue
        elif range2_second_digit in range(first_digit,second_digit+1):
            count_num_overlap_part2+=1
            continue
        elif first_digit in range(range2_first_digit,range2_second_digit+1):
            count_num_overlap_part2+=1
            continue
        elif second_digit in range(range2_first_digit,range2_second_digit+1):
            count_num_overlap_part2+=1
            continue
    print(count_num_overlap)
    print(count_num_overlap_part2)
