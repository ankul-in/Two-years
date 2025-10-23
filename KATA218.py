#kata
#https://www.codewars.com/kata/58b1ae711fcffa34090000ea/train/python

#knew this was possible 
#whats wrong with me oh shit now i get it 
#average for me is not 5 its 50 damn i messed up
#if i try to excell then am i going to reach the previous average
#if not then ... then what
def controller(events: str) -> str:
    position = 0
    direction = 0  # 1 for opening, -1 for closing, 0 for stopped
    paused = False
    output = []

    for event in events:
        # Handle event
        if event == 'O':
            if direction != 0:
                direction *= -1  # reverse direction
                paused = False
        elif event == 'P':
            if direction == 0:
                # Start moving
                direction = 1 if position == 0 else -1
                paused = False
            else:
                paused = not paused  # toggle pause

        # Update position
        if not paused and direction != 0:
            position += direction
            # Clamp position and stop if fully open/closed
            if position >= 5:
                position = 5
                direction = 0
            elif position <= 0:
                position = 0
                direction = 0

        output.append(str(position))

    return ''.join(output)


#well i tried
# def controller(s):
#     direction = 0
#     position = 0
#     paused = False
#     pressed_P = False
#     answer = []

#     for j in s:
#         if j == "O" and not paused:
#             direction *= -1
#             position += direction
#             answer.append(str(position))
        
#         elif j == "P":
#             if position > 5:
#                 direction *= -1
#                 position += direction
#                 answer.append(str(position))
#             else:
#                 if pressed_P and position < 5:
#                     paused = True
#                 if not paused:
#                     if direction == 0:
#                         direction = 1
#                     position += direction
#                     answer.append(str(position))
#                 else:
#                     answer.append(str(position))
#             pressed_P = True

#         elif j == ".":
#             if paused:
#                 answer.append(str(position))
#             else:
#                 position += direction
#                 answer.append(str(position))
#     newAnswer=[i if int(i) < 5 else '5' for i in answer]
#     return "".join(newAnswer)
# print(controller('P......P......'))
        
        
                
            
            
    
    























# def controller(events):
#     log=[]
#     open=False
#     answer=[]
#     for i in events:
#         if i==".":
#             answer.append(0)
#         if i=="P":
#             if open:

#             open=True



# print(controller('...P......P....O....'))
# # def controller(events):
# #     x="O"
# #     answer=[]
# #     for i,j in enumerate(events):
# #         if j=="P" and x=="P":
# #             x="Q"
# #         elif j=="P":
# #             x="P"
# #         elif j=="O":
# #             x="R"

# #         answer.append(x)     
# #     return answer