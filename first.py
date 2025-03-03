sentence = "it was a dark and stormy python"

def first_word(sentence):
    return sentence.split()[0]

def second_word(sentence):
    return sentence.split()[1]

def last_word(sentence):
    return sentence.split()[-1]




if __name__ == "__main__":
    print(first_word(sentence)) # it
    print(second_word(sentence)) # was
    print(last_word(sentence)) # python