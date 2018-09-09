#coding=utf-8
if __name__ == '__main__':
    input_str = raw_input()
    front = 0
    back = 1
    res_len = 1
    while back<len(input_str):
        exit_flag = False
        for each in range(front,back):
            if input_str[back]==input_str[each]:
                tmp_len = back-front
                front = back
                back += 1
                exit_flag = True
                break
        if not exit_flag:
            back += 1
            tmp_len = back-front
        if tmp_len>res_len:
            res_len = tmp_len
    if len(input_str)==1:
        print 1
    elif len(input_str)==0:
        print 0
    else:
        print res_len
#通过了80%的测试用例,尽力了