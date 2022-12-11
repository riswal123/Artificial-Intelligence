# import modules all modules
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import pyjokes
import ctypes
import wolframalpha







engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
##print(voices[1].id)

engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good Evening")

    speak("I am NOAH How can i Help you, Sir")
    print("I am NOAH How can i Help you, Sir")
    
    '''assname =("NOAH 1 point 0")
    speak("I am your Assistant")
    speak(assname)
    def usrname():
        speak("What should i call you sir")
        uname = takeCommand()
        speak("Welcome Mister")
        speak(uname)
        columns = shutil.get_terminal_size().columns
	
        print("#####################".center(columns))
        print("Welcome Mr.", uname.center(columns))
        print("#####################".center(columns))
        speak("How can i Help you, Sir")'''
    



def takeCommand():
    #it takes microphone input to user and return string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listenig...")
        r.pause_threshold=0.8
        r.energy_threshold = 400
        audio=r.listen(source)

    try:
        query=("You said " + r.recognize(audio))
        print(query)
##        query=r.recognize_google(audio, language='eng-in')
        print(f"User said:{query}\n")

    except Exception as e:
        print(e)
        print("say that again please...")
        return"None"
    return query
            
if __name__=="__main__":
    speak("hello sir")
    wishMe()


    while True:
        query = takeCommand().lower()


    #logic for executinh taks based on query


        if"wikipedia" in query:
            speak("Searching wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("Accordinng to wikipedia")
            print(results)
            speak(results)
            
        elif"open youtube" in query:
            speak("okay sir. i am opening youtube")
            webbrowser.open("https://www.youtube.com/")
            
        elif"open google" in query:            
            webbrowser.open("google.com")
            
        elif"open facebook" in query:
            speak("ok sir. i am opening facebook")
            webbrowser.open("https://www.facebook.com/")

        elif"open instagram" in query:
            speak("okay sir. i am opening instagram")
            webbrowser.open("https://www.instagram.com/")
            
        elif"open majhinaukari" in query:
            speak("okay sir. i am opening majhinaukari")
            webbrowser.open("majhinaukari.com")



        elif"open Nmk" in query:
            speak("okay sir. i am opening nmk")
            webbrowser.open("nmk.com")

            
        elif"open music" in query:
            speak("okay sir. i am opening youtube music")
            webbrowser.open("https://music.youtube.com/")
            
        elif "play music"in query:
            speak("Here you go with music")
            n = random.randint(0,55)
            #print(n)
            music_dir ="F:\\song"
            files=os.listdir(music_dir)
            songs = os.listdir(music_dir)
            #print(songs)
            os.startfile(os.path.join(music_dir, songs[n]))



        elif "favourite song"in query:
            speak("Here you going with a favourite music")
            n = random.randint(0,55)
            #print(n)
            music_dir ="F:\\Song\\Favourite Song"
            files=os.listdir(music_dir)
            songs = os.listdir(music_dir)
            #print(songs)
            os.startfile(os.path.join(music_dir, songs[n]))
                    
        elif "open whatsapp" in query:
            speak("okay sir. opening whatsapp")
            codePath = "C:\\Users\\anilr\\AppData\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(codePath)

        elif "open stack overflow" in query:
            speak("okay sir. opening stack overflow")
            webbrowser.open("https://stackoverflow.com/")
            
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            
        elif 'open code' in query:
            speak("okay sir. i am opening code")
            codePath = "C:\\Users\\anilr\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

            
        elif"open chrome" in query:
            speak("okay sir. i am opening google chrome")
            codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)


        


        elif "python" in query:
            speak("okay sir. i am opening idel library")
            codePath ="C:\\Users\\anilr\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\idlelib\\idle.pyw"
            os.startfile(codePath)

                    

        elif"shutdown" in query:
            speak("Do you wish to shutdown your computer")
            if "no" in query:
                speak("thank u sir will not shut down the computer")
            if "yes" in query:
                speak("Shutting the computer")
                os.system("shutdown /s /t 2")
                break
            

        elif"restart computer" in query:
            speak("do you want to re restart your system")
            if "no" in query:
                speak("thank u sir will not re start the system")
            if "yes" in query:
                speak("restartting the system")   
                os.system("shutdown /r /t 2")
                break


        elif "goodbye" in query or "good night" in query or "shut up" in query or "bye" in query or "get lost" in query or "stop" in query:
            speak("good bye")
            quit()


        elif "your name" in query or "who are you" in query:
            stMsgs = ["I was created as a Minor project by Mister Anil", "not Sure", "i am NOAH sir"]
            ans_q = random.choice(stMsgs)
            speak(ans_q)  
            ans_take_from_user_how_are_you = takeCommand()

        elif "reason for you" in query or "why are you" in query:
            stMsgs = ["my name is Noah", "I am your virtual assistant created by Anil"]
            ans_q = random.choice(stMsgs)
            speak(ans_q)  
            ans_take_from_user_how_are_you = takeCommand()


        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,0,"F:\\Photo Shoot 08-05-21",0)
            speak("Background changed succesfully")



        elif "who i am" in query:
            stMsgs = ["If you talk then definitely your human.", "If you have piling then definitely your human"]
            ans_q = random.choice(stMsgs)
            speak(ans_q)  
            ans_take_from_user_how_are_you = takeCommand()

        

        elif "why you come to world" in query:
            speak("Thanks to Anil, Further It's a secret")


        elif "search" in query or "play" in query:
            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)

        elif "good morning" in query:
            speak("A warm" +query)
            speak("How are you Mister")


        elif "how are you" in query:
            stMsgs = ['i am fine, how about you!', 'I am fine!, lets talk about you are you fine?', 'I am nice and in full mood of helping you','i am okay ! How are you']
            ans_q = random.choice(stMsgs)
            speak(ans_q)  
            ans_take_from_user_how_are_you = takeCommand()


        elif "will you be my gf" in query or "will you be my bf" in query:
            stMsgs = ["I'm not sure about, may be you should give me some time","I lovespending time with you,we have a great person-to-AI kind of relationship"]
            ans_q = random.choice(stMsgs)
            speak(ans_q)  
            ans_take_from_user_how_are_you = takeCommand()
            
        elif "who is rushikesh" in query:
            speak("rushikesh is good boy, is his friend of anil")

	
        elif "open google classroom" in query:

            speak("opening google classroom")
            webbrowser.open("https://classroom.google.com/u/3/h")


        elif "open spotify" in query:
            speak("opening spotify")
            webbrowser.open("https://open.spotify.com/")

        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")


        elif "open my favourite songs album" in query:
            speak("opening your favourite music albumb")
            webbrowser.open("https://open.spotify.com/artist/2NjfBq1NflQcKSeiDooVjY?si=XvPrJaBNSnadmX8iWTlpyw")


        elif "open my gmail" in query:
            speak("okay, opening your gmail")
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

        elif "hello" in query or "hi" in query or "hey" in query:
            stMsgs = ['hi how can i help you today', 'hello there, what can i do for you', 'hey, what can i help you with today','hello, what do you want me to do today']
            ans_q = random.choice(stMsgs)
            speak(ans_q)  
            ans_take_from_user_how_are_you = takeCommand()


        elif "what's the weather " in query:
            speak("looking for the weather...")
            #r = sr.Recognizer()
            results =webbrowser.open ("https://www.google.com/search?rlz=1C1CHBF_enIN911IN911&biw=1536&bih=763&sxsrf=ALeKk02WEeO5ibqsklVfK4AaRYshJYil7g%3A1598262964246&ei=tI5DX63LDrSX4-EP_bOA8A4&q=google+weather&oq=googweather&gs_lcp=CgZwc3ktYWIQAxgAMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB46BAgAEEdQ7i1Y0jJgwTxoAHACeAGAAYEDiAHmBZIBBzEuMi4wLjGYAQCgAQGqAQdnd3Mtd2l6wAEB&sclient=psy-ab")

        elif "fine" in query or "im good" in query or "even im okay" in query or "nice" in query or "yeah" in query or "yes im nice" in query or "yes" in query:
            speak("oh that's nice, anyways what can i help you with today?")


        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)


        elif "what's up" in query:
            stMsgs = ['asif now im only helping you with whatever you need me for', 'I am fine!, lets talk about you are you fine?', 'oh, nothing','i am okay ! How are you']
            ans_q = random.choice(stMsgs)
            speak(ans_q)  
            ans_take_from_user_how_are_you = takeCommand()


        elif "open my studio" in query or "youtube studio" in query:
            speak("opening youtube studio")
            webbrowser.open("https://studio.youtube.com/channel/UCNcVMyq5JyZ5V_TXN6KUgbA")

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")


        elif "video from laptop" in query or "play videos" in query:
            speak("ok playing music")
            video_dir = "./video"
            videos = os.listdir(video_dir)
            os.startfile(os.path.join(video_dir, videos[0]))


        elif "play dance monkey" in query:
            speak("okay, playing dance monkey from the artist tones and i")
            webbrowser.open("https://open.spotify.com/track/2XU0oxnq2qxCpomAAuJY8K?si=hqT3uLOtQnmV9glVfKP84g")


        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            assname = takeCommand()
            speak("Thanks for naming me")

        elif "write a note" in query:

            speak("What should i write, sir")
            note = takeCommand()
            file = open('anil.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("anil.txt", "r")
            print(file.read())
            speak(file.read(6))
        
        
        
        elif 'joke' in query:
            speak(pyjokes.get_joke())


        elif "calculate" in query:
			
            app_id = "Wolframalpha api id"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)
