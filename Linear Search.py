#Linear Search 
#brute force solution or linear search
def locate_card(cards, query):
    position = 0 
    
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1 
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

