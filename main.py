from BrailleToKorean import BrailleToKorean
from RecognizeBraille import logic
from TTS import tts

if __name__ == "__main__":
    if BrailleToKorean(logic()).translate():
        tts("해석할 수 없는 점자입니다")
    else:
        tts(BrailleToKorean(logic()).translate())
