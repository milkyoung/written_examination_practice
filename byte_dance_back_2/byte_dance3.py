if __name__ == '__main__':
    string,m = raw_input().split()
    m = int(m)
    alpha_pos_dict = {}
    for pos_index,alpha in enumerate(string):
        if alpha_pos_dict.has_key(alpha):
            alpha_pos_dict[alpha].append(pos_index)
        else:
            alpha_pos_dict[alpha] = [pos_index]
    res = 0
    for alpha in alpha_pos_dict:
        pos_list = alpha_pos_dict[alpha]
        if len(pos_list)<=res:
            continue
        for pos_index,pos in enumerate(pos_list):
            # print 'now is',alpha,'at',pos_list[pos_index]
            left_index = pos_index
            right_index = pos_index
            left = pos
            right = pos
            cost = 0
            tmp_res = 1
            while cost<=m:
                if left_index>0 and right_index<len(pos_list)-1:
                    if left-pos_list[left_index-1]>pos_list[right_index+1]-right:
                        cost += pos_list[right_index+1]-right-1
                        if cost>m:
                            break
                        tmp_res += 1
                        right_index += 1
                        right += 1
                    else:
                        cost += left - pos_list[left_index-1] - 1
                        if cost > m:
                            break
                        tmp_res += 1
                        left_index -= 1
                        left -= 1
                elif left_index==0 and right_index<len(pos_list)-1:
                    cost += pos_list[right_index + 1] - right - 1
                    if cost > m:
                        break
                    tmp_res += 1
                    right_index += 1
                    right += 1
                elif left_index > 0 and right_index == len(pos_list) - 1:
                    cost += left - pos_list[left_index - 1] - 1
                    if cost > m:
                        break
                    tmp_res += 1
                    left_index -= 1
                    left -= 1
                else:
                    break
            # print 'and the tmp_res is',tmp_res
            if tmp_res>res:
                res = tmp_res
    print res