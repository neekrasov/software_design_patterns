import time

def time_it(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print("Total time: {}s".format(end - start))
        return result
    return wrapper

@time_it
def function():
    print("Starting function")
    time.sleep(1)
    print("Ending function")
    return 1

if __name__ == "__main__":
    function()