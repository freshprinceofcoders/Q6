def sum_of_squares():
    total_sum_of_squares = 0
    for num1 in range(1,101):
        total_sum_of_squares += num1**2
    return total_sum_of_squares


def square_of_sums():
    answer = 0
    sum_of_numbers = 0
    total_square_of_sum = 0
    for num2 in range(1,101):
        sum_of_numbers += num2
        answer = sum_of_numbers ** 2

    return answer




sum = sum_of_squares()
squares = square_of_sums()
final_ans = squares - sum
print(final_ans)
