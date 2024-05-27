import moviepy.editor as mp
import speech_recognition as sr
from pydub import AudioSegment

def transcribe_audio(file_path):
    recognizer = sr.Recognizer()
    audio = AudioSegment.from_wav(file_path)
    
    # Diviser l'audio en segments de 60 secondes
    segment_length = 60 * 1000  # 60 secondes en millisecondes
    segments = [audio[i:i + segment_length] for i in range(0, len(audio), segment_length)]
    
    transcription = ""
    
    for i, segment in enumerate(segments):
        segment_path = f"segment_{i}.wav"
        segment.export(segment_path, format="wav")
        
        with sr.AudioFile(segment_path) as source:
            audio_data = recognizer.record(source)
            try:
                text = recognizer.recognize_google(audio_data, language='fr-FR')
                transcription += text + " "
            except sr.UnknownValueError:
                print(f"La reconnaissance vocale n'a pas compris l'audio du segment {i}")
            except sr.RequestError as e:
                print(f"Erreur lors de la requête à l'API de reconnaissance vocale pour le segment {i} : {e}")
                break
    
    return transcription

# Charger la vidéo
video = mp.VideoFileClip("introduction.mp4")  # Remplacez "votre_video.mp4" par le chemin de votre fichier vidéo

# Extraire l'audio et le sauvegarder en tant que fichier WAV
audio_path = "extracted_audio.wav"
video.audio.write_audiofile(audio_path)

# Transcrire l'audio
transcription = transcribe_audio(audio_path)
print("Texte transcrit :")
print(transcription)

# Enregistrer le texte transcrit dans un fichier texte
with open("transcription.txt", "w", encoding="utf-8") as file:
    file.write(transcription)
print("La transcription a été enregistrée dans le fichier 'transcription.txt'")
