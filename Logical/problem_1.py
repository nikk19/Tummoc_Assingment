def is_val_creditCard(number):
    num_str = str(number)
    length = len(num_str)
    
    if not (13 <= length <= 16):
        return False

    if not ((length == 13 and num_str.startswith('4')) or
            (length == 16 and num_str.startswith('5')) or
            (length == 15 and num_str.startswith('37')) or
            (length == 16 and num_str.startswith('6'))):
        return False

    nums = [int(digit) for digit in num_str]

    doubled_sum = sum(sum(int(digit) for digit in str(num * 2)) if num * 2 > 9 else num * 2
                      for num in nums[-2::-2])
    
    total_sum = doubled_sum + sum(nums[-1::-2])

    return total_sum % 10 == 0

num = 4123456789123
if is_val_creditCard(num):
    print("Valid")
else:
    print("Invalid")
