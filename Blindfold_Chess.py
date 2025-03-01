import speech_recognition as sr
import pyttsx3
import chess
import chess.engine

# Initialize speech recognition and text-to-speech
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    with sr.Microphone() as source:
        speak("Your move.")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "Could not understand"
    except sr.RequestError:
        return "Speech service error"

def main():
    board = chess.Board()
    while not board.is_game_over():
        move = recognize_speech()
        if move.lower() == "quit":
            speak("Game over.")
            break
        try:
            board.push_san(move)
            speak(f"Move {move} played.")
        except ValueError:
            speak("Invalid move, try again.")
    speak("Game finished.")

if __name__ == "__main__":
    main()
