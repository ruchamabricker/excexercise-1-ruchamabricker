import time

def timer(f, *args, **kwargs):
    begin_time = time.time()
    f(*args, **kwargs)
    end_time = time.time()

    return end_time - begin_time

def example_func(a, b, c):
    time.sleep(1)
    return a*b*c

print(timer(example_func, 1, 2, 3))

