# #counting smile function 
#Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
# A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
# Every smiling face must have a smiling mouth that should be marked with either ) or D
list=[":-)",":-D",":~)",":~D",":)",":D",";-)",";-D",";~)",";~D",";)",";D"]
def count_smileys(arr):
    count=0
    for smile in arr:
        if smile in list:
            count+=1
    
        
    return count