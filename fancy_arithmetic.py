def add(nums):
    return sum(nums)

def subtract(nums):
    if check_if_too_few_numbers(nums, 2):
        return
    
    result = nums.pop(0) - nums.pop(0)
    for num in nums:
        result -= num
    return result

def multiply(nums):
    if check_if_too_few_numbers(nums, 2):
        return
    result = nums.pop(0) * nums.pop(0)
    for num in nums:
        result *= num
    return result

def divide(nums):
    if check_if_too_few_numbers(nums, 2):
        return
    result = float(nums.pop(0)) / nums.pop(0)
    for num in nums:
        result /= num
    return result

def square(nums):
    """return the square of provided number"""
    if check_if_too_few_numbers(nums, 1):
        return
    result = []
    for num in nums:
        result.append(num * num)

    return result

def cube(nums):
    """return the cube of the number"""
    if check_if_too_few_numbers(nums, 1):
        return
    result = []
    for num in nums:
        result.append(num * num * num)

    return result

def power(nums):
    """return result of raising num1 to the power of num2"""
    if check_if_too_few_numbers(nums, 2):
        return
    result = nums.pop(0) ** nums.pop(0)
    for num in nums:
        result **= num

    return result

def mod(nums):
    """returns the remainder when num1 is divided by num2"""
    # result = []
    # for index in range(len(nums)):
    #     if index % 2 == 0:
    #         continue
    #     else:
    #         result.append(nums[index-1] % nums[index])
    # return resultdef calculator():
    if check_if_too_few_numbers(nums, 2):
        return

    results = []

    first_int = None
    for num in nums:
        if not first_int:
            first_int = num
        else:
            results.append(first_int%num)
            first_int = None

    return results


def check_if_too_few_numbers(nums, expected_number):
    if len(nums) < expected_number:
        return True

    return False
