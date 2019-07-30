import threading

def job():
    print("Job started by {}".format(threading.current_thread().getName()))
    for i in range(1000):
        for j in range(1000):
            i + j
    print("Job completed by {}".format(threading.current_thread().getName()))

for i in range(5):
    t = threading.Thread(target=job,name="Thread_{}".format(i))
    t.start()