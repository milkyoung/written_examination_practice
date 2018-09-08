#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    n = int(raw_input())
    like_list = map(int,raw_input().split())
    if len(like_list)!=n:
        print 'error'
    like_pos_dict = {}
    for index,each_like in enumerate(like_list):
        if like_pos_dict.has_key(each_like):
            like_pos_dict[each_like].append(index)
        else:
            like_pos_dict[each_like] = [index]
    q = int(raw_input())
    for each_q in range(q):
        l,r,k = map(int,raw_input().split())
        if like_pos_dict.has_key(k):
            show_list = like_pos_dict[k]
        else:
            show_list = []
        count=0
        for each in show_list:
            if l-1<=each<=r-1:
                count += 1
        print count