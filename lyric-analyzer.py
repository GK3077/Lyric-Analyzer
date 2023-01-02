text = "All smiles, I know what it takes to fool this town I'll do it 'til the sun goes down And all through the nighttime Oh, yeah Oh, yeah, I'll tell you what you wanna hear Leave my sunglasses on while I shed a tear It's never the right time Yeah, yeah "
print(text.split())
word_count = { }
for word in text.split():
  if word in word_count:
    word_count[word]+=1
  else:
    word_count[word] =1

      
word_count0 = { }
for word in text.lower().split():
  if word in word_count:
    word_count0[word]+=1
  else:
    word_count0[word] =1   
