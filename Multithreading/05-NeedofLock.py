import threading
import time

class ThreadSafety():

    def __init__(self,bal):
        self.bal = 10000

    def balance(self, amount):
        try:
            print("Hello", threading.current_thread().getName(), "balance is", self.bal)
            time.sleep(2)
            if self.bal > amount:
                if self.bal > 5000:
                    self.bal = self.bal - amount
                    print(threading.current_thread().getName(),"Remaining balance:",self.bal)
                else:
                    print("Can't withdraw...")
            else:
                print("Can't withdraw")
        except Exception as ex:
            print(ex)

        # print("Thread {} exit".format(threading.current_thread().getName()))
        print("Balance after transaction by",threading.current_thread().getName(),"is",self.bal)

obj = ThreadSafety(10000)

thread1 = threading.Thread(target=obj.balance, args = (4000,), name='Thread_1')
thread2 = threading.Thread(target=obj.balance, args = (4000,), name='Thread_2')

thread1.start()
thread2.start()
