if __name__ == '__main__':
    n,m,c = map(int,raw_input().split())
    color_pos_dict = {}
    for index in range(n):
        each_list = map(int,raw_input().split())
        each_list = each_list[1:]
        for color in each_list:
            if color_pos_dict.has_key(color):
                color_pos_dict[color].append(index)
            else:
                color_pos_dict[color] = [index]
    count = 0
    for color in color_pos_dict:
        this_color_pos_list = color_pos_dict[color]
        if len(this_color_pos_list)==1:
            continue
        for index,this_pos in enumerate(this_color_pos_list):
            if index != len(this_color_pos_list)-1:
                if this_pos+m > this_color_pos_list[index+1]:
                    count += 1
                    break
            else:
                if (this_pos+m)%n > this_color_pos_list[0]:
                    count += 1
                    break
    print count