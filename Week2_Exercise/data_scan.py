"""
Scans a csv file redirected into the script
 "--header" indicates the first row is a header row
"""
import sys as sys
import argparse

def scan(has_header=False):
    result = []
    values = []
    do_header = has_header
    header_names = {}
    try:
        for aline in sys.stdin:
                this_line = aline.strip().split(',')
                if do_header:
                    header_names = this_line
                    do_header = False
                else:
                    a_dict = {}
                    for i in range(0,len(this_line)):
                        if has_header :
                            a_dict[header_names[i]]= this_line[i]
                        else:
                            a_dict[i]= this_line[i]

                    result += [a_dict]
                    values += [this_line]
    except:
        print("Unexpected error:", sys.exc_info()[0])
        return result,values

    return result,values

# Exercise one
def sum_of(column_name, a_list_of_dictionary):
    """
    Return one value that is the sum of the column 
    column_name of each "row" (dictionary)
    """
    aline_dict = {x.replace(' ', ''): v for x, v in a_list_of_dictionary[0].items()} # get the list of key and value from row aline
    bline_dict = {x.replace(' ', ''): v for x, v in a_list_of_dictionary[1].items()} # get the list of key and value from row bline
    capitalize_column = column_name.capitalize()

    result = int(aline_dict[capitalize_column]) + int(bline_dict[capitalize_column])

    return result


#Exercise Two
def multiple_cols(column_names,a_list_of_dictionary):
    """
    Return a new list of "rows" (dictionary)
    That multiples the values of the named columns
    
    """
     
    result = sum_of(column_names[0], a_list_of_dictionary) * sum_of(column_names[1], a_list_of_dictionary)
  
    return result


#Exercise Three
# - fix display_table so that the columns all line up
def display_table(a_list_of_dictionary):
    lines = ""
    # Get a header line
    a_dictionary = a_list_of_dictionary[0]
    header_line = ""
    for key in a_dictionary:
        header_line += f'{key.strip()}\t'
    header_line = header_line.strip()

    # Make up the table
    lines += header_line 

    for a_dictionary in a_list_of_dictionary:
        a_line = ''
        for key,value in a_dictionary.items():
            a_line += f'{value.strip()}\t' #add strip method to remove additonal space
        a_line = a_line.strip()
        lines += f'\n{a_line}'
    print(lines)

if __name__ == "__main__":
   parser = argparse.ArgumentParser(description="Scan some rows into a list of one list per line.")
   parser.add_argument('--header',action='store_true',help='The first row is a header row.')
   args = vars(parser.parse_args())
   print(f'The args are {args}')

   dict_lst,values_lst = scan(args['header'])
   display_table(dict_lst)

   # Exercise One
   
   column_name = 'Item'
   print(f'The sum of column {column_name} is {sum_of(column_name, dict_lst)}')
   
   # Exercise Two
   column_names = ['Length', 'Item']
   print(f'The multiple of column {column_names[0]} and column {column_names[1]} is {multiple_cols(column_names, dict_lst)}')


   
   
