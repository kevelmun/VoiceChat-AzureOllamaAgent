import os
import io
from dotenv import load_dotenv
import simpleaudio as sa
import azure.cognitiveservices.speech as speechsdk
import wave
import time

def play_audio_from_bytes(audio_data):
    # Leer el audio desde bytes usando wave
    with io.BytesIO(audio_data) as audio_io:
        with wave.open(audio_io, 'rb') as wave_read:
            sample_rate = wave_read.getframerate()
            num_channels = wave_read.getnchannels()
            bytes_per_sample = wave_read.getsampwidth()
            audio_frames = wave_read.readframes(wave_read.getnframes())

    # Reproducir usando simpleaudio
    play_obj = sa.play_buffer(
        audio_frames,
        num_channels=num_channels,
        bytes_per_sample=bytes_per_sample,
        sample_rate=sample_rate
    )
    play_obj.wait_done()  # Espera a que termine la reproducción

def text_to_speech(text):
    """Sintetiza el texto dado en voz, lo guarda como archivo WAV y lo reproduce."""
    # Cargar variables de entorno
    load_dotenv()
    
    # Configurar el servicio de síntesis de voz
    speech_config = speechsdk.SpeechConfig(
        subscription=os.getenv('api_key'),
        region=os.getenv('region')
    )
    speech_config.speech_synthesis_voice_name = 'es-MX-JorgeNeural'
    
    # Crear un sintetizador de voz
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
    
    # Realizar la síntesis de voz
    result = speech_synthesizer.speak_text_async(text).get()
    
    # Verificar si la síntesis fue exitosa
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        # Obtener los datos de audio en bytes
        audio_data = result.audio_data
        
        # Guardar los datos de audio en un archivo WAV en la carpeta tmp
        tmp_dir = 'tmp'  # Definir la carpeta tmp
        if not os.path.exists(tmp_dir):
            os.makedirs(tmp_dir)
        
        # Crear un nombre de archivo único utilizando una marca de tiempo
        filename = os.path.join(tmp_dir, f"agent_{int(time.time())}.wav")
        with open(filename, 'wb') as f:
            f.write(audio_data)
        
        print(f"Audio guardado en {filename}")
    else:
        print(f"Error al sintetizar el texto: {result.reason}")
