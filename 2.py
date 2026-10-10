s=str.lower(input()).split(' ')

#count_words={i:s.count(i) for i in s}
count_words=sorted({i:s.count(i) for i in s}, key=len)
#count_words={sorted(s, key=len):len(i) for i in s}

print(count_words)

