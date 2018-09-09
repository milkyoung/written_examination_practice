#coding=utf-8
if __name__ == '__main__':
    input_str = raw_input()
    # if len(input_str)==4:
    #     print 1
    count = 0
    for length1 in range(1,4):
        if len(input_str)-length1<3:
            continue
        first = input_str[0:length1]
        if int(first)>255:
            continue
        left1 = input_str[length1:]
        for length2 in range(1,4):
            left = left1
            if len(left) - length2 < 2:
                continue
            second = left[0:length2]
            if int(second) > 255:
                continue
            if int(second) < (len(second)-1)*10:
                continue
            left = left[length2:]
            left2 = left
            for length3 in range(1, 4):
                left = left2
                if len(left) - length3 < 1:
                    continue
                third = left[0:length3]
                if int(third) > 255:
                    continue
                if int(third) < (len(third)-1)*10:
                    continue
                left = left[length3:]
                if int(left) > 255:
                    continue
                if int(left) < (len(left)-1)*10:
                    continue
                count += 1
                print 'first',first,'second',second,'third',third,'last',left
    print count

#考试的时候最高通过率是40%
#现在这个是修改后的版本，看情况吧