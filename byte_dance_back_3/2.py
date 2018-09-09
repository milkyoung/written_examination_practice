#coding=utf-8
def if_near(group_node,each_node):
    if group_node[0]==each_node[0] and abs(group_node[1]-each_node[1])==1 \
            or group_node[1]==each_node[1] and abs(group_node[0]-each_node[0])==1:
        return True
    else:
        return False

if __name__ == '__main__':
    m = int(raw_input())
    show_list = []
    group_list = []
    for row_index in range(m):
        row_list = map(int,raw_input().split())
        for col_index,each in enumerate(row_list):
            if each==1:
                show_list.append((row_index,col_index))
    for each_node in show_list:
        find_flag = False
        for group in group_list:
            for group_node in group:
                if if_near(group_node,each_node):
                    group.append(each_node)
                    find_flag = True
                    break
            if find_flag:
                break
        if not find_flag:
            group_list.append([each_node])
    print len(group_list)
#存在语法错误或者数组越界非法访问的情况 通过80%