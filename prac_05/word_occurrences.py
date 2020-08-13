words=input('TEXT:').split()
word_to_count={}
for word in words:
    word_to_count[word]=word_to_count.get(word,0)+1
for k,v in sorted(word_to_count.items()):
    print('%10s : %2i'%(k,v))