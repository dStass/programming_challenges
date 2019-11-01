'''
Given 2 strings of length n, return the 'pin' distance between two words
A pin distance is given by the sum of the difference of each number once the strings
have been converted to a pin of numbers. The pin system follows the system:

  1      2      3
[   ]  [abc]  [def]

  4      5      6
[ghi]  [jkl]  [mno]

  7      8      9
[pqrs] [tuv] [wxyz]

         0
       [ _ ]


Similar to the lock screen of a mobile phone

Example: pdist('mean', 'stat') = 3
= difference between 6326 and 7828, 6!=7, 3!=8, 2==2, 6!=8

bring = 27464
arioi - 27464
'''
import math

class PinDistance:
  _ctoi = None  # char to int, int to str map
  _lexpart = None  # partitioned lexicon
  _chars = None  # position of characters
  _words = None

  def __init__(self, lex='words.txt'):
    self._ctoi = {}  # char to int
    self._lexpart = {}
    self._words = {}

    self._chars = [[' 0', [4, 2]], ['1', [1,1]], ['abc1', [1,2]],['def2', [1,3]],
                  ['ghi3',[2,1]], ['jkl4', [2,2]],['mno5', [2,3]],
                  ['pqrs6', [3,1]],['tuv7', [3,2]],['wxyz8', [3,3]]]
    for i in range(len(self._chars)):
      for c in self._chars[i][0]:
        self._ctoi[c] = i
      self._ctoi[(i+2)] = self._chars[i][0]

    self.load_lex(lex)


  def load_lex(self, lex):
    f = open(lex)
    line = f.readline()
    while line:
      line = line[:-1]  # remove \n
      if self._words.get(line, False):
        continue
      
      length = len(line)
      lexicon_of_length = self._lexpart.get(length, [])
      lexicon_of_length.append(line)
      self._lexpart[length] = lexicon_of_length
      self._words[line] = True
      line = f.readline()
    f.close()
    print('Done loading lexicon:', lex)


  def pdist(self, str1, str2):
    if len(str1) != len(str2):
      return -1

    difference = 0
    for i in range(len(str1)):
      if str1[i] == '.' or str2[i] == '.':
        continue
      str1i = self._ctoi[str1[i]]
      str2i = self._ctoi[str2[i]]
      difference += 0 if str1i == str2i else 1
    return difference


  def pdist_away(self, word, difference=0):
    to_return = []
    word_len = len(word)
    same_words = self._lexpart[word_len]
    for w in same_words:
      if self.pdist(w, word) == difference:
        to_return.append(w)
    return to_return


  def min_pdist_away(self, word, difference):
    to_return = []
    word_len = len(word)
    same_words = self._lexpart[word_len]
    for w in same_words:
      if self.pdist(w, word) >= difference:
        to_return.append(w)
    return to_return


  def max_pdist_away(self, word, difference):
    to_return = []
    word_len = len(word)
    same_words = self._lexpart[word_len]
    for w in same_words:
      if self.pdist(w, word) <= difference:
        to_return.append(w)
    return to_return


  def words_from_pin(self, pin):
    length = len(pin)
    artificial_word = ''
    for i in range(length):
      if pin[i] == '0' or pin[i] == '1':
        artificial_word += '.'
      else:
        artificial_word += self._ctoi[int(pin[i])][0]
    return self.pdist_away(artificial_word, 0)


  def pin_from_word(self, word):
    pin = ''
    for c in word:
      pin += str(self._ctoi[c])
    return pin

  
  def time_to_text(self, message, time=1):
    if len(message) == 0:
      return 0
    loc = None
    total = 0
    for m in message:
      loc_next = self._chars[self._ctoi[m]][1]
      dist = self.euclid_distance(loc, loc_next)
      for c in self._chars[self._ctoi[m]][0]:
        if c == m:
          break
        total += time  # to change to right char
      total += time  # to press
      total += time * dist  # to move finger between buttons
      loc = loc_next
    
    return total
      

  
  def euclid_distance(self, loc1, loc2):
    if not loc1 or not loc2:
      return 0
    return math.sqrt(math.pow(loc1[0] - loc2[0], 2) + math.pow(loc1[1] - loc2[1], 2))



pd = PinDistance('words.txt')
print(pd.pdist_away('elaine',1))
print(pd.pin_from_word('hero'))

# print(pd.time_to_text('hello my name is david', 0.5))