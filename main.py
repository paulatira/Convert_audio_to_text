"""Program realizat de Tira Paula-Florentina in cadrul laboratorului Limbaje de Programare 2
 Am folosit cod de aici: https://www.thepythoncode.com/article/using-speech-recognition-to-convert-speech-to-text-python
 si de aici: https://likegeeks.com/python-gui-examples-tkinter-tutorial/"""

from tkinter import *

try:  # tratarea erorii generate daca nu s-a instalat modulul SpeechRecognition
    import speech_recognition as sr
except ModuleNotFoundError:
    print("Nu ati instalat modulul SpeechRecognition!")
filename = "audio.wav"
r = sr.Recognizer()   # initializare recunoastere


def afisare_din_document():
    """Functie pentru convertirea semnalului audio dintr-un fisier audio in text"""
    # deschidere fisier
    try:
        with sr.AudioFile(filename) as source1:
            # incarcare audio din memorie
            audio_data1 = r.record(source1)
            # converteste din audio in text
            text1 = r.recognize_google(audio_data1, language="ro-RO")
            print(text1)
    except FileNotFoundError:
        print("Documentul pe care doriti sa-l deschideti nu a fost gasit")


def afisare_de_la_microfon():
    """Functie pentru convertirea semnalului audio de la microfon in text"""
    try:
        # asculta de la microfon
        with sr.Microphone() as source2:
            # asculta audio de la microfonul prestabilit
            print("Cate secunde doresti sa vorbesti?")
            try:
                sec = int(input("Introdu secundele:"))
                if sec < 0:
                    raise ValueError
            except ValueError:
                while sec < 0:
                    print("Trebuie sa introduci un numar mai mare decat 0!")
                    sec = int(input("Introdu secundele:"))
            print("Spune ceva in limba roamana:")
            audio_data2 = r.record(source2, duration=sec)
            print("Convertire...")
            # converteste din audio in text
            text2 = r.recognize_google(audio_data2, language="ro-RO")  # Vorbeste in limba romana
            print("Ai spus:", text2)
    except sr.UnknownValueError:
        print("Nu ai rostit nimic!")


# Se creeaza o fereastra noua
window = Tk()
window.title("Vorbeste cu mine!")  # Titlul ferestrei
window.geometry('1400x700')  # Dimensiunea ferestrei
# pentru fisier audio
lbl = Label(window, text="Redare text de pe un fisier audio", font=("Arial Bold", 30))
lbl.grid(column=1, row=1)
lbl1 = Label(window, text="Introdu numele documentului audio pe care doresti sa-l deschizi(+extensie)", font=("Arial Bold", 15))
lbl1.grid(column=1, row=2)
txt = Entry(window, width=50)
txt.grid(column=2, row=2)
lbl2 = Label(window, text="Daca vrei sa afisezi textul de pe documentul audio apasa aici:", font=("Arial Bold", 15))
lbl2.grid(column=1, row=3)


def clicked():  # definim functia butonului
    filename1 = txt.get()
    with sr.AudioFile(filename1) as source1:
        # incarcare audio din memorie
        audio_data1 = r.record(source1)
        # converteste din audio in text
        text1 = r.recognize_google(audio_data1, language="ro-RO")
        lbl2 = Label(window, text=text1)
        lbl2.grid(column=2, row=4)


btn = Button(window, text="aici", command=clicked)
btn.grid(column=2, row=3)
lbl3 = Label(window, text="Textul extras din document este:", font=("Arial Bold", 15))
lbl3.grid(column=1, row=4)

# pentru microfon
lbl4 = Label(window, text="Redare text de la microfon", font=("Arial Bold", 30))
lbl4.grid(column=1, row=5)
lbl5 = Label(window, text="Cate secunde doresti sa vorbesti?", font=("Arial Bold", 15))
lbl5.grid(column=1, row=6)
txt1 = Entry(window, width=50)
txt1.grid(column=2, row=6)
lbl6 = Label(window, text="Play record: (Asteapta in jur de 3 secunde pana sa incepi sa vorbesti)", font=("Arial Bold", 15))
lbl6.grid(column=1, row=7)


def clicked1():  # definim functia butonului1

    # asculta de la microfon
    with sr.Microphone() as source2:
        # asculta audio de la microfonul prestabilit
        sec = int(txt1.get())
        audio_data2 = r.record(source2, duration=sec)
        # converteste din audio in text
        text2 = r.recognize_google(audio_data2, language="ro-RO")  # Vorbeste in limba romana
        lbl7 = Label(window, text=text2)
        lbl7.grid(column=2, row=10)


btn1 = Button(window, text="play", command=clicked1)
btn1.grid(column=2, row=7)
lbl6 = Label(window, text="Ai spus:", font=("Arial Bold", 15))
lbl6.grid(column=1, row=10)
window.mainloop()  # bucla infinita, pentru a sta deschisa fereastra cat timp vrem noi
