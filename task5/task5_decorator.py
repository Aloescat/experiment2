import time


def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {execution_time:.6f} seconds")
        return result
    return wrapper


@timer_decorator
def add_numbers(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")
    return result


@timer_decorator
def calculate_from_file(input_file='input.txt', output_file='output.txt'):
    try:
        with open(input_file, 'r') as f:
            content = f.read().strip()
        
        numbers = content.split()
        if len(numbers) < 2:
            print(f"Error: File '{input_file}' must contain at least two numbers")
            return None
        
        a = float(numbers[0])
        b = float(numbers[1])
        
        result = a + b
        
        with open(output_file, 'w') as f:
            f.write(f"{result}")
        
        print(f"Successfully read {a} and {b} from '{input_file}'")
        print(f"Result {result} written to '{output_file}'")
        return result
        
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found")
    except ValueError:
        print("Error: Could not parse numbers from file")
    except Exception as e:
        print(f"Error: {e}")
    
    return None


# Test the decorator 
if __name__ == "__main__":
    print("Testing timer decorator:")
    print("=" * 50)
    
    # Test 1: Calculate sum of two numbers
    print("\nTest 1: Calculating sum of two numbers")
    add_numbers(10, 20)
    
    # Test 2: Calculate from file
    print("\nTest 2: Calculating sum from file")

    calculate_from_file()
    
    try:
        with open('output.txt', 'r') as f:
            print(f"\nContent of output.txt: {f.read()}")
    except FileNotFoundError:
        print("output.txt file not found")