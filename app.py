# Entry point: integrates stt, llm, tts, and logger
import time
from utils import stt, llm, tts, metrics_logger
from utils.record_audio import record_audio

def run_session():
    session_id = 'session_001'
    print("🎙️ Voice Agent is running. Say 'exit' to stop.\n")

    while True:
        record_audio("sample.wav", duration=5)
        audio_file = "sample.wav"

        # Speech to Text
        start = time.time()
        text = stt.transcribe(audio_file).strip()
        eou = time.time() - start

        print(f"🗣️ User said: {text}")

        # Exit condition
        if text.lower() in ["exit", "stop", "quit"]:
            print("👋 Exiting session.")
            break

        # Handle empty transcription (to avoid LLM error)
        if not text:
            print("⚠️ Didn't catch that. Please try speaking more clearly.\n")
            continue

        # LLM Response
        start = time.time()
        reply = llm.generate_response(text)
        ttft = time.time() - start

        # Text to Speech
        start = time.time()
        tts_output = tts.speak(reply)
        ttfb = time.time() - start

        # Metrics
        total_latency = eou + ttft + ttfb
        metrics_logger.log_metrics(eou, ttft, ttfb, total_latency, session_id)

        print(f"🤖 Agent said: {reply}")
        print(f"🔊 Audio File: {tts_output}")
        print("-" * 50)

if __name__ == "__main__":
    run_session()
