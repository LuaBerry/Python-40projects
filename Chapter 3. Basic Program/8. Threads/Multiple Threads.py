import threading

def sum(name, value):
    for i in range(value):
        print(f"{name} : {i}")

t1 = threading.Thread(target=sum, args=('Thread 1', 10))
t2 = threading.Thread(target=sum, args=('Thread 2', 20))
t3 = threading.Thread(target=sum, args=('Thread 3', 30))

t1.start()
t2.start()
t3.start()

print("Main")