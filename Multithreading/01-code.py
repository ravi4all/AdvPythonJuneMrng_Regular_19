import threading

def job_1():
    print("This is job_1")
    for i in range(10000):
        for j in range(10000):
            k = i + j
    print("Job_1 Completed")

def job_2():
    print("This is job_2")
    for i in range(100):
        for j in range(100):
            k = i + j
    print("Job_2 Completed")

# job_1()
# job_2()

t1 = threading.Thread(target=job_1)
t2 = threading.Thread(target=job_2)

t1.start()
t2.start()