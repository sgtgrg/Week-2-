class StringManipulator:
     def find_character(self,text, char):
         return text.find(char)
     
     def get_length(self,text):
         return len(text)
     
     def convert_uppercase(self,text):
         return text.upper()
        
def reg():     
#Create an instace of the StringManipulator class
 name  = StringManipulator()

#Call the find_character method on the object
 result = name.find_character("example",'x')
 print("Index of 'x':", result) #Output: 1

#Call the get_length method
 length = name.get_length("example")
 print("Length of the string:",length)

#Call the convert_uppercase method
 uppercase = name.convert_uppercase("example")
 print("Uppercase of the word:",uppercase) 


if __name__ == "__main__":
    reg()