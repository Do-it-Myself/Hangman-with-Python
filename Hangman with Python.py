import time
import random

# begin game
print('Welcome to Hangman Game!')
time.sleep(0.5)
name = input('What\'s your name? ')
time.sleep(0.5)
print('Hello ' + name + '! Good luck!')
print('')
time.sleep(0.5)

# initialize variables
life = 6

# define functions
def hangman():
  if life == 6:
    print("   _____ \n"
          "  |     | \n"
          "  |      \n"
          "  |      \n"
          "  |      \n"
          "__|__\n")
  elif life == 5:
    print("   _____ \n"
          "  |     | \n"
          "  |     O \n"
          "  |      \n"
          "  |      \n"
          "__|__\n")
  elif life == 4:
    print("   _____ \n"
          "  |     | \n"
          "  |     O \n"
          "  |     | \n"
          "  |      \n"
          "__|__\n")
  elif life == 3:
    print("   _____ \n"
          "  |     | \n"
          "  |     O \n"
          "  |    /| \n"
          "  |      \n"
          "__|__\n")
  elif life == 2:
    print("   _____ \n"
          "  |     | \n"
          "  |     O \n"
          "  |    /|\ \n"
          "  |      \n"
          "__|__\n")
  elif life == 1:
    print("   _____ \n"
          "  |     | \n"
          "  |     O \n"
          "  |    /|\ \n"
          "  |    /  \n"
          "__|__\n")
  elif life == 0:
    print("   _____  \n"
          "  |     | \n"
          "  |     O \n"
          "  |    /|\ \n"
          "  |    / \ \n"
          "__|__\n")

def win():
  print('You have won :D')
  time.sleep(0.5)
  final_display_string = ' '.join(word.upper())
  print('The word is:', final_display_string)
  time.sleep(0.5)
  print("\O/ - Thank you for saving me! \n"
        " | \n"
        "/ \ \n")

def lose():
  print('You have lost :(')
  time.sleep(0.5)
  final_display_string = ' '.join(word.upper())
  print('The word is:', final_display_string)
  time.sleep(0.5)
  hangman()

# initialize word for guessing
# https://arraythis.com/
word_list = ['Android', 'about', 'account', 'across', 'addition', 'adjustment', 'advertisement', 'affix', 'after', 'again', 'against', 'agreement', 'almost', 'among', 'amount', 'amusement', 'angle', 'angry', 'animal', 'answer', 'apparatus', 'apple', 'approval', 'argument', 'attack', 'attempt', 'attention', 'attraction', 'authority', 'automatic', 'avenue', 'awake', 'awkward', 'balance', 'basin', 'basket', 'beautiful', 'because', 'beekeeper', 'before', 'behaviour', 'belief', 'berry', 'between', 'birth', 'bitter', 'black', 'blade', 'blood', 'board', 'boggle', 'boiling', 'bottle', 'brain', 'brake', 'branch', 'brass', 'bread', 'breath', 'brick', 'bridge', 'bright', 'broken', 'brother', 'brown', 'brush', 'bucket', 'building', 'burst', 'business', 'butter', 'button', 'camera', 'canvas', 'carriage', 'cause', 'certain', 'chain', 'chalk', 'chance', 'change', 'cheap', 'cheese', 'chemical', 'chest', 'chief', 'church', 'circle', 'clean', 'clear', 'clock', 'cloth', 'cloud', 'cobweb', 'collar', 'colour', 'comfort', 'committee', 'common', 'company', 'comparison', 'competition', 'complete', 'complex', 'condition', 'connection', 'conscious', 'control', 'copper', 'cotton', 'cough', 'country', 'cover', 'crack', 'credit', 'crime', 'cruel', 'crush', 'current', 'curtain', 'curve', 'cushion', 'cycle', 'damage', 'danger', 'daughter', 'death', 'decision', 'degree', 'delicate', 'dependent', 'design', 'desire', 'destruction', 'detail', 'development', 'different', 'digestion', 'direction', 'dirty', 'discovery', 'discussion', 'disease', 'disgust', 'distance', 'distribution', 'division', 'doubt', 'drain', 'drawer', 'dress', 'drink', 'driving', 'duplex', 'early', 'earth', 'education', 'effect', 'elastic', 'electric', 'engine', 'enough', 'equal', 'equip', 'error', 'event', 'every', 'example', 'exchange', 'existence', 'exodus', 'expansion', 'experience', 'expert', 'false', 'family', 'father', 'feather', 'feeble', 'feeling', 'female', 'fertile', 'fiction', 'field', 'fight', 'finger', 'first', 'fixed', 'flame', 'flight', 'floor', 'flower', 'foolish', 'force', 'forward', 'frame', 'frequent', 'friend', 'front', 'fruit', 'funny', 'future', 'galaxy', 'garden', 'general', 'glass', 'glove', 'gossip', 'government', 'grain', 'grass', 'great', 'green', 'group', 'growth', 'guide', 'hammer', 'hanging', 'happy', 'harbour', 'harmony', 'healthy', 'hearing', 'heart', 'history', 'hollow', 'horse', 'hospital', 'house', 'humour', 'icebox', 'important', 'impulse', 'increase', 'industry', 'injury', 'insect', 'instrument', 'insurance', 'interest', 'invention', 'island', 'ivory', 'jackpot', 'jelly', 'jelly', 'jewel', 'jockey', 'joking', 'journey', 'joyful', 'judge', 'jumbo', 'kayak', 'kettle', 'khaki', 'kiosk', 'knife', 'knowledge', 'language', 'laugh', 'learning', 'leather', 'lengths', 'letter', 'level', 'library', 'light', 'limit', 'linen', 'liquid', 'little', 'living', 'loose', 'lucky', 'luxury', 'lymph', 'machine', 'manager', 'market', 'married', 'match', 'material', 'measure', 'medical', 'meeting', 'memory', 'metal', 'middle', 'military', 'minute', 'mixed', 'money', 'monkey', 'month', 'morning', 'mother', 'motion', 'mountain', 'mouth', 'muscle', 'music', 'narrow', 'nation', 'natural', 'necessary', 'needle', 'nerve', 'night', 'nightclub', 'noise', 'normal', 'north', 'number', 'observation', 'offer', 'office', 'operation', 'opinion', 'opposite', 'orange', 'order', 'organization', 'ornament', 'other', 'ovary', 'owner', 'paint', 'pajama', 'paper', 'parallel', 'parcel', 'paste', 'payment', 'peace', 'pencil', 'person', 'physical', 'picture', 'place', 'plane', 'plant', 'plate', 'please', 'pleasure', 'plough', 'pneumonia', 'pocket', 'point', 'poison', 'polish', 'political', 'porter', 'position', 'possible', 'potato', 'powder', 'power', 'present', 'price', 'print', 'prison', 'private', 'probable', 'process', 'produce', 'profit', 'property', 'prose', 'protest', 'public', 'punishment', 'puppy', 'purpose', 'quality', 'question', 'quick', 'quiet', 'quite', 'range', 'reaction', 'reading', 'ready', 'reason', 'receipt', 'record', 'regret', 'regular', 'relation', 'religion', 'representative', 'request', 'respect', 'responsible', 'reward', 'rhythm', 'right', 'river', 'rough', 'round', 'scale', 'school', 'science', 'scissors', 'scratch', 'screw', 'second', 'secret', 'secretary', 'selection', 'sense', 'separate', 'serious', 'servant', 'shade', 'shake', 'shame', 'sharp', 'sheep', 'shelf', 'shirt', 'shock', 'short', 'silver', 'simple', 'sister', 'skirt', 'sleep', 'slope', 'small', 'smash', 'smell', 'smile', 'smoke', 'smooth', 'snake', 'sneeze', 'society', 'solid', 'sound', 'south', 'space', 'spade', 'special', 'sponge', 'spoon', 'spring', 'square', 'staff', 'stage', 'stamp', 'start', 'statement', 'station', 'steam', 'steel', 'stick', 'sticky', 'stiff', 'still', 'stitch', 'stocking', 'stomach', 'stone', 'store', 'story', 'straight', 'strange', 'street', 'stretch', 'stretch', 'strong', 'structure', 'substance', 'sudden', 'sugar', 'suggestion', 'summer', 'support', 'surprise', 'sweet', 'system', 'table', 'taste', 'teaching', 'tendency', 'theory', 'there', 'thick', 'thing', 'thought', 'thread', 'throat', 'through', 'through', 'thumb', 'thunder', 'ticket', 'tight', 'tired', 'together', 'tomorrow', 'tongue', 'tooth', 'touch', 'trade', 'train', 'transport', 'trick', 'trouble', 'trousers', 'twist', 'umbrella', 'under', 'value', 'verse', 'vessel', 'violent', 'voice', 'waiting', 'waste', 'watch', 'water', 'weather', 'weight', 'wheel', 'where', 'while', 'whistle', 'white', 'window', 'winter', 'woman', 'wound', 'writing', 'wrong', 'yellow', 'yesterday', 'young']
word_index = random.randint(0, len(word_list)-1)
word = word_list[word_index]
display_list = []
display_string = ''
guessed_letter_list = []
wrong_letter_list = []
wrong_letter_string = ''

for letter in word:
  display_list.append('_')
display_string = ' '.join(display_list)

print('The word is: ' + display_string)
time.sleep(0.5)
print('Remaining guesses: ' + str(life))
time.sleep(0.5)
hangman()
time.sleep(0.5)

while True:
  # player interacts
  print('')
  guessed_letter = input('Enter a letter: ')
  time.sleep(0.5)

  # check input validity
  if len(guessed_letter) != 1:
    print('Invalid input!')
    continue
  elif not guessed_letter.isalpha():
    print('Invalid input!')
    continue
  elif guessed_letter_list.count(guessed_letter.upper()) > 0:
    print('You have guessed this letter already!')
    continue
  
  # check whether letter is correct
  guessed_letter_list.append(guessed_letter.upper())

  iteration = 0
  correct_flag = False

  for letter in word:
    # if any letter matches
    if letter.upper() == guessed_letter.upper():
      display_list[iteration] = guessed_letter.upper()
      correct_flag = True
    iteration += 1
  
  # if correct
  if correct_flag:
    pass
  # if wrong
  else:
    life -= 1
    wrong_letter_list.append(guessed_letter.upper())
    wrong_letter_string = ', '.join(wrong_letter_list)

  display_string = ' '.join(display_list)



  # if won
  if display_list.count('_') == 0:
    win()
    break

  # if lost
  if life <= 0:
    lose()
    break

  # if neither
  print('The word is: ' + display_string)
  time.sleep(0.5)
  print('Wrong letter guessed: ' + wrong_letter_string)
  time.sleep(0.5)
  print('Remaining guesses: ' + str(life))
  time.sleep(0.5)
  hangman()
  time.sleep(0.5)
