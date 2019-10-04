
def encode(input_string):
    try:
        final_string = ""
        index = 1
        for i in range(len(input_string)-1):
            if(input_string[i] == input_string[i+1]):
                index+=1
            else:
                final_string+=input_string[i]
                if(index > 1):
                    final_string+=str(index)
                index = 1
        final_string += input_string[len(input_string)-1]
        if(index > 1):
            final_string += str(index)
        return final_string
    except:
        return input_string
