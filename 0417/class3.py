def match_words(words):
  ctr = 0

  for word in words:
    if len(word) > 1 and word[0] == word[-1]:
      ctr += 1
  return ctr

s= ['aba', 'xyz', 'abc', '121']
print(s)
print('문자열의 개수=', match_words(s))