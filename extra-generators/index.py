# Loop solution
def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

my_nums = square_numbers([1,2,3,4,5])
print(my_nums)

# List comprehension for loop solution
my_nums = [i*i for i in [1,2,3,4,5]]
print(my_nums)

#--------------------------------------
# Generator solution
def square_numbers_generator(nums):
    for i in nums:
        yield i*i

my_nums = square_numbers_generator([1,2,3,4,5])
for i in my_nums:
    print(i, end=', ')
print('')

# List comprehension for generator solution
my_nums = (i*i for i in [1,2,3,4,5])
for i in my_nums:
    print(i, end=', ')
print('')
