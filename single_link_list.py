import sys

class ListObject:

    def __init__(self, data):
        self.data = data
        self.next_obj = None

    def link(self, obj):
        self.next_obj = obj

lst_in = list(map(str.strip, sys.stdin.readlines()))
object_list = []

for i in range(len(lst_in))[::-1]:
    
    if object_list:
        obj = ListObject(lst_in[i])
        obj.link(object_list[-1])
        object_list.append(obj)
    else:
        obj = ListObject(lst_in[i])
        object_list.append(obj)

head_obj = object_list[-1]

print(object_list[0].next_obj)
