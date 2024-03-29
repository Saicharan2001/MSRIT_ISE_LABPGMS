#!/usr/bin/env python


#Introduction to Python : Classes & Objects, Functions
#a)  Write a python class to reverse a sentence (initialized via constructor) word by word.
#That is: “I am here” should be reversed as “here am I”. Create instances of this class
#for each of the three strings input by the user and display the reversed string for each,
#in descending order of number of vowels in the string

# Note : Handle all other corner cases which are not handled here
class SentenceReverser:
	vowels = ["a","e","i","o","u"]
	sentence = ""
	reverse = ""
	vowelCount = 0
	def __init__(self,sentence):
		self.sentence = sentence
		self.reverseSentence()
	def reverseSentence(self):
		self.reverse = " ".join(reversed(self.sentence.split()))
	def getVowelCount(self):
		self.vowelCount = sum(s in SentenceReverser.vowels for s in self.sentence.lower())
		return self.vowelCount
	# def getReverse(self):
	# 	return self.reverse

items = []

for i in range(3):
	sentence = input("Enter a phrase : ")
	reverser = SentenceReverser(sentence.strip())
	items.append(reverser)  #List storing the three objects
	print()

sortedItems = sorted(items, key=lambda item: item.getVowelCount(), reverse=True)

print ("Sorted on vowel count (descending) : \n")
for i in range(len(sortedItems)):
	print ("Reverse : ", sortedItems[i].reverse, ", Vowel Count : ", sortedItems[i].getVowelCount())


# class SentenceReverser:
# 	vowels=["a","e","i","o","u"]
# 	sentence=""
# 	reverse=""
# 	getvowelcount=0
# 	def __init__(self,senten):
# 		self.sentence=senten
# 		self.reversal()
# 	def reversal(self):
# 		self.reverse=" ".join(reversed(self.sentence.split()))
# 		self.vowelcount()
# 	def vowelcount(self):
# 		self.getvowelcount=sum(i in self.vowels for i in self.sentence.lower())


# items=[]
# for i in range(3):
# 	sent=input("Enter the sentence")
# 	items.append(SentenceReverser(sent))

# sorted_items=sorted(items,key=lambda item:item.getvowelcount,reverse=True)

# for i in sorted_items:
# 	print(i.sentence," ",i.reverse," ",i.getvowelcount)