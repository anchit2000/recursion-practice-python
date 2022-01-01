def reverse_string(string):
    if string == "":
        return ""
    return string[-1] + reverse_string(string[:-1])
    
print(reverse_string("Anchit"))

def check_palindrome(string):
    if len(string) < 2:
        return True
        
    if string[0] != string[-1]:
        return False
        
    return check_palindrome(string[1:-1])
    
print(check_palindrome("kayak"))
print(check_palindrome("anchit"))
print(check_palindrome("racecar"))

def convert_decimal_to_binary(number : int):
    if number < 1:
        return ""
        
    return convert_decimal_to_binary(number//2) + str(number%2)
    
print(convert_decimal_to_binary(233))
    
def sum_of_natural_numbers(number):
    if number == 0:
        return 0
    return number + sum_of_natural_numbers(number-1)
    
print(sum_of_natural_numbers(10))

def binary_search(listi , start_point, end_point, number):

    mid_point = (start_point + end_point) //2

    if mid_point < 0 or mid_point > len(listi):
        return -1
    
    if listi[mid_point] == number:
        return mid_point
    
    if listi[mid_point] > number:
        return binary_search(listi , 0 , mid_point-1 , number)
        
    if listi[mid_point] < number:
        return binary_search(listi, mid_point+1, len(listi), number)

sorted_list = [-1,0,1,2,3,4,7,9,10,20]
print(binary_search(listi = sorted_list,start_point = 0,end_point = len(sorted_list),number = 10))
