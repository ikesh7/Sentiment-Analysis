import tkinter as tk
from tkinter import messagebox
from textblob import TextBlob

def analyze_sentiment():
    text = entry_text.get("1.0", tk.END).strip()
    if not text:
        messagebox.showerror("Error", "Please enter some text to analyze.")
        return
    
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    
    if sentiment_score > 0:
        sentiment = "Positive 😊"
    elif sentiment_score < 0:
        sentiment = "Negative 😞"
    else:
        sentiment = "Neutral 😐"
    
    label_result.config(text=f"Sentiment: {sentiment}")

# GUI Setup
root = tk.Tk()
root.title("Sentiment Analysis Tool")
root.geometry("400x300")

tk.Label(root, text="Enter Text for Sentiment Analysis:").pack(pady=5)
entry_text = tk.Text(root, height=5, width=40)
entry_text.pack()

tk.Button(root, text="Analyze Sentiment", command=analyze_sentiment).pack(pady=10)
label_result = tk.Label(root, text="Sentiment: ")
label_result.pack()

root.mainloop()
