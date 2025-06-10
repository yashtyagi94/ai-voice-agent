import whisper
model = whisper.load_model('base')

def transcribe(audio_path):
    result = model.transcribe(audio_path, language='en')
    return result['text']
