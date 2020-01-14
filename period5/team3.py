####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Parambe' # Only 10 chars displayed.
strategy_name = 'John Stockton'
strategy_description = 'Based on the research, we have chosen our decision to either collude or betray accordingly.'
    
def move(my_history, their_history, my_score, their_score):
    return 'b'