#kata
#https://www.codewars.com/kata/57061b6fcb7293901a000ac7/train/python

def head_smash(arr):
    ans=[]
    if not arr:
        return "Gym is empty"
    if isinstance(arr,int):
        return "This isn't the gym!!"
    for i in arr:
        ans.append(i.replace("O"," "))
        
    return  "\n".join(ans)


print(head_smash(
        [
        '*****************************************',
        '***********   _O_   *   _O_   ***********',
        '**  _O_   *  C(.)J  *  /(.)J  *   _O_  **',
        '** /(.)J  *  _| |_  *  _/ )_  *  C(.)J **',
        '** _/ )_  *********************  _/ |_ **',
        '******************* X *******************',
        '**********************  _O_  ************',
        '**  _O_   *   _O_   *  /(.)J  *   _O_  **',
        '** /(.)J  *  C(.)J  *  _/ )_  *  C(.)J **',
        '** _( )_  *  _| |_  ***********  _/ |_ **',
        '****************************************']))