import stt
import tts
import util
import os
import agent

def main():
    # Definir y crear el directorio temporal
    tmp_dir = os.path.join(os.getcwd(), 'tmp')
    print(tmp_dir)
    os.makedirs(tmp_dir, exist_ok=True)
    
    # Grabar audio y convertir a texto

    while True:

        audio_file_path = stt.record_audio_to_file()
        text = stt.speech_to_text(audio_file_path)
        
        
        # Limpiar archivos WAV temporales
        util.clean_wav_files(tmp_dir)
        
        response = agent.agent_response(text)

        if response is not None:
            print("Texto reconocido:", response)
            
            # Convertir el texto a voz
            tts.text_to_speech(response)
        else:
                print("No se pudo reconocer el texto.")
                

if __name__ == "__main__":
    main()