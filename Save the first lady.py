print("Welcome to Sambisa Forest")
print("Your mission is to save the Kidnapped First Lady") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
First_move = input('You lost your map and your compass is broken. You have come to a crossroad, where do you turn? Type "Right" to go right or "Left" to go left\n')

if First_move == 'Right':
  second_move = input('Great Choice! But you are now faced with a river, what do you do?\n Type "Swim" to swim through the river or "Wait" to wait for a boat\n')
  if second_move == 'Wait':
    third_move = input('Luckily, a deserted boat washed up the river and you have paddled it till you got to a house.\nThis house has three doors with different colours\nType "Red" to go through the first door.\nType "Blue" to go through the second door.\nType "Yellow" to go through the third door. \n')
    if third_move == 'Blue':
      print('Did you write your will, because you are surely not returning home as you now lie in the belly of a beast lurking behind the door.\nMission failed')

    elif third_move == 'Red':
      print('Unfortunately, a trip-wire was placed on the hinges of the door. Now you have been blown to pieces. \nMission failed')

    elif third_move == 'Yellow':
      print('You are a true soldier! You have saved the First Lady, your reward awaits you!\nMission Accomplished.')
    
    else:
      print('Worst move! You just fell into a bottomless pit. Mission failed')
    
  else:
    print('Did you forget you are a bad swimmer?! Well now you have drowned. Mission failed!')

else:
  print('You stepped on a mine and got blown up.\nMission Failed!')
    