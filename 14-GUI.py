# exercise
 #Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

for item in picture:
    for pixel in item:
        if pixel == 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print('')        
    
# to have a good code 
# code should be clean
#readability 
# predictability
# don't repeat yourself    