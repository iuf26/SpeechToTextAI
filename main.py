import speech_recognition as sr

def main():
    r = sr.Recognizer()
    # with sr.Microphone() as source:
    #     r.adjust_for_ambient_noise(source)
    #
    #     print("Say something...")
    #     audio = r.listen(source)
    #
    #     try:
    #         print('You have said : \n' + r.recognize_google(audio))
    #
    #     except Exception as e:
    #         print("Error" + str(e))
    filename = './dataset1/1272-141231-0000.flac'
    with sr.AudioFile(filename) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text = r.recognize_google(audio_data)
        print(text)
if __name__ == "__main__":
    main()