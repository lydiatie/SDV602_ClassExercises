def fizz_buzz(fizzNumber, buzzNumber, up_to): 
    a_list = []
    i = 1
    while i < up_to + 1:
        a_tuple = ()
        if i % fizzNumber == 0 and i % buzzNumber == 0: 
            string = 'fizzbuzz'
            a_tuple = (i, string)
              
        elif i % fizzNumber == 0: 
            stringA = 'fizz'
            a_tuple = (i, stringA)

        elif i % buzzNumber == 0: 
            stringB = 'buzz'
            a_tuple = (i, stringB)
            
        else: 
            stringC = str(i)
            a_tuple = (i, stringC)

        a_list = a_list + [a_tuple]
        i += 1 
    for list in a_list:
        print(f'Counting {list[0]} say {list[1]}')

if __name__ == '__main__':
    fizz_buzz(3, 5, 36)