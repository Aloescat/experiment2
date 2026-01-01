def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome """
    cleaned = ''.join(filter(str.isalnum, s)).lower()
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    print("Please enter a string :")
    while True:
        user_input = input("> ")
        if user_input.lower() == 'exit':
            print("Program exited.")
            break
            
        if is_palindrome(user_input):
            print(f'"{user_input}" is a palindrome.')
        else:
            print(f'"{user_input}" is not a palindrome.')
            
        print(" Please enter a new string: ")