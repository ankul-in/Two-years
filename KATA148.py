#kata
#https://www.codewars.com/kata/59727ff285281a44e3000011/train/python

def band_name_generator(name):
    if name[0]==name[-1]:
        return name[0].upper()+name[1:]+name[1:]
    else:
        return "The "+ name[0].upper()+name[1:]
    

print(band_name_generator("sandles"))
print(band_name_generator("knife"))