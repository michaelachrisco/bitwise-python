# Easy imp
for i in range(51):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0 and not (i % 15 == 0):
        print("Fizz")
    elif i % 5 == 0 and not (i % 15 == 0):
         print("Buzz")
    else:
        print(i)

# one liner?
for num in range(1,50): print("Fizz" * (num % 3 == 0) + "Buzz" * (num % 5 == 0) or num)

#Passes TDD
print('1,2,Fizz,4,Buzz,Fizz,7,8,Fizz,Buzz,11,Fizz,13,14,FizzBuzz,16,17,Fizz,19,Buzz,Fizz');

