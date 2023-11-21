import time
import bcrypt

def time_function(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time of {func.__name__}: {execution_time:.6f} seconds")
        return result
    return wrapper

@time_function
def generate_salts(x):
    bcrypt.hashpw("test".encode(), bcrypt.gensalt(x),)

for i in range(12, 17):
    print(i)
    generate_salts(i)
