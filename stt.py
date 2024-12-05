import tempfile
import azure.cognitiveservices.speech as speechsdk
import os
import sounddevice as sd
import soundfile as sf
import tempfile
import os
import time
import uuid
from scipy.io.wavfile import write
import numpy as np
import webrtcvad

def speech_to_text(audio_file_path):
    # Load environment variables
    api_key = os.getenv('api_key')
    region = os.getenv('region')

    # Set up the speech configuration
    speech_config = speechsdk.SpeechConfig(subscription=api_key, region=region)
    speech_config.speech_recognition_language="es-MX"
    audio_config = speechsdk.audio.AudioConfig(filename=audio_file_path)

    # Create a speech recognizer
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    # Recognize speech from the audio file
    result = speech_recognizer.recognize_once_async().get()

    # Check the result
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        return result.text
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized.")
    else:
        print(f"Speech Recognition canceled: {result.cancellation_details.error_details}")

    return None



def record_audio_to_file():
    # Asegurar que el directorio 'tmp/' existe
    tmp_dir = 'tmp'
    if not os.path.exists(tmp_dir):
        os.makedirs(tmp_dir)

    # Generar un nombre de archivo único
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"{timestamp}.wav"
    filepath = os.path.join(tmp_dir, filename)

    # Parámetros de grabación
    fs = 16000  # Frecuencia de muestreo compatible con webrtcvad
    channels = 1
    device = None
    silence_duration = 2  # Duración de silencio para detener la grabación (en segundos)
    frame_duration = 30  # Duración de cada frame en ms (10, 20 o 30 ms)
    vad = webrtcvad.Vad(1)  # Nivel de agresividad del VAD (0-3)
    recording = []
    silence_frames = 0
    max_silence_frames = int(silence_duration * 1000 / frame_duration)

    try:
        print("Escuchando microfono...")
        with sd.RawInputStream(samplerate=fs,
                               blocksize=0,  # Dejar que la API determine el tamaño del bloque
                               channels=channels,
                               dtype='int16',
                               device=device) as stream:
            while True:
                # Leer un frame de audio
                
                frames_per_chunk = int(fs * frame_duration / 1000)
                frame, overflowed = stream.read(frames_per_chunk)

                # Verificar si el frame contiene voz
                is_speech = vad.is_speech(frame, fs)

                if not is_speech:
                    silence_frames += 1
                else:
                    silence_frames = 0

                # Convertir el frame a numpy array y agregarlo a la grabación
                frames_array = np.frombuffer(frame, dtype='int16')
                recording.append(frames_array)

                if silence_frames >= max_silence_frames:
                    print("Silencio detectado. Deteniendo la grabación.")
                    break

    except KeyboardInterrupt:
        print("Grabación detenida por el usuario.")

    # Convertir la lista de frames en un arreglo numpy
    if recording:
        recording = np.concatenate(recording, axis=0)
    else:
        recording = np.array([], dtype='int16')

    # Guardar como archivo WAV
    write(filepath, fs, recording)

    return filepath  # Devolver la ruta completa al archivo guardado
