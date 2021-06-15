#  Your task is to make a function that can take any non-negative integer as an argument and return it with its
#    digits in descending order. Essentially, rearrange the digits to create the highest possible number.

num = int(input("Enter please number: "))# Ввели число перевели его в список и список отсортировали
result_1 = [int(x) for x in str(num)]
result_1.sort(reverse=True)
result = int(''.join(map(str, result_1)))

print(result)
