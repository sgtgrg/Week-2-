class SentenceManipulator:
    def word_count(self, sentence):
      words = sentence.split()
      return len(words)

def reg():
    #Create an instance of the SentenceManipulator class
    counter = SentenceManipulator()

    #Get sentence inout from the user
    sentence = input("Please enter your desired sentence: ")
    
    #Call the word_count method
    begin_count = counter.word_count(sentence)
    
    #Print the number of words in the sentence
    print("The number of words in the given sentence: ", begin_count)
    
if __name__ == "__main__":
    reg()

    