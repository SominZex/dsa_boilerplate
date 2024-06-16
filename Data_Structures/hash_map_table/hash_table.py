my_array = ['Somin', 'Ankit', 'Sanju', 'Sunil', 'Tamin']

my_hash_set = [None,None,None,None,None,None,None,None,None,None]

def hash_function(value):
    sum_of_chars = 0
    for char in value:
        sum_of_chars += ord(char)
    
    return sum_of_chars % 10

print('Hash Code for Somin is', hash_function('Somin'))
print('Hash code for Ankit is', hash_function('Ankit'))
print('Hash code for Sanju is', hash_function('Sanju'))
print('Hash code for Sunil is', hash_function('Sunil'))
print('Hash code for Tamin is', hash_function('Tamin'))



#Looking up a name in a hash set/hash table
my_hash_set = [
    [None],
    ['Jones'],
    [None],
    ['Lisa'],
    [None],
    ['Bob'],
    [None],
    ['Siri'],
    ['Pete'],
    [None]
]

def hash_function(value):
    return sum(ord(char) for char in value) % 10
    
def add(value):
    index = hash_function(value)
    bucket = my_hash_set[index]
    if value not in bucket:
        bucket.append(value)
        
def contains(value):
    index = hash_function(value)
    bucket = my_hash_set[index]
    return value in bucket

add('Stuart')

print(my_hash_set)
print('Contains Stuart:',contains('Stuart'))