
def transportation_question(cash_in_hand, destination_choice):
    transportation_choice = input(f'Please select and enter the type of transportation to go to the {destination_choice}.\nBus, Train or type "back" to the previous question\n').lower()
    
    if transportation_choice == 'train':
        train(cash_in_hand, destination_choice)

    elif transportation_choice == 'bus':
        bus(cash_in_hand, destination_choice)
    
    elif transportation_choice == 'back':
        first_question()
    
    else:
        print("Sorry, wrong answer")
        transportation_question(cash_in_hand, destination_choice)

    
def first_question():
    cash_in_hand = 100
    destination_choice = input('You have just arrived in Auckland Airport.\nPlease select from the list below and enter the place you want to go.\nHotel, Skytower or Museum\n').lower()
    
    if destination_choice == 'hotel' or destination_choice == 'skytower' or destination_choice == 'museum':
        transportation_question(cash_in_hand, destination_choice)
    
    else:
        print("Sorry, wrong answer")
        first_question()

def train(cash_in_hand,destination_choice):
   
    # Creating a list of estimated time taken and fare
    train_dictionary = {'hotel': ['5 mins', 30],
                        'skytower': ['30 mins', 80],
                        'museum': ['10 mins', 40]
                        }

    list_dictionary = train_dictionary[destination_choice]
    train_confirmation = input(f'The train takes {list_dictionary[0]} to arrive {destination_choice} and the fare is ${list_dictionary[1]}.\nYou have ${cash_in_hand}. Do you want to proceed?\nType yes to confirm or no to back.\n').lower()
    
    if train_confirmation == 'yes':
        cash_in_hand = cash_in_hand - list_dictionary[1]
        print(f'Going to the {destination_choice} by train. You have ${cash_in_hand} left')
    
    elif train_confirmation == 'no':
        transportation_question(cash_in_hand, destination_choice)
    
    else:
        print("Sorry, wrong answer")
        train(cash_in_hand, destination_choice)

def bus(cash_in_hand, destination_choice):

    # Creating a list of estimated time taken and fare
    bus_dictionary = {'hotel': ['20 mins', 10],
                      'skytower': ['1 hr', 50],
                      'museum': ['25 mins', 30]
                     }
    
    list_dictionary = bus_dictionary[destination_choice] 
    confirmation = input(f'The bus takes {list_dictionary[0]} to arrive {destination_choice} and the fare is ${list_dictionary[1]}.\nYou have ${cash_in_hand}. Do you want to proceed?\nType yes to confirm or no to back.\n').lower()
    
    if confirmation == 'yes':
        cash_in_hand = cash_in_hand - list_dictionary[1]
        print(f'Going to the {destination_choice} by bus. You have ${cash_in_hand} left')
    
    elif confirmation == 'no':
        transportation_question(cash_in_hand, destination_choice)
    
    else:
        print("Sorry, wrong answer")
        bus(cash_in_hand, destination_choice)

           
if __name__ == '__main__':

    first_question()
    
