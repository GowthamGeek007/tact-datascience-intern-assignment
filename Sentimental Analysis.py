#!/usr/bin/env python
# coding: utf-8

# In[45]:


import os
import nltk

txt="""Pay, Potential to advance,management,team lead.

This place is  run like a frat and sorority house. The management blames you out and you are racist.
They will do whatever to tear you down and please don't express to anyone anything personal because everyone will know.

This place was a nightmare and I feel for anyone that will not follow the status quo at this company.
Daring to be different and not kiss butt is a death..."""

from nltk.tokenize import word_tokenize

txt_tokens=word_tokenize(txt)#seperation of string to each parts is called tokens
print("TOKENS or SEPERATION OF STRING:")
for i in txt_tokens:
    print(i)

print("")


print("LENGTH OF THE TOKENS(words):",len(txt_tokens))#total number of items in the string is counted by the LEN method
print("")

print("THE NO.OF OCCURANCES OF WORD 'and':",fdist['and'])#no of occurances of a paarticular word EG:and
print("")


fdist_top5=fdist.most_common(5)
print("TOP 5 MOST USED WORDS or SYMBOLS:",fdist_top5)#the top most used words or symbols 
print("")


from nltk.tokenize import blankline_tokenize
txt_blank=blankline_tokenize(txt)
print("NO.OF PARAGRAPHS:",len(txt_blank))
print("")
#the no.of paragraphs are differentiated by BLANKLINES

from nltk.util import bigrams , trigrams , ngrams

txt_bigrams=list(nltk.bigrams(txt_tokens))
print("DOUBLE TOKENS:")
for i in txt_bigrams:
    print(i)
print("")
#tokens are seperated uniquely in 1st method...now it is seperated DUALLY


#FOR triple aand multi seperated TOKENS UNCOMMAND the below 10LINES


# txt_trigrams=list(nltk.trigrams(txt_tokens))
# print("TRIPLE TOKENS:")
# for i in txt_trigrams:
#     print(i)
# print("")

# txt_ngrams=list(nltk.ngrams(txt_tokens,4))
# print("MULTIPLE TOKENS:")
# for i in txt_ngrams:
#     print(i)
# print("")


#until this

from nltk.stem import PorterStemmer
pst=PorterStemmer()

print("STEMMING(root word) (sample word=HAVING):",pst.stem("having"))
print("")
#stemming is finding ROOT WORDS of words EG:ROOT WORD OF give,given,gave,giving  IS  give 


import re
punctuation=re.compile(r'[-.?!,:;()|0-9]')

post_punctuation=[]
for words in txt_tokens:
    word=punctuation.sub("",words)
    if len(word)>0:
        post_punctuation.append(word)

print("REMOVAL OF SYMBOLS AND NUMBERS(stop words):",post_punctuation)
print("")
#removal of unused words and numbers and symbols


print("PARTS OF SPEECH OF EACH WORDS:")
for token in post_punctuation:
    print(nltk.pos_tag([token]))
print("")
#parts of speech of each words EG:NOUN,SUBJECT,VERB




from nltk import ne_chunk
NE_sent="The US President stays in the White HOUSE"

print("SAMPLE STRING FOR NER:",NE_sent)
NE_tokens=word_tokenize(NE_sent)
NE_tags=nltk.pos_tag(NE_tokens)


NE_NER=ne_chunk(NE_tags)
print("NER(Naming Entity Recognization):",NE_NER)
print("")

from nltk.probability import FreqDist
fdist=FreqDist()

for word in txt_tokens:
    fdist[word.lower()]+=1
print("NO.OF OCCURANCES OF ALL WORDS:")
fdist
#find no.of occurances of a word.
#lower is used to avoid capital letters confusion

#PACKAGES DOWNLOADED
# nltk.download('maxent_ne_chunker')
# nltk.download('words')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('punkt')


# In[ ]:




