# importing all packages
import speech_recognition as sr
import subprocess
import webbrowser
import pyttsx3

# creating a class 
class VoiceSearch:
    
    # function initializing all the voice recognition
    def listenSource(self):
        # initializing text to speech engine
        engine = pyttsx3.init()
        # initializing text to speech speed
        engine.setProperty("rate", 150)
        # initializing speech recognition
        r = sr.Recognizer()
        # initializing speech recognition mic
        mic = sr.Microphone()
        MyText = ''
        flag = 0
        # till no proper response is got keep on asking for command
        # you can modify this part to your liking !
        while flag == 0:
            with mic as source:
                try:   
                    # Voice recognition part
                    engine.say('  Listening to Command')
                    engine.runAndWait()  
                    # adjusting ambient noise 
                    r.adjust_for_ambient_noise(source) 
                    # listening for 15 seconds
                    # you can increase this length
                    audio = r.listen(source,timeout = 15)
                    # google api giving the recognized words
                    MyText = r.recognize_google(audio)
                    engine.say('Command Recorded' + MyText)
                    engine.runAndWait()
                    print('Command Recorded' + MyText)                    
                    flag = 1 
                except sr.UnknownValueError:
                    engine.say('Unknown Command')
                    engine.runAndWait()
                    MyText = 'Unknown Command'
                
        return MyText.lower()
                    
    # function to create task based on words received
    def voiceSearch(self):
        MyText = self.listenSource()
        print("Command given: " + MyText)
        # initializing the chrome path
        chromedir= 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        
        # for windows search
        if MyText == 'windows search':
            query_string = self.listenSource()
            if query_string == 'Unknown Command':
                print('Cannot perform search as Command was unknown')
            else:
                # will search for all files in C drive
                local_path = r"C:"
                subprocess.Popen(f'explorer /root,"search-ms:query={query_string}&crumb=folder:{local_path}&"')
        # for google search                
        elif MyText == 'google search':
            search_term = self.listenSource()
            if search_term == 'Unknown Command':
                print('Cannot perform search as Command was unknown')
            else:
                # setting the search to google and opening the chrome browser
                url = "https://www.google.com.tr/search?q={}".format(search_term)
                webbrowser.get(chromedir).open(url) 