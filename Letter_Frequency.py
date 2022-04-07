"""
You are making a program to analyze text.

Take the text as the first input and a letter as the second input, and output the frequency of that letter in the text as a whole percentage.



Sample Input:

hello

l



Sample Output:

40



The letter l appears 2 times in the text hello, which has 5 letters. So, the frequency would be (2/5)*100 = 40.
"""

#solution
text = input()

letter = input()

len_text = len(text)

for letters in text:

    if letter in letters:

        num = text.count(letter)

        

        

        

result = int((num/len_text) * 100)

print(result)

