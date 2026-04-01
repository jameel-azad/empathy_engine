import pyttsx3
import argparse
import sys
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def detect_emotion(text):
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(text)
    compound = scores['compound']
    if compound >= 0.05:
        emotion = "positive"
        intensity = min(compound, 1.0)
    elif compound <= -0.05:
        emotion = "negative"
        intensity = min(abs(compound), 1.0)
    else:
        emotion = "neutral"
        intensity = 0.0
    return emotion, intensity

def map_emotion_to_voice(emotion, intensity):
    # Baseline values
    rate_base = 150
    volume_base = 0.8
    
    if emotion == "positive":
        # Rate: 150 to 200, Volume: 0.8 to 1.0
        rate = rate_base + (intensity * 50)
        volume = volume_base + (intensity * 0.2)
    elif emotion == "negative":
        # Rate: 150 down to 100, Volume: 0.8 down to 0.6
        rate = rate_base - (intensity * 50)
        volume = volume_base - (intensity * 0.2)
    else:
        rate = rate_base
        volume = volume_base
    
    # Clamp values to valid ranges
    rate = max(100, min(200, rate))
    volume = max(0.6, min(1.0, volume))
    
    return {"rate": int(rate), "volume": volume}

def synthesize_speech(text, output_file):
    emotion, intensity = detect_emotion(text)
    params = map_emotion_to_voice(emotion, intensity)
    
    engine = pyttsx3.init()
    engine.setProperty('rate', params['rate'])
    engine.setProperty('volume', params['volume'])
    
    engine.save_to_file(text, output_file)
    engine.runAndWait()
    
    print(f"Audio saved to: {output_file}")
    print(f"Detected emotion: {emotion} (intensity: {intensity:.2f})")
    print(f"Voice parameters: rate={params['rate']}, volume={params['volume']:.2f}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Empathy Engine - Emotion-based TTS")
    parser.add_argument("text", nargs="?", help="Text to speak")
    parser.add_argument("-o", "--output", default="output.wav", help="Output audio file (default: output.wav)")
    args = parser.parse_args()
    
    if args.text:
        text = args.text
    else:
        text = input("Enter text to speak: ")
    
    synthesize_speech(text, args.output)