k = 0
def enqueue(data):
    global k
    queue_dict.update({k: data})
    k = k + 1

def dequeue():
    if len(queue_dict) > 0:
        # print(queue_dict.keys())
        return queue_dict.pop(min(queue_dict.keys()))
    return "stack  dictionary Empty!"


def display():
    print("Elements on queue are:")
    for i in range(len(queue_dict)):
        print(queue_dict)


# executable code
if __name__ == "__main__":
    queue_dict = {}
    enqueue('mohamed')
    enqueue(6)
    enqueue(9)
    enqueue(5)
    enqueue(3)
    print("Popped Element is: " + str(dequeue()))
    # print('deque all result :', str(dequeue_all()))
    display()