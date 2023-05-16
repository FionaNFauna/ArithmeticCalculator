def get_values(case_given):
    new_list = case_given.split()

    if new_list[0].isnumeric() == False or new_list[2].isnumeric() == False:
        return 'Error: Numbers must only contain digits.'

    if len(new_list[0])>4 or len(new_list[2])>4:
        return 'Error: Numbers cannot be more than four digits.'

    first_number = int(new_list[0]) #identify the first and second numbers
    second_number = int(new_list[2])
    sign = new_list[1]  #Addition or Subtraction

    #Calculations
    if new_list[1] == "+": #Addition
        output = first_number + second_number
    elif new_list[1] == "-": #Subtraction
        output = first_number - second_number
    else:
        return "Error: Operator must be '+' or '-'."

    listy = [first_number,second_number,sign, output]
    return listy


def output_lines(given_list):        
    larger_number = max(given_list[:2])
    number_of_dashes = 2 + len(str(larger_number))
    first_line = '{message: >{fill}}'.format(message=given_list[0], fill=number_of_dashes)
    second_line = given_list[2] + '{message: >{fill}}'.format(message=given_list[1], fill=number_of_dashes-1)
    third_line = '-'*number_of_dashes
    fourth_line = '{message: >{fill}}'.format(message=given_list[3], fill=number_of_dashes)
    output_list = [first_line, second_line, third_line, fourth_line]
    return output_list


def arithmetic_arranger(inputy, calculate=False):

    if len(inputy) > 5:
        return 'Error: Too many problems.'

    first_line = ''
    second_line = ''
    third_line = ''
    fourth_line = ''

    y = 0
    for x in inputy:
        new_list = get_values(x)
        if type(new_list) != list:
            return new_list
        output_list = output_lines(new_list)
        first_line += output_list[0]
        second_line += output_list[1]
        third_line += output_list[2]
        fourth_line += output_list[3]
        y += 1
        if y != 0 and y != len(inputy):
            first_line += '    '
            second_line += '    '
            third_line += '    '
            fourth_line += '    '
        
    output = first_line + '\n' + second_line + '\n' + third_line
    if calculate == True:
        output += '\n' + fourth_line
        
    return output