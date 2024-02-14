import wikipedia
import gtts
import os
import speech_recognition as sr

def getTextFromUser() -> str:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        text = ""
        while text == "":
            # getting audio data from the default microphone
            audio_data = r.record(source, duration=5)
            try:
                # convert speech to text
                text = r.recognize_google_cloud(audio_data)
            except:
                print("Can't Recognise Word!! Try again or Speak END to stop...")
    return text

while True:
    c: str = 'n'
    key: str = ''
    while c.lower() == 'n':
        print("\n\nTell me a Keyword... I'm Listening... ")
        # Getting search keyword from user
        key = getTextFromUser().lower()
        c = input(f"Do you want to search {key.upper()} (y/n): ")

    # Suggestions for search
    results: list[str] = wikipedia.search(key, results=5)
    print("===============================================")
    print("These are the Search Suggestions")
    for i, result in enumerate(results):
        print(f"{i+1}. {result}")
    print("===============================================")

    choice: int = int(input("Select (1-5): "))
    search: str = ""
    try:
        search = results[choice-1]
        result = wikipedia.summary(search, auto_suggest=False, redirect=False, sentences=2)
    except wikipedia.DisambiguationError as e:
        print(f"Multiple options found for {search}. Please choose one:")
        options: list[str] = e.options
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
        userInput: int = int(input("Enter the number of your choice: "))
        search = results[userInput-1]
        result = wikipedia.summary(search, auto_suggest=False, redirect=False, sentences=2)

    print("\n\n" + result) 
    print(f"\nREAD MORE: https://en.wikipedia.org/wiki/{search.replace(' ', '_')}")
    try:
        os.system(f'say -v Samantha "{result}. READ MORE, on the link given here" ')
    except:
        a = gtts.gTTS(result)
        a.save("audio.mp3")
        os.system("afplay audio.mp3")
