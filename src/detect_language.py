from langdetect import detect

def detect_lan(sentence : str):
    lan = detect(sentence)

    return lan