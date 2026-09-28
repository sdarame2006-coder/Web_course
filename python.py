#A- Basic List Logic

def countdown(n):
    return list(range(n, -1, -1))

print(countdown(5))  

#________________________________________

def print_and_return(lst):
    print(lst[0])
    return lst[1]
print_and_return([1, 2])
#________________________________________

def first_plus_length(lst):
    return lst[0] + len(lst)

print(first_plus_length([1, 2, 3, 4, 5]))

#_________________________________________

def values_greater_than_second(lst):
    if len(lst) < 2:
        return False
    second_val = lst[1]
    new_list = [x for x in lst if x > second_val]
    print(len(new_list))
    return new_list

print(values_greater_than_second([5, 2, 3, 2, 1, 4]))  

#_______________________________________________________

def length_and_value(size, value):
    return [value] * size

print(length_and_value(4, 7))

#________________________________________________________
# B-List Algorithms

def biggie_size(lst):
    for i in range(len(lst)):
        if lst[i] > 0:
            lst[i] = "big"
    return lst


def count_positives(lst):
    count = sum(1 for x in lst if x > 0)
    lst[-1] = count
    return lst


def sum_total(lst):
    return sum(lst)

def average(lst):
    if not lst:
        return 0
    return sum(lst) / len(lst)

def minimum(lst):
    if not lst:
        return False
    return min(lst)

#________________________________________________________       
#c- Python Shorthand & Sequences

def greet(name="Guest", time_of_day="day"):
    return f"Good {time_of_day}, {name}!"

result = greet(time_of_day="morning", name="Nesma")
print(result) 

#________________________________________________________

score = 85
result = "Pass" if score >= 60 else "Fail"
print(result)  

#________________________________________________________

fruits = ["apple", "banana", "cherry"]
fruits[0], fruits[-1] = fruits[-1], fruits[0]
print(fruits)  

#________________________________________________________

text = "Coding is fun"

word1 = text[:6]  
word2 = text[-3:]
reversed_text = text[::-1]

print(word1)         
print(word2)          
print(reversed_text)  

#________________________________________________________

data = [42, 10, 77, 2, 15]

max_val = max(data)
total_sum = sum(data)
sorted_data = sorted(data)

print("Max:", max_val)           
print("Sum:", total_sum)         
print("Sorted:", sorted_data)    