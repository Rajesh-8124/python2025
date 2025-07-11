import pywhatkit

number = input("Enter recevier's phone number (with countary code) :")
massage = input("Enter massage :")
t1 = int(input("Enter hour in 24 hour format :"))
t2 = int(input("Enter minute :"))

pywhatkit.sendwhatmsg(number, massage, t1, t2,20,True, 15)
