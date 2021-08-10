import PySimpleGUI as sg

def first_question():
    
    sg.theme('Dark Blue 9')  
    cash_in_hand = 100
    layout = [[sg.Text(f'Cash : ${cash_in_hand}')],
              [sg.Text('You have just arrived in Auckland Airport.\nPlease click the place you want to go.', pad=(0,20)) ],
              [sg.Button('Hotel'), sg.Button('Skytower'),sg.Button('Museum')]
             ]

    window = sg.Window('Where do you want to go?', layout, font="Helvetica" )

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Hotel' or \
           event == 'Skytower' or \
           event == 'Museum':

           destination_choice = window[event].get_text()
           window.close()
           transportation_question(cash_in_hand, destination_choice)
           
    window.close()

def transportation_question(cash_in_hand, destination_choice):


    sg.theme('Dark Blue 9')  

    layout = [[sg.Text(f'Cash : ${cash_in_hand}')],
              [sg.Text(f'Please click the type of transportation to go to the {destination_choice}.\nBus, Train or type "back" to the previous question', pad=(0,20))],
              [sg.Button('Bus'), sg.Button('Train'),sg.Button('Back')]]

    window = sg.Window('Which transport?', layout, font="Helvetica")

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Bus':        
            bus(cash_in_hand, destination_choice)
            window.close()
        elif event == 'Train':
            train(cash_in_hand, destination_choice)
            window.close()
        elif event == 'Back':
            window.close()
            first_question()
            
    window.close()

def bus(cash_in_hand, destination_choice):
    bus_dictionary = {'Hotel': ['20 mins', 10],
                      'Skytower': ['1 hr', 50],
                      'Museum': ['25 mins', 30]
                     }
    
    list_dictionary = bus_dictionary[destination_choice] 

    if sg.popup_yes_no(f'The bus takes {list_dictionary[0]} to arrive {destination_choice} and the fare is ${list_dictionary[1]}.\nYou have ${cash_in_hand}.Do you want to proceed?') == 'Yes':
        cash_in_hand = cash_in_hand - list_dictionary[1]
        print(f'Going to the {destination_choice} by bus. You have ${cash_in_hand} left')
    else:
        
        transportation_question(cash_in_hand, destination_choice)


def train(cash_in_hand, destination_choice):
    train_dictionary = {'Hotel': ['5 mins', 30],
                        'Skytower': ['30 mins', 80],
                        'Museum': ['10 mins', 40]
                        }
    
    list_dictionary = train_dictionary[destination_choice]

    if sg.popup_yes_no(f'The train takes {list_dictionary[0]} to arrive {destination_choice} and the fare is ${list_dictionary[1]}.\nYou have ${cash_in_hand}.Do you want to proceed?') == 'Yes':
        
        cash_in_hand = cash_in_hand - list_dictionary[1]
        print(f'Going to the {destination_choice} by train. You have ${cash_in_hand} left')
    else:

        transportation_question(cash_in_hand, destination_choice)


if __name__ == "__main__":
    first_question()