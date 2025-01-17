# Video Transcript

Video Transcript est un projet Python qui permet d'extraire l'audio d'une vidéo, de transcrire cet audio en texte et de sauvegarder la transcription dans un fichier texte. Ce projet utilise les bibliothèques `moviepy`, `pydub` et `SpeechRecognition` pour accomplir cette tâche.

## Fonctionnalités

- Extraction de l'audio d'une vidéo
- Division de l'audio en segments de 60 secondes pour une meilleure gestion des requêtes API
- Transcription de l'audio en texte en utilisant l'API de Google Speech Recognition
- Sauvegarde de la transcription dans un fichier texte lisible

## Prérequis

Avant de commencer, assurez-vous d'avoir installé les éléments suivants :

- Python 3.x
- `ffmpeg` (doit être accessible via la ligne de commande)

## Installation

1. Clonez le dépôt GitHub :

    ```sh
    git clone https://github.com/votre-utilisateur/video-transcript.git
    cd video-transcript
    ```

2. Installez les dépendances Python :

    ```sh
    pip install moviepy SpeechRecognition pydub
    ```

3. Téléchargez et installez `ffmpeg` :

    - Téléchargez la version appropriée pour votre système depuis [ffmpeg.org](https://ffmpeg.org/download.html).
    - Extrayez l'archive et ajoutez le chemin du dossier `bin` à votre variable d'environnement `PATH`.

## Utilisation

1. Placez votre fichier vidéo dans le répertoire du projet ou spécifiez le chemin complet vers le fichier vidéo dans le script.

2. Modifiez le script `transcription.py` pour pointer vers votre fichier vidéo :

    ```python
    video = mp.VideoFileClip("votre_video.mp4")  # Remplacez "votre_video.mp4" par le chemin de votre fichier vidéo
    ```

3. Exécutez le script :

    ```sh
    python transcription.py
    ```

4. La transcription sera sauvegardée dans un fichier texte nommé `transcription.txt` dans le même répertoire.

## Exemple de script

```python
import moviepy.editor as mp
import speech_recognition as sr
from pydub import AudioSegment

def transcribe_audio(file_path):
    recognizer = sr.Recognizer()
    audio = AudioSegment.from_wav(file_path)
    
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
video = mp.VideoFileClip("votre_video.mp4")  # Remplacez "votre_video.mp4" par le chemin de votre fichier vidéo

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
```
# Contributions
Les contributions sont les bienvenues ! Veuillez soumettre une pull request ou ouvrir une issue pour discuter de vos modifications.

# Licence
Ce projet est sous licence MIT.

# Remerciements
- **moviepy** pour l'extraction et la manipulation vidéo
- **pydub** pour le traitement audio
- **SpeechRecognition** pour la reconnaissance vocale

Pour toute question ou suggestion, n'hésitez pas à me contacter
