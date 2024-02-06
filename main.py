from random import randint
import speech_recognition as sr
import os 

r = sr.Recognizer()

def getTextFromUser():
    with sr.Microphone() as source:
        text = None
        while not text:
            # getting audio data from the default microphone
            audio_data = r.record(source, duration=2)
            try:
                # convert speech to text
                text = r.recognize_google(audio_data)
            except:
                print("Can't Recognise Word!! Try again or Speak END to stop...")
    return text

def printBill():
    sum = 0
    print(f"===============================================")
    print(f"\tNAME: {name}\t")
    print(f"===============================================")
    print(f"\tPRODUCT\t\t\tPRICE")
    print(f"===============================================")
    for productName in products:
        price = menu[productName]
        sum+=price
        print(f"\t{productName}\t\t\t{price}")
    print(f"===============================================")
    print(f"\tTOTAL:\t\t\t{sum}")
    print(f"===============================================")

if __name__ == '__main__':
    menu = {
        "Dosa": 13.33,
        "Apple": 20.00,
        "Orange": 20.00,
        "Biriyani": 100.00
    }
    products = []

    print("Recognizing...")
    print("Tell me your name: ")
    name = getTextFromUser()
    print(name)

    product = "hello"
    while product.lower() != "end":
        print("\nRecognizing...")
        print("Product Name (Speak END to stop): ")
        product = getTextFromUser().capitalize()
        if product in menu:
            print(product)
            products.append(product)
        else:
            print("Product not it Menu. Try Again... ")

    printBill()
