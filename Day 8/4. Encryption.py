alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text_arg, shift_arg):

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    #e.g.
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"
    cypher_text=""
    #cypher_text=[]
    for letter in text_arg:
        current_index=alphabet.index(letter)
        new_index = current_index + shift_arg
        if new_index<=(len(alphabet)-1):
            #cypher_text.append(alphabet[new_index])
            cypher_text+=alphabet[new_index]
        elif new_index>(len(alphabet)-1):
            new_index=new_index-(len(alphabet)-1)
            #cypher_text.append(alphabet[new_index])
            cypher_text+=alphabet[new_index]
    #concat_name = "".join(cypher_text)
    #print(f"The encoded text is {concat_name}")
    print(f"The encoded text is {cypher_text}")

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
encrypt(text_arg=text,shift_arg=shift)