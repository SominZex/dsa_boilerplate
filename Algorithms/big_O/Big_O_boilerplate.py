import time

def calculate_time_complexity(func, *args, **kwargs):
    """
    Calculate the time complexity of a function.

    Parameters:
        func (function): The function to analyze.
        *args: Positional arguments to pass to the function.
        **kwargs: Keyword arguments to pass to the function.

    Returns:
        time_taken (float): Time taken to execute the function.
    """
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()
    time_taken = end_time - start_time
    return time_taken

# Example function to analyze
def example_function(n):
    """
    Example function to analyze its time complexity.

    Parameters:
        n (int): Input size.

    Returns:
        None
    """
    for i in range(n):           # O(n)
        for j in range(n):       # O(n)
            print(i, j)          # O(1)

# Example usage:
input_size = 1000
time_taken = calculate_time_complexity(example_function, input_size)
print(f"Time taken for input size {input_size}: {time_taken} seconds")
