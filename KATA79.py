def color(face_up):
        face_up_color=face_up.split(" ")[0]
        return face_up_color 
def num(face_up):
        face_up_num=face_up.split(" ")[1]
        return face_up_num
def can_play(hand, face_up):
    for i in hand:
          if color(i)==color(face_up) or num(i)==num(face_up):
                 return True
    return False
print(can_play(['yellow 3', 'yellow 5', 'red 8'], 'black 2'))