from BrailleToKorean import BrailleToKorean
from RecognizeBraille import logic
from TTS import tts

if __name__ == "__main__":
    tts(BrailleToKorean(logic()).translate())