
def encode(input_string):
    try:
        if(input_string[0] == input_string[1]):
            if(input_string[0] != input_string[len(input_string)-1] and input_string[len(input_string)-2] == input_string[len(input_string)-1]):
                index = 0
                initial_value = input_string[0]
                for i in input_string:
                    if(i == initial_value):
                        index+=1
                    else:
                        break
                return input_string[0] + str(index) + input_string[len(input_string)-1] + str(len(input_string)- index)
            else:
                return input_string[0] + str(len(input_string))
        else:
            return input_string
    except:
        return input_string
