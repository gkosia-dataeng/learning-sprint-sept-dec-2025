'''Context managers are used to namage resources in a scope of code
   The context manager object should implement the __enter__, __exit__ methods

   
   Another way to create a context manager in more functional way is to use contextlib.contextmanager

   Benefits:
        Automatic cleanup of resources
        Cleaner code
        Reusability of context manager
        Central handling of exceptions

'''
class TimerCtxM():
    def __enter__(self):
        print("__enter__ method called")

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"__exit__ method called, exception information {exc_type, exc_value, traceback}")


with TimerCtxM() as t:
    print("Doing the job using TimerCtxM")
    #raise Exception("Raised exception in context manager scope")



from contextlib import contextmanager

@contextmanager
def cntx_manager():
    print("enter the cntx manager")
    yield
    print("exit the cntx manager")

with cntx_manager():
    print("Doing the job in functional context manager")