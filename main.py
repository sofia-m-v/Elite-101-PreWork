import random

name= input('Hello! What is your name?\n')

print(f'What a nice name, {name}!\n')

mood=input('How are you doing today?\n')

if mood == 'good' :
  print('That is great to hear!\n')
elif mood == 'bad' :
  print('Oh no... sorry to hear that\n')
elif mood == 'tired' :
  print('Yeah, me too...\n')

print('Tell me more about yourself....')

origin = input ('Where are you from?\n')
print(f'Oh, that\'s cool! I really like {origin}....')

place = input (f'What\'s your favorite place to go to {origin}?\n')

print('Nice!')

def generate_responses(user_input):
  responses = [
    'How interesting!', 
    'Very nice', 
    'That\'s cool']
  return random.choice(responses)
 
family = input ('Tell me about your family...\n')

print (generate_responses)

life = input('What do you want to be when you grow up?')

last = input('Anything else you want to tell me?')

while last != 'bye':
  print (generate_responses)