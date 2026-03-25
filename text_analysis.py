# text = "Python is powerful and python helps build powerful applications"
# Write code to:
# •	Count occurrences of each word 
# •	Return results as a dictionary 
# •	Treat uppercase and lowercase as the same

text = "Python is powerful and python helps build powerful applications"
def count_words(text):
    word_count = {}
    words = text.lower().split() #Kthimi i tekstit ne lowercase dhe ndarja e fjaleve
    for word in words:
        if word in word_count:
            word_count[word] += 1 #Rritja e numrit te fjales nese ekziston
        else:
            word_count[word] = 1 #Shtimi i fjales ne dictionary me vleren 1
    return word_count
print("Numri i fjaleve:", count_words(text))

#output: Numri i fjaleve: {'python': 2, 'is': 1, 'powerful': 2, 'and': 1, 'helps': 1, 'build': 1, 'applications': 1}