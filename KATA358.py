#kata
#https://www.codewars.com/kata/53921994d8f00b93df000bea/train/python

def content_weight(bottle_weight, scale): 
    parts = scale.split()
    k = int(parts[0])  
    relation = parts[-1]  
    if relation == "larger":
        return (k * bottle_weight) // (k + 1)
    elif relation == "smaller":
        return bottle_weight // (k + 1)
    else:
        raise ValueError("Scale must end with 'larger' or 'smaller'")



