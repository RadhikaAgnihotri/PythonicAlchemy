#Binary search

#function to handle multiple occurrence issue 
def test_location(cards, query, mid):
    mid_number = cards[mid]
    print("mid:", mid, ", mid_number:", mid_number)
    if mid_number == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'  
        else:
            return 'found'
    elif mid_number < query:  
        return 'left'    
    else: 
        return 'right'   

def locate_card(cards, query):
    low, high = 0, len(cards) -1   
    
    while low <= high:
        print("low:", low, ", high:", high)
        mid = (low + high) // 2 #double slash return quotient as int and not with decimals
        result = test_location(cards, query, mid)
        
        
        if result == 'found':
            return mid 
        elif result == 'left':
            high = mid - 1 
        elif result == 'right': 
            low = mid + 1 
            
    return -1
#creating dictionary as testcases
tests = []

#general case where query is somewhere in middle
tests.append ({
    'input': {
        'cards' : [13,11,10,7,4,3,1,0],
        'query' : 7
    },
    'output' : 3
})

#query occurs in the middle or closer to one end
tests.append({
    'input' : {
        'cards' : [13,11,10,7,4,3,1,0],
        'query' : 1
    },
    'output' : 6
})

#query is the first element
tests.append({
    'input' : {
        'cards' : [4,2,1,-1],
        'query' : 4
    },
    'output' : 0
})

#query is the last element
tests.append({
    'input' : {
        'cards' : [3,-1,-9,-127],
        'query' : -127
    },
    'output' : 3
})

#card contain only 1 element i.e. query
tests.append({
    'input' : {
        'cards' : [6],
        'query' : 6
    },
    'output' : 0
})

#cards does not contain query
tests.append({
    'input' : {
        'cards' : [9,7,5,2,-9],
        'query' : 4
    },
    'output' : -1 #our assumption/ask interviewer
})

#cards is an empty list
tests.append({
    'input' : {
        'cards' : [],
        'query' : 7
    },
    'output' : -1
})

#numbers repeat in the cards' list but query does not repeat
tests.append({
    'input' : {
        'cards' : [8,8,6,6,6,6,6,3,2,2,2,0,0,0],
        'query' : 3
    },
    'output' : 7
})

#query occurs multiple times
tests.append({
    'input' : {
        'cards' : [8,8,6,6,6,6,6,3,2,2,2,0,0,0],
        'query' : 6
    },
    'output' : 2 #we return the 1st occurrence   
})

#print(tests)

# result = locate_card(test['input']['cards'], test['input']['query'])
# print(result)

for i, test in enumerate(tests, start=1):
    input_cards = test['input']['cards']
    input_query = test['input']['query']
    expected_output = test['output']
    
    # Call the function with input from the testcase
    result = locate_card(input_cards, input_query)
    
    # Compare the result with the expected output
    if result == expected_output:
        #print(result)
        print(f"Testcase {i}: Passed")
    else:
        print(f"Testcase {i}: Failed. Expected {expected_output}, got {result}")

#----------x----------x----------x----------x----------x----------

#Binary Search Simple Implementation
#Given a list sorted in ascending order

def binary_search(sequence, number_to_find):
    begin_index = 0
    end_index = len(sequence) - 1


    while begin_index <= end_index:
        mid = (begin_index + end_index) // 2 #// is floor division
        mid_value = sequence[mid]
        if mid_value == number_to_find:
            return mid
        elif mid_value < number_to_find:
            begin_index = mid + 1
        elif mid_value > number_to_find:
            end_index = mid - 1
    return None   
    
sequence_a = [2,4,5,6,12,62,65,78,80,92]
find_num = 65

print(binary_search(sequence_a, find_num))