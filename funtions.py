def multiply(x: float, y: float) -> float:
    """Multiplies 'x' by 'y'

    Args:
        x: The first integer given which will multiply
        by 'y'
        y: The second integer given which will multiply
        by 'x'
        
    Returns:
        The integer result of 'x' * 'y'
    """
    result = x * y
    return result

def is_palindrome(string: str) -> bool:
    """Checks to see if a word is a palindrome and returns
    that word.
    
    A palindrome is a string that reads the samee forwards
    as backwards.

    Args:
        string: The String that the function will use to
        determine if it is a palindrome.

    Returns:
        True if 'string' is a palindrome, False otherwise.
    """
    return string[::-1] == string
    
def palindrome_sentence(sentence: str) -> bool:
    """Checks to see if a sentence is a palindrome and
    returns that sentence.
    
    The function ignores whitespace, capitalisation and
    punctuation in the sentence.

    Args:
        sentence: The String that the function will use to
        determine if it is a palindrome.

    Returns:
        True if 'sentence' is a palindrome, False otherwise.    
    """
    empty_string = ''
    for i in sentence:
        if i.isalnum():
            empty_string += i
    return is_palindrome(empty_string)


def fibonacci(n: int) -> int:
    """Return the 'n'th Fibonacci number, for positive 'n'."""
    if 0 <= n <= 1:
        return n
    n_minus1, n_minus2 = 1, 0
    
    result = None
    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result
        
    return result


for i in range(36):
    print(i, fibonacci(i))
    
p = palindrome_sentence()