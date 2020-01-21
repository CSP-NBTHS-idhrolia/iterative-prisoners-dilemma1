####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

import random
team_name = 'Team1' # Only 10 chars displayed.
strategy_name = 'Good Boi Points'
strategy_description = 'Always betray if my_score < their_score.'

def move(my_history, their_history, my_score, their_score):
    b_c_value = 0
    goodboy_points = 0

    if len(my_history) == 0:
        return 'c'
    
    if their_score > my_score:
        return 'b'
    
    for i in their_history:
        if i == 'b':
            b_c_value += -10
        if i == 'c':
            b_c_value += +10

    goodboy_points = b_c_value / len(their_history)

    if random.randint(-10, 10) <= goodboy_points:
            return 'c'
    else:
            return 'b'

    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

def test_move(my_history, their_history, my_score, their_score, result = random.choice(['a','b'])):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    
    return False

if __name__ == '__main__':
     
    # Test 1: Collude on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='c'):
         print('Test1: passed')
    
    # Test 2: They have a high goodie points
    if test_move(my_history='bbbbbbbbbbbbbb',
              their_history='ccccccccccccbb', 
              my_score = 0,
              their_score = 0,
              result='c'):
         print('Test2: passed')
    else:
        print("Test2: failed")
    
    # Test 3: They have high goodie points but higher score
    if test_move(my_history='bbbbbbbb',
              their_history='cccccccc', 
              my_score = 0,
              their_score = 100,
              result='b'):
         print('Test3: passed')
    else:
        print('Test3: Failed')

    # Test 4: They have low goodie points
    if test_move(my_history='bbbbbbbb',
              their_history='bbbbbbcc', 
              my_score = 0,
              their_score = 0,
              result= 'b'):
         print('Test4: passed')
    else:
        print('test4: failed')

    # Test 5: Medium
    if test_move(my_history='bbbbbbbb',
              their_history='bbbbcccc', 
              my_score = 0,
              their_score = 0,
              result= 'b'):
         print('Test5: passed')
    else:
        print('Test5: failed')
    
    
    

           
