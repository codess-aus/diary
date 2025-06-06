import random
import os
from datetime import datetime

def analyze_sentiment(text):
    positive_words = ["happy", "great", "good", "love", "excited", "joy", "wonderful", "amazing", "awesome", "fantastic"]
    negative_words = ["sad", "bad", "angry", "upset", "tired", "worried", "anxious", "terrible", "awful", "hate"]
    text_lower = text.lower()
    pos = sum(word in text_lower for word in positive_words)
    neg = sum(word in text_lower for word in negative_words)
    if pos > neg:
        return "positive"
    elif neg > pos:
        return "negative"
    else:
        return "neutral"

encouragements = {
    "positive": [
        "That's awesome! 😃 Keep shining! ✨",
        "Love your energy! 🌟 Keep it up! 💪",
        "So happy to hear that! 😊 Keep smiling! 😁"
    ],
    "negative": [
        "It's okay to have tough days. 💙 Tomorrow is a new start! 🌅",
        "Sending you a big virtual hug! 🤗 You got this! 💪",
        "Remember, after rain comes sunshine! ☀️ Stay strong! 🌈"
    ],
    "neutral": [
        "Thanks for sharing! 📖 Hope your day gets even better! 😊",
        "Every day is a new page. Keep writing your story! 📝✨",
        "I'm here to listen anytime! 👂💖"
    ]
}

def save_entry(entry):
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"diary_{today}.txt"
    with open(filename, "a", encoding="utf-8") as f:
        timestamp = datetime.now().strftime("%H:%M:%S")
        f.write(f"[{timestamp}] {entry}\n")

def main():
    print("Welcome to your Digital Diary! 📝")
    entry = input("How was your day? Write anything you'd like: \n")
    save_entry(entry)
    sentiment = analyze_sentiment(entry)
    response = random.choice(encouragements[sentiment])
    print(f"\nDiary says: {response}")

if __name__ == "__main__":
    main()
