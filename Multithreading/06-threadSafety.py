import threading
import time

class ThreadSafety(threading.Thread):

    def __init__(self,bal):
        self.bal = bal

    def balance(self, amount):
        lock.acquire()
        try:
            print("Hello", threading.current_thread().getName(), "balance is", self.bal)
            print("Lock Acquired by {}".format(threading.current_thread().getName()))
            time.sleep(5)
            if self.bal > amount:
                if self.bal > 5000:
                    self.bal = self.bal - amount
                    print("Remaining balance :",self.bal)
                else:
                    print("Can't withdraw...")
            else:
                print("Can't withdraw")
        except Exception as ex:
            print(ex)

        print("{} exit".format(threading.current_thread().getName()))
        lock.release()
        print("Lock Released by {}".format(threading.current_thread().getName()))
        # print("Now balance is",self.bal)

obj = ThreadSafety(8000)

lock = threading.Lock()

thread1 = threading.Thread(target=obj.balance, args = (4000,), name='Thread_1')
thread2 = threading.Thread(target=obj.balance, args = (4000,), name='Thread_2')

thread1.start()
thread2.start()
