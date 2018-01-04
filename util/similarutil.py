#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 使用编辑距离算法来寻找文本之间的相似性
import sys
sys.path.append('..')
import util.dateutil

reload(sys)
sys.setdefaultencoding('utf8')

#方法1（速度最慢）
def ld(str1,str2):
    n = len(str1)
    m = len(str2)

    ch1 = ''
    ch2 = ''
    temp = 0
    if(n == 0):
        return m
    if(m == 0):
        return n
    d = []
    for a in range(0,n+2):
        d.append([])
        for b in range(0,m+2):
            d[a].append(0)


    for i in range(0,n+1):
        d[i][0] = i
    for j in range(0,m+1):
        d[0][j] = j

    for i in range(1,n+1):
        ch1 = str1[i-1]
        for j in range(1,m+1):
            ch2 = str2[j-1]
            if(ch1 == ch2):
                temp = 0
            else:
                temp = 1
            d[i][j] = min(d[i-1][j]+1,d[i][j-1]+1,d[i-1][j-1]+temp)
    return d[n][m]

#相似度
def sim(str1,str2):
    try:
        a = levenshtein3(str1,str2)+0.0
        return (1-a/(float)(max(len(str1),len(str2))))
    except Exception as r:
        print 'error %s' % str(r)
        return 0.1

#方法2（速度居中）
def levenshtein2(s1, s2):
    if len(s1) < len(s2):
        return levenshtein2(s2, s1)

        # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[
                             j + 1] + 1  # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1  # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

#方法3（速度最快）
def levenshtein3(s, t):

    if s == t:
        return 0
    elif len(s) == 0:
        return len(t)
    elif len(t) == 0:
        return len(s)
    v0 = [None] * (len(t) + 1)
    v1 = [None] * (len(t) + 1)
    for i in range(len(v0)):
        v0[i] = i
    for i in range(len(s)):
        v1[0] = i + 1
        for j in range(len(t)):
            cost = 0 if s[i] == t[j] else 1
            v1[j + 1] = min(v1[j] + 1, v0[j + 1] + 1, v0[j] + cost)
        for j in range(len(v0)):
            v0[j] = v1[j]

    return v1[len(t)]

def main():

    str1 = "旷视科技有限公司"
    str2 = "旷视科技（北京）有限公司"
    begin = util.dateutil.get_milliseconds()
    for p in range(0,10000):
        ld(str1,str2)
    end = util.dateutil.get_milliseconds()
    print 'ld 使用时间 %d' % (end-begin)

    begin = util.dateutil.get_milliseconds()
    for p in range(0, 10000):
        levenshtein2(str1, str2)
    end = util.dateutil.get_milliseconds()
    print 'ld 使用时间 %d' % (end-begin)

    begin = util.dateutil.get_milliseconds()
    for p in range(0, 10000):
        levenshtein3(str1, str2)
    end = util.dateutil.get_milliseconds()
    print 'ld 使用时间 %d' % (end - begin)

#main()