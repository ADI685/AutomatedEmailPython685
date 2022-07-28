import  smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage
 
 
 
listener = sr.Recognizer()
 
 
def pylisten():
    
    try:
        with sr.Microphone() as source:
            print("listening......")
            voice=listener.listen(source)
            info = listener.recognize_google(voice)
            return info.lower()
        
    except:
        pass
 
 
 
def sendMail(rec,subject,message):
    server = smtplib.SMTP('smtp.gmail.com', 587) # server and port number
    server.starttls()
    server.ehlo()
    server.login('your@email.com','email_code')
    email =  EmailMessage()
    email["From"]='your@email.com'
    email['To'] = rec
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)
    print("DONE")
    pytalk("your mail has been successfully sent")
        
 
 
 
def pytalk(text):
    print(text)
    engine = pyttsx3.init()
    engine.setProperty('rate', 130)
    engine.say(text)
    engine.runAndWait()
 
 
 
mailList={

    "ramesh":"ramesh16@something.com",
    }
 
 
 
 
def main():
    pytalk("Welcome, to whom you wanted to send email")
    receiver = pylisten()
    
    if receiver == None or " " in receiver :
        pytalk("Sorry You are not audible")
        pytalk("please type your receiver's mail id")
        rec=input("receiver's mail id : ")
        if rec == None:
            pytalk("No response")
            return
    
    else:
        if receiver not in mailList:
            pytalk("please type your receiver's mail id is not saved please type in mail ")
            rec=input("receiver's mail id : ")
            if rec == None:
                pytalk("No response")
                return
            mailList["receiver"]=rec
        else:
            rec = mailList[receiver]
    pytalk("your email will be send to " +str(rec))
        
        
    pytalk("what is the subject of your email")
    subject= pylisten()
    if subject == None:
        subject=""
        pytalk("Sorry You are not audible")
        pytalk("there is no subject for this mail")
    else:
        pytalk("your email subject is "+ str(subject))
        
        
    pytalk('Tell me the body of your mail?')
    
    
    reply = pylisten()
    pytalk(reply)
    while True:
        pytalk("do you want to add more")
        reply1 = pylisten()
        if reply1 == "yes":
            print("Yes")
            pytalk("add more")
            j = pylisten()
            reply = reply +"  " + str(j)
        else:
            break
        
        
    pytalk("your final message is")
    pytalk(reply)
    sendMail(rec,subject, reply)
    
  
    
            
main()
