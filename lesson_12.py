import random
import msvcrt











n = int(input("N: "))
hp = 3
scores = 0
monkey_row = random.randint(1, n)
monkey_column = random.randint(1, n)
monkey_emoji = ':monkey:'





banana_row = random.randint(1, n)
banana_column = random.randint(1, n)
banana_emoji = ':banana:'

bomb_row = random.randint(1, n)
bomb_colomn = random.randint(1, n)
bomb_emoji = ":bomb:"

heart_row = random.randint(1, n)
heart_colomn = random.randint(1, n)
heart_emoji = ":heart:"

eagle_row = random.randint(1, n)
eagle_colomn = random.randint(1, n)
eagle_emoji = ":eagle:"







while True:
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == monkey_row and j == monkey_column:
                print(':monkey:', end='\t')
            elif i == banana_row and j == banana_column:
                print(':banana:', end='\t')
            elif i == bomb_row and j == bomb_colomn and scores >= 3:
               print(':bomb:', end='\t')
            elif i == heart_row and j == heart_colomn and scores >= 3:
               print(":heart:", end="\t")
            elif i == eagle_row and j == eagle_colomn and scores >= 2:
               print(":eagle:", end="\t")

            else:
                print('*', end='\t')
        print()
    print(hp * ':heart: ')
    print(scores * ':star:')







    monkey_step = msvcrt.getwche()
    print()
    monkey_step == monkey_step.lower()
    if monkey_step == 'q':
     break
    elif monkey_step == 'w':
     monkey_row -= 1
    elif monkey_step == 's':
       monkey_row += 1
    elif monkey_step == 'a':
       monkey_column -= 1
    elif monkey_step == 'd':
       monkey_column += 1

    if monkey_row == banana_row and monkey_column == banana_column:
        scores += 1
        banana_row = random.randint(1, n)
        banana_column = random.randint(1, n)
    if monkey_row == bomb_row and monkey_column == bomb_colomn:
       hp -= 1
       bomb_row = random.randint(1, n)
       bomb_colomn = random.randint(1, n)
    if hp == 0:
       print("GAME OVER!!!")
       break
    if monkey_row == heart_row and monkey_column == heart_colomn:
       hp += 1
       heart_row = random.randint(1, n)
       heart_colomn = random.randint(1, n)
    if monkey_row == eagle_row and monkey_column == eagle_colomn:
       hp -= 1
       eagle_row = random.randint(1, n)
       eagle_colomn = random.randint(1, n)
    if scores > 2:
        if eagle_row < monkey_row:
            eagle_row += 1
        elif eagle_row > monkey_row:
            eagle_row -= 1
        elif eagle_colomn < monkey_column:
             eagle_colomn += 1
        elif eagle_colomn > monkey_column:
             eagle_colomn -= 1

if scores >= 15:
    print("WELL DONE!!")