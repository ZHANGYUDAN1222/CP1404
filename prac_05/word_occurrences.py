words=input('Text:').split()
word_to_count={}
for word in words:
    word_to_count[word]=word_to_count.get(word,0)+1
for k,v in sorted(word_to_count.items()):
    print('%s : %i'%(k,v))