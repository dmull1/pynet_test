#!/usr/bin/env python

my_list = range(7)
my_list.append('something')
my_list.append('nothing')
print my_list.pop(3)

print "Length of list: {}".format(len(my_list))
my_list.sort()
print my_list
