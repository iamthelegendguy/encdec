#The program simply encrypts or decrypts your plain text messages!
class EncDec:
    #Function for the encryption process
   def Encodes():
      messageenc = input("Message: ")
      tempenc = messageenc
      messageenc = list(tempenc)#Adding the message to the list
      conversionenc = [ord(ch) for ch in messageenc]#Converting to ASCII numbers
      conversionenc1 = [(i + 101) for i in conversionenc]
      conversionenc = [(i * sec) for i in conversionenc1]
      conversionenc = [chr(ch) for ch in conversionenc]#Converting back to utf-8
      conversionenc = ''.join(str(e) for e in conversionenc)#Removing the brackets
      print(conversionenc)
      print('\tCopy the above text and send to decrypt!\n')
      print ("-----------------------------------------------------------")
      return
    #Function for the decryption process
   def Decodes():
      messagedec = input("Message: ")
      tempdec = messagedec
      messagedec = list(tempdec)#Adding the message to list
      conversiondec = [ord(ch) for ch in messagedec]#Converting to ASCII
      conversiondec2 = [(j // sec) for j in conversiondec]
      conversiondec = [(j - 101) for j in conversiondec2]
      conversiondec = [chr(ch) for ch in conversiondec]#Converting back to utf-8
      conversiondec = ''.join(str(e) for e in conversiondec)#Removing the brackets
      print(conversiondec)
      print('\tYour message is displayed above.\n')
      print ("-----------------------------------------------------------")
      return

   print("\tWelcome to Cryptography\n")
   print('\n')
   print("Make sure you have all the fonts installed in your system so that there is no any problem while encryption/decryption process.")
   print()
   print("The key is the same through the process. Make sure you and your partner use the same key.")
   print()
   #sec = int(input("Enter the secret key: "))
   global sec #Making the variable global so it can be used to use as a key in enc/dec process
   sec = int(input("Enter the secret key: "))
   looping = 1
   while (looping == 1):#For continuation of the program without exiting
      option = input("Encrypt, Decrypt or Exit? [e/d/x]")
      if ((option == 'e') or (option == 'E')):
         Encodes()
      elif ((option == 'd') or (option == 'D')):
         Decodes()
      elif ((option != 'x') or (option != 'X')):
         print("Exiting....")
         break
      else:
         print("Invalid key pressed!\n")
         print()
   exit() #Exits the program

