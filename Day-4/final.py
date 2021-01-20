import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
listChooses = [rock, paper, scissors]
choose = int(
    input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: '))
print(listChooses[choose])
computer_choose = random.randint(0, 2)
print('Computer choose: ')
print(listChooses[computer_choose])
if choose == computer_choose:
    print('Draw')
elif choose == 0 and computer_choose == 2:
    print('You lose ')
elif computer_choose == 0 and choose == 2:
    print('You win ! ')
elif computer_choose > choose:
    print('You Lose')
elif choose > computer_choose:
    print('You Win')
