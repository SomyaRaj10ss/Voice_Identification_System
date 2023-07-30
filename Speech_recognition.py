import tkinter as tk
import speech_recognition as sr
import webbrowser

# Create the tkinter application window
app = tk.Tk()
app.title("Speech-to-Text")

# Set the window size and background color
app.geometry("400x300")
app.configure(bg="#f7f7f7")

# Create a label to display recognized text
label = tk.Label(app, text="Say something...", font=("Helvetica", 16), fg="#333333", bg="#f7f7f7")
label.pack(pady=20)

# Initialize the speech recognition engine
r = sr.Recognizer()

# Define a function to listen for speech and display recognized text
def listen_for_speech():
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        label.config(text=text)
    except sr.UnknownValueError:
        label.config(text="Sorry, I didn't catch that.")
    except sr.RequestError:
        label.config(text="Sorry, my speech service is down.")

# Create a button to trigger speech recognition
button = tk.Button(app, text="Listen", font=("Helvetica", 14), bg="#4CAF50", fg="#FFFFFF", command=listen_for_speech)
button.pack(pady=10)

# Add a feature to save the recognized text to a file
def save_text():
    text = label.cget("text")
    if text != "Say something...":
        with open("recognized_text.txt", "a") as f:
            f.write(text + "\n")
            label.config(text="Text saved to file.", fg="#4CAF50")

# Create a button to save the recognized text to a file
save_button = tk.Button(app, text="Save to file", font=("Helvetica", 12), bg="#FFFFFF", fg="#333333", command=save_text)
save_button.pack(pady=5)

# Add a feature to clear the recognized text
def clear_text():
    label.config(text="Say something...", fg="#333333")

# Create a button to clear the recognized text
clear_button = tk.Button(app, text="Clear", font=("Helvetica", 12), bg="#FFFFFF", fg="#333333", command=clear_text)
clear_button.pack(pady=5)

# Add a feature to search the recognized text on the default browser
def search_on_browser():
    text = label.cget("text")
    if text != "Say something...":
        url = "https://www.google.com/search?q=" + text.replace(" ", "+")
        webbrowser.open(url)

# Create a button to search the recognized text on the default browser
search_button = tk.Button(app, text="Search on browser", font=("Helvetica", 12), bg="#FFFFFF", fg="#333333", command=search_on_browser)
search_button.pack(pady=5)

# Run the tkinter event loop
app.mainloop()
