
def encode(input_string):
    try:
        if(input_string[0] == input_string[1]):
            return input_string[0] + str(len(input_string))
        else:
            return input_string
    except:
        return input_string
