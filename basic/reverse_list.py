l = [1,2,3,4,5,6,7,8,9]


l = [ 'a', (1,2), None, 2, 3]
# def print_reverse(l):
#     state = len(l)
#     print(state)
#     i = 0
#     new_l = []
#     while i < len(l):
#         new_l.append(state)
#         state = state - 1
#         i = i + 1
#     print(new_l) 
# print_reverse(l)

# def print_reverse(l):
#     print(l[::-1])

def print_reserve(l):
    final_list = []
    for i in range(len(l)):
        if i > 0 :
            final_list.append(i)
    print(final_list)

print_reserve(l)
    