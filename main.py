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

def merge_sort(listi, left, right):
    if left < right:
        middle = (left + right) // 2
        merge_sort(listi, left, middle)
        merge_sort(listi, middle + 1, right)
        merge(listi, left, right, middle)


def merge(listi, left, right, middle):
    l = listi[left:middle + 1]
    r = listi[middle + 1:right + 1]
    i,j,k = 0,0,left
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            listi[k] = l[i]
            i+=1
        else:
            listi[k] = r[j]
            j+=1
        k+=1
    while i < len(l):
        listi[k] = l[i]
        i+=1
        k+=1
    while j < len(r):
        listi = r[j]
        j+=1
        k+=1

test_list = [4, 3, 10, 2, 5]
test_list2 = [12, 11, 13, 5, 6, 7]
test_list3 = [4,0,6,1,5,2,3]
merge_sort(test_list, 0, 4)
print(test_list)
merge_sort(test_list2, 0, len(test_list2)-1)
print(test_list2)
merge_sort(test_list3, 0, len(test_list3) - 1)
print(test_list3)
# call stack = [(0,4),(0,2), (0,1), (0,0)]
# ---- left = 0, right = 4
# ---- condition check : true
# ---- middle = 2
# ---- calls reccur (0, 2)
# ---- condition check True
# ---- middle = 1
# ---- calls reccur (0,1)
# ---- condition check True
# ---- calls reccur (0,0)
# ---- condition check False returns None
# ---- pops (0,0) from call stack
# call stack = [(0,4),(0,2), (0,1)]
# ---- will finish (0,1) calls now
# ---- calls right side now (0,0) returns None
# ---- calls merge(0,0,1)


def print_list(head):
    if not head:
        print(head)
    curr = head
    while curr:
        print(curr.val)
        curr = curr.nxt

class Node:
    def __init__(self, val):
        self.val = val
        self.nxt = None

def reverse_linked_list(head):
    if not head or not head.nxt:
        return head
    p = reverse_linked_list(head.nxt)
    head.nxt.nxt = head
    head.nxt = None
    return p
    
# 1 - 2 - 3 - 4 - 5
# 5 - 4 - 3 - 2 - 1
head = Node(1)
one = Node(2)
two = Node(3)
three = Node(4)
four = Node(5)
head.nxt = one
one.nxt = two
two.nxt = three
three.nxt = four

print_list(head)

p = reverse_linked_list(head)
print("************")

print_list(p)
    
