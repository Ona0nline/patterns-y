# TODO: Complete the required shape below with reference to the unittests
def is_prime(n):

   count = 0
   for num in range(2,n):
       if n % num != 0:
           count += 1
           if count == (n-2):
              return True
       else:
           return False

def draw_triangle_prime(height:int)->None:
    """
    Draws a triangle of prime numbers where each row contains the first n primes
    that fit the row width.
    
    Parameters:
        height (int): The height of the triangle. Must be a positive integer.
        
    Returns:
        None: Prints the prime number triangle pattern directly to console.
        
    """
    primes = [2]
    num = 3
    while len(primes) < sum(range(1, height + 1)):
        if is_prime(num):
            primes.append(num)
        num += 1

    for i in range(height):
        [ print(primes.pop(0), end="" + " ") for _ in range(1, i + 2 )]
        print()

draw_triangle_prime(5)








# TODO: Complete the required shape below with reference to the unittests
def draw_triangle(height:int)->None:
    """
    Draws a number triangle where each row contains sequential numbers from 1 to the row number.
    
    Parameters:
        height (int): The height of the triangle. Must be a positive integer.
        
    Returns:
        None: Prints the triangle pattern directly to console.
    
        
    """
    num_list = [i for i in range(1, height + 1)]

    print(num_list)
    
    index = 0
    for i in range(len(num_list)):
        [print(num_list[index], end=" " + " ") for _ in range(1, i+2 )]
        index += 1
        i = 1
        print()

  
draw_triangle(5)






# TODO: Complete the required shape below with reference to the unittests
def pascal_triangle(n):
    """
    Generates Pascal's triangle and returns the final row as a list.

    Parameters:
    n (int): The row number of Pascal's triangle to generate (0-based index).

    Returns:
    list: The final row of Pascal's triangle as a list.

    Formula for Pascal's Triangle:
    Each element in Pascal's triangle can be calculated using the following formula:

    C(n, k) = n! / (k! * (n-k)!)

    Where:
    - n is the row number (0-based index)
    - k is the column number (0-based index)
    - C(n, k) represents the value at row n and column k in Pascal's triangle
    - n! represents the factorial of n

    To generate a row of Pascal's triangle, iterate over the columns from 0 to n.





    
    Calculate each element using the formula and store them in a list to form the row.
    Repeat this process for each row up to the desired row number.

    Example:
     * Input: n = 6
     * Output:
     *           1
     *         1   1
     *       1   2   1
     *     1   3   3   1
     *   1   4   6   4   1
     * 1   5  10   10  5   1
    """

    row = [1]
    for i in range(1, n +1):

        row = [x + y for x, y in zip([0]+ row, row + [0])]

    print(row)   

pascal_triangle(3)

# Draw triangle reversed, draw multiplatcation triangle
