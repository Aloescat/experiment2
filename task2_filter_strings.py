def filter_strings(lambda_func, strings):
    return [s for s in strings if lambda_func(s)]

if __name__ == "__main__":
    # one per line, empty line to finish
    print("Please enter strings :")
    strings = []
    while True:
        line = input()
        if line == "":
            break
        strings.append(line)
    
    no_spaces = filter_strings(lambda s: ' ' not in s, strings)
    print("\nNo spaces:", no_spaces)
    
    no_a_start = filter_strings(lambda s: not s.startswith('a'), strings)
    print("No 'a' start:", no_a_start)
    
    min_length_5 = filter_strings(lambda s: len(s) >= 5, strings)
    print("Min length 5:", min_length_5)