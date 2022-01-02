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

def fibonacci(number):
    if number == 0 or number == 1:
        return number
        
    return fibonacci(number-1) + fibonacci(number-2)
    
print(fibonacci(10))

listi = []
def return_fibonacci_list(number):
    if number < 2:
        return listi
    listi.append(fibonacci(number))
    return return_fibonacci_list(number-1)
    
print(return_fibonacci_list(10))

def merge_sort(array, low, high):
    
    if low < high:
        
        middle = (low+high)//2
        
        merge_sort(array,low, middle)
        
        merge_sort(array, middle+1, high)
        
        merge(array, low, middle, high)
        
        # print(array[low:middle])
        
def merge(arr , low, middle, high):

    n1 = middle - low +1
    n2 = high - middle 
 
    L = [0] * (n1)
    R = [0] * (n2)
 
    for i in range(0, n1):
        try:
            L[i] = arr[low + i]
        except:
            print(i)
 
    for j in range(0, n2):
        try:
            R[j] = arr[middle + 1 + j]
        except:
            print(j)
 
    i = 0   
    j = 0   
    k = low
    
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
        
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1



array = [4,0,6,1,5,2,3]

merge_sort(array,0,len(array)-1)

print(array)
