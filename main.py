import stt
import tts
import util
import os
import agent
import llm


total_time = []

def main():
    total_time.append(util.report_time("Inicio: "))
    # Definir y crear el directorio temporal
    tmp_dir = os.path.join(os.getcwd(), 'tmp')
    os.makedirs(tmp_dir, exist_ok=True)
    

    total_time.append(util.report_time("Carpeta tmp creada: "))
    # Grabar audio y convertir a texto

    while True:

        audio_file_path = stt.record_audio_to_file()

        total_time.append(util.report_time("Grabacion de voz del usuario: "))


        text = stt.speech_to_text(audio_file_path)
        
        total_time.append(util.report_time("Procesado de voz a audio: "))     
        # Limpiar archivos WAV temporales
        util.clean_wav_files(tmp_dir)
        

        # response = agent.agent_response(text)
        response = llm.model_response(text)
        total_time.append(util.report_time("Respuesta del modelo: "))  

        if (response is not None) and response != "exit":
            
            # Convertir el texto a voz
            tts.text_to_speech(response)
        if response == "exit":
            response = "¡Ha sido un placer, hablar contigo! Espero verte en otra ocasión"
             # Convertir el texto a voz
            tts.text_to_speech(response)
            break
        else:
            print("No se pudo reconocer el texto.")
        total_time.append(util.report_time("Respuesta del modelo por speech: "))         

    print("Tiempo total de ejecucion: ", sum(total_time))
if __name__ == "__main__":
    main()