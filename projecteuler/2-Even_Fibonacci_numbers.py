"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""
number_sum = 2
fibonacci_number = 3
last_number = 2
last_last_number = 1
limit = 4_000_000
while fibonacci_number < limit:
    fibonacci_number, last_number, last_last_number = (fibonacci_number + last_number), fibonacci_number, last_number
    print(f'fibonacci_number={fibonacci_number} | last_number={last_number} | last_last_number={last_last_number}')
    if fibonacci_number % 2 == 0 and fibonacci_number < limit:
        number_sum += fibonacci_number
        print(f'soma={number_sum}')

print(number_sum)
