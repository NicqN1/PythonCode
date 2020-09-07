MORSE_CODE_DICT = { 'a':'.-', 'b':'-...',
   'c':'-.-.', 'd':'-..', 'e':'.',
   'f':'..-.', 'g':'--.', 'h':'....',
   'i':'..', 'j':'.---', 'k':'-.-',
   'l':'.-..', 'm':'--', 'n':'-.',
   'o':'---', 'p':'.--.', 'q':'--.-',
   'r':'.-.', 's':'...', 't':'-',
   'u':'..-', 'v':'...-', 'w':'.--',
   'x':'-..-', 'y':'-.--', 'z':'--..'}
def ltomorse(x):
    if "a" in x:
        x = x.replace("a",".- ")
    if "b" in x:
        x = x.replace("b","-... ")
    if "c" in x:
        x = x.replace("c","-.-. ")
    if "d" in x:
        x = x.replace("d","-.. ")
    if "e" in x:
        x = x.replace("e",". ")
    if "f" in x:
        x = x.replace("f","..-. ")
    if "g" in x:
        x = x.replace("g","--. ")
    if "h" in x:
        x = x.replace("h",".... ")
    if "i" in x:
        x = x.replace("i",".. ")
    if "j" in x:
        x = x.replace("j",".--- ")
    if "k" in x:
        x = x.replace("k","-.- ")
    if "l" in x:
        x = x.replace("l",".-.. ")
    if "m" in x:
        x = x.replace("m","-- ")
    if "n" in x:
        x = x.replace("n","-. ")
    if "o" in x:
        x = x.replace("o","--- ")
    if "p" in x:
        x = x.replace("p",".--. ")
    if "q" in x:
        x = x.replace("q","--.- ")
    if "r" in x:
        x = x.replace("r",".-. ")
    if "s" in x:
        x = x.replace("s","... ")
    if "t" in x:
        x = x.replace("t","- ")
    if "u" in x:
        x = x.replace("u","..- ")
    if "v" in x:
        x = x.replace("v","...- ")
    if "w" in x:
        x = x.replace("w",".-- ")
    if "x" in x:
        x = x.replace("x","-..- ")
    if "y" in x:
        x = x.replace("y","-.-- ")
    if "z" in x:
        x = x.replace("z","--.. ")
    return x

def mtoletter(message):
   message += ' '
   decipher = ''
   mycitext = ''
   for myletter in message:
      # checks for space
      if (myletter != ' '):
         i = 0
         mycitext += myletter
      else:
         i += 1
         if i == 2 :
            decipher += ' '
         else:
            decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
            .values()).index(mycitext)]
            mycitext = ''
   return decipher

def display_menu():
    print("1. Convert text to morse code")
    print("2. Convert morse code to text")
    print("0 Exit the program")
    print("")
    choice = input()

    if choice == "1":
        utext = str(input("Enter text: "))
        translation = ltomorse(utext)
        print(translation)

    if choice == "2":
        utext = str(input("Enter text: "))
        translation = mtoletter(utext)
        print(translation)

display_menu()