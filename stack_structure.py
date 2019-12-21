# keys_state = 0
def push(data,value):
    # global keys_state
    queue_dict.update({data : value})
    # keys_state = keys_state +  1


def pop():
    if len(queue_dict) > 0:
        for (k, v) in queue_dict.items():
            if v == max(queue_dict.values()):
                to_pop = k
        return queue_dict.pop(to_pop)
        # return queue_dict.pop(key for (key, value) in queue_dict.items() if value == max(queue_dict.values()))
    return "stack  dictionary Empty!"


# def deque_max(data):
#     return data.pop(max(data)) if type(data) == "list" else data.pop(max(data.keys()))

def pop_max(data):
    if type(data) not in [list, dict]:
        return f"a list type is required, your input has a  {type(data)}, with  {data}"
    return data.pop(max(data)) if type(data) == list else data.pop(max(data.keys()))
        

# def dequeue_all():
#     k = queue_dict.keys()
#     for i in range(len(k)):
#         return queue_dict.pop(i)


def display():
    print("Elements on queue are:")
    for i in range(len(queue_dict)):
        print(queue_dict)


# executable code
if __name__ == "__main__":
    queue_dict = {}
    push('mohamed', 1)
    push(6, 2)
    push(9, 1)
    push(5, 1)
    print(f"the maximum value that will be poped is : {pop_max(queue_dict)}")
    pop()
    pop()
    pop()
    pop()
    print("Popped Element is: " + str(pop()))
    # print('deque all result :', str(dequeue_all()))
    display()
