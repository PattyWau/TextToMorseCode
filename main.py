#dict of alphabet and their morse code characters
char_dict = {"A":"*-","B":"-***","C":"-*-*","D":"-**","E":"*","F":"**-*","G":"--*","H": "****", "I":"**", "J":"*---","K":"-*-","L":"*-**",
 "M":"--","N":"-*","O":"---","P":"*--*","Q":"--*-","R":"*-*","S":"***","T":"-", "U":"**-","V":"***-","W":"*--","X":"-**-","Y":"-*--",
 "Z":"--**","1":"*----","2":"**---","3":"***--","4": "****-","5":"*****", "6":"-****", "7":"--***", "8":"---**","9":"----*", "0":"-----",
 ".": "*-*-*-","," :"--**--",":" :"---***","?":"**--**","'": "*----*","-": "-****-", " ": " ",
}

Encoder_on = True

#function to carry out encoding
def encode(msg):
  code=""
  try:
      for char in msg:
        code+=char_dict[char]
      print (f"Your encoded message:\n{code}")

  except KeyError:
      print("This punctuation does not exist in morse code, try again.")


while Encoder_on:
    #user decides whether to encode/not
    choice = input("Do you wish to encode(0) or to end program (1)? ").lower()

    def processing(str):
        global Encoder_on
        if str == "0":
            message = input("Input the messages you want to encode, adding a space between punctuations.\nEg:'Hello , How are you ?':\n ").upper()
            encode(message)

        elif str == "1":
            print("Thank you for using Text-To-Morse!")
            Encoder_on = False

    processing(choice)


















