import statistics

def length(lst):
    """
    Returns the number of elements in the list.
    
    Args:
    lst: A list of numbers.
    
    Returns:
    int: The length of the list.
    """
    if not isinstance(lst, list):
        raise ValueError("Input must be a list.")
    return len(lst)

def mean(lst):
    """
    Calculates the arithmetic mean of the list.
    
    Args:
    lst: A list of numbers.
    
    Returns:
    float: The mean of the numbers in the list.
    """
    if not isinstance(lst, list):
        raise ValueError("Input must be a list.")
    
    if len(lst) == 0:
        raise ValueError("List cannot be empty.")
    
    if not all(isinstance(i, (int, float)) for i in lst):
        raise ValueError("All elements in the list must be numbers.")
    
    return sum(lst) / len(lst)

def range_of_list(lst):
    """
    Returns the difference between the maximum and minimum values in the list.
    
    Args:
    lst: A list of numbers.
    
    Returns:
    float: The range of the list (max - min).
    """
    if not isinstance(lst, list):
        raise ValueError("Input must be a list.")
    
    if len(lst) == 0:
        raise ValueError("List cannot be empty.")
    
    if not all(isinstance(i, (int, float)) for i in lst):
        raise ValueError("All elements in the list must be numbers.")
    
    return max(lst) - min(lst)

def median(lst):
    """
    Calculates the median of the list.
    
    Args:
    lst: A list of numbers.
    
    Returns:
    float: The median of the numbers in the list.
    """
    if not isinstance(lst, list):
        raise ValueError("Input must be a list.")
    
    if len(lst) == 0:
        raise ValueError("List cannot be empty.")
    
    if not all(isinstance(i, (int, float)) for i in lst):
        raise ValueError("All elements in the list must be numbers.")
    
    return statistics.median(lst)

def standard_deviation(lst):
    """
    Calculates the standard deviation of the list.
    
    Args:
    lst: A list of numbers.
    
    Returns:
    float: The standard deviation of the numbers in the list.
    """
    if not isinstance(lst, list):
        raise ValueError("Input must be a list.")
    
    if len(lst) == 0:
        raise ValueError("List cannot be empty.")
    
    if not all(isinstance(i, (int, float)) for i in lst):
        raise ValueError("All elements in the list must be numbers.")
    
    return statistics.stdev(lst)

def list_statistics(lst):
    """
    Creates a dictionary with list statistics.
    
    Args:
    lst: A list of numbers.
    
    Returns:
    dict: A dictionary with statistics (length, mean, range, median, standard deviation).
    """
    if not isinstance(lst, list):
        raise ValueError("Input must be a list.")
    
    if len(lst) == 0:
        raise ValueError("List cannot be empty.")
    
    if not all(isinstance(i, (int, float)) for i in lst):
        raise ValueError("All elements in the list must be numbers.")
    
    stats = {
        "Length": length(lst),
        "Mean": mean(lst),
        "Range": range_of_list(lst),
        "Median": median(lst),
        "Standard Deviation": standard_deviation(lst)
    }
    
    return stats

# Test cases
numbers = [1, 2, 3, 4, 5]
print("Statistics for [1, 2, 3, 4, 5]:")
print(list_statistics(numbers))

# Additional test cases
print("\nStatistics for [10, -10, 0, 5]:")
print(list_statistics([10, -10, 0, 5]))

print("\nStatistics for [1.5, 2.5, 3.5]:")
print(list_statistics([1.5, 2.5, 3.5]))

print("\nStatistics for [42]:")
print(list_statistics([42]))

print("\nStatistics for []:")
try:
    print(list_statistics([]))
except ValueError as e:
    print(e)
