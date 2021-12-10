#Given an integer n, return a string array answer (1-indexed) where:
#answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
#answer[i] == "Fizz" if i is divisible by 3.
#answer[i] == "Buzz" if i is divisible by 5.
#answer[i] == i (as a string) if none of the above conditions are true.



def fizzBuzz(n):
    count = 1
    index = 0
    dFive = " Buzz"
    dThree = " Fizz"
    dThreeAndFive = "FizzBuzz"
    answer = [None] * (n)
    
    while count <= n:
        answer[index] = str(count)
        if count % 3 == 0 and count % 5 == 0: #divisible by 3 and 5
            answer[index] = (dThreeAndFive)
        if count % 3 == 0 and count % 5 != 0: # divisible by 3 only
            answer[index] = (dThree)
        if count % 3 != 0 and count % 5 == 0: # divisible by 5 only
            answer[index] = (dFive)
        count += 1
        index += 1

    return answer

answer = fizzBuzz(20)

i = 0
while i < len(answer):
    print (answer[i]) # prints contents of array, one element at a time
    i += 1
    
