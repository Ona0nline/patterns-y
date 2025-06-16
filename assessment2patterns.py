def main():
  print(pascals)
  print(draw_triangle_prime(5))

def pascals(n):
  
  row = [1]
  for i in range(1, n):
    row = [x + y for x,y in zip([0] + row, row + [0])]
  # print(row)
  return row


def is_prime(n):
  
  if n <= 1:
    return False
  
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False
    
  return True

def draw_triangle_prime(height):
  
  primes = []
  num = 2
  while(len(primes) < sum(range(1, height + 1))):
    if is_prime(num):
      primes.append(str(num))
      
    num += 1
    
  output = ""
  for i in range(height):
    row = " ".join(primes.pop(0) for _ in range(1, i + 2))
    output += row + "\n"
    # print(output)
    
  return output[:-1]



def square(n):
  output = ""
  for i in range(1, n+1):
    row = "".join(n * "*")
    output += row + "\n"
    
  return output


def right_angled_star_triangle(n):
  
  output = ""
  for i in range(1, n+1):
    row = "".join(i * "*")
    output += row + "\n"
    
  return output

def number_triangle(height):
  
  number = 1
  for i in range(1, height + 1):
    print((str(number) + " ") * i, end="")
    number += 1
    print()
    
def number_triangle_reverse(height):
  
  number = 1
  for i in range(height, 0, -1):
    print((str(number) + " ") * i, end="")
    number += 1
    print()

def counting_triangle(height):
  
  for i in range(1, height + 1):
    for j in range(1, i + 1):
      print(str(j) + " ", end="")
    print()
    

def multiplication_triangle(height):
  for i in range(1, height + 1):
    for j in range(1, i + 1):
      print((str(i * j) + " "), end="")
    print()
    
def pyramid(height):
  
  pyramidempty = ""
  for i in range(1, height + 1):
    pyramid = '  ' * (height - i) + "* " * (2 * i - 1)
    pyramidempty += pyramid + "\n"
    # print(pyramid)
  return pyramidempty

    
print(pascals(5))
print(draw_triangle_prime(5))
print(square(5))
print(right_angled_star_triangle(5))
print(number_triangle(5))
print(number_triangle_reverse(5))
print(counting_triangle(5))
print(multiplication_triangle(5))
print(pyramid(5))

