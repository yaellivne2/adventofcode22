if __name__ == '__main__':
    path_input_txt = r"C:\Workspace\adventofcode\day3.txt"
    # Part 1
    a_file = open(path_input_txt, 'r')
    list_of_items = a_file.read()
    a_file.close()
    list_of_items = list_of_items.split('\n')
    temp_sum = 0
    for item in list_of_items:

        middle_item = int(len(item)/2)
        item_part_one = item[:middle_item]
        item_part_two = item[middle_item:]
        try:
            letter_in_both = [i for i in item_part_one if i in item_part_two][0]
            if ord(letter_in_both)>=97: # small letter
                temp_sum+= ord(letter_in_both)-96


            else: # cap letter
                temp_sum+= ord(letter_in_both)-64+26
        except:
            continue
    print(temp_sum)

    # part 2
    index_3 = 0
    n = len(list_of_items)
    temp_sum = 0
    while index_3 < n-3:
        person1 = list_of_items[index_3]
        person2 = list_of_items[index_3+1]
        person3 = list_of_items[index_3+2]
        letter_in_both = [i for i in person1 if i in person2 and i in person3][0]
        try:
            if ord(letter_in_both) >= 97:  # small letter
                temp_sum += ord(letter_in_both) - 96
            else:  # cap letter
                temp_sum += ord(letter_in_both) - 64 + 26
        except:
            continue
        index_3 += 3

    print(temp_sum)


