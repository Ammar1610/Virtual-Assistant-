def virtual_assistant():

    import speech_recognition as sr
    import pyttsx3
    import pywhatkit
    import datetime
    import wikipedia
    import subprocess

    listener = sr.Recognizer()
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)


    def talk(text):
        engine.say(text)
        engine.runAndWait()


    def take_command():
        try:
            with sr.Microphone() as source:
                print('listening...')
                talk("listening")
                command=''
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
                if 'alexa' in command:
                    command = command.replace('alexa', '')
                    print(command)
        except:
            pass
        return command


    def run_alexa():
        command = take_command()
        print(command)
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
        elif 'who is' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        elif 'open chrome' in command:
            chrome=command.replace('open chrome','')
            task=subprocess.Popen('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe')
            talk("chrome opened")
        elif 'write' in command:
             notes=command.replace('notes','')
             talk('taking notes')
             a=open("C:\\Users\\Lenovo\\Documents\\Virtual Assistant\\Notes.txt",'a')
             a.write(notes)
             a.close()    
   
        else:
          talk('Please say the command again.')


    
    run_alexa()
    