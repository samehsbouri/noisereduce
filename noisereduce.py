import noisereduce as nr
from scipy.io import wavfile
import tkinter.filedialog
import os
from alive_progress import alive_bar
import time
from scipy.io.wavfile import write
import sounddevice
from playsound import playsound




desktop = os.path.normpath(os.path.expanduser("~/Desktop"))
#size terminal
width = os.get_terminal_size().columns


print("###########################################".center(width))
print("Bienvenu".center(width))
print("1) ouvrir un fichier wav")
print("2) enregistrer un vocal")
print("###########################################".center(width))
while True:
    x = int(input("donner votre choix:\n"))
    if x < 1 or x > 2:
        print("essayer une autre fois\n")
    break
print("###########################################".center(width))
if x == 1:
    file_path = tkinter.filedialog.askopenfilename()
    print('En cours de traitement\n')
    with alive_bar(100) as bar:
        for i in range(100):
            time.sleep(0.001)
            bar()      
    rate, data = wavfile.read(file_path)
    reduced_noise = nr.reduce_noise(y=data, sr=rate)
    wavfile.write("/home/sameh/Desktop/result.wav", rate, reduced_noise)
    print("Fichier sauvgardée dans le Desktop\n")
    print("###########################################".center(width))
    z = input("voulez vous ecoutez le resultat? Oui / Non\n")
    if z == "oui":
        playsound("/home/sameh/Desktop/result.wav")
else:
    fps = 44100
    duration = int(input("Saisir la durée d enregistrement: \n"))
    print("Recording...\n")
    recording = sounddevice.rec(int(duration*fps), samplerate=fps, channels=1)
    sounddevice.wait()
    print("Terminé!\n")
    print("###########################################".center(width))
    write("/home/sameh/Desktop/output.wav", fps, recording)
    k=input("Fichier sauvgardée dans le  Desktop voulez vours ecoutéz le resultat? Oui / Non\n")
    if k=="oui":
        playsound("/home/sameh/Desktop/output.wav")
    print("###########################################".center(width))
    y = input("Voulez Vous supprimer le bruit? Oui / Non?\n")
    if y == 'oui':
        print("Traitement en cours")
        with alive_bar(100) as bar:
            for i in range(100):
                time.sleep(0.001)
                bar()
    rate, data = wavfile.read("/home/sameh/Desktop/output.wav")
    reduced_noise = nr.reduce_noise(y=data, sr=rate)
    wavfile.write("/home/sameh/Desktop/result.wav", rate, reduced_noise)
    print("Fichier sauvgardée dans le  Desktop\n")
    print("###########################################".center(width))
    q = input("Voulez Vous ecoutez le resultat?\n oui / non\n")
    if q == 'oui':
        playsound("/home/sameh/Desktop/result.wav")
    else:
        print('exit')

