import tkinter as tk
from tkinter import messagebox

# Recommendation Data
recommendations = {
    "Technology": [
        "Learn Python",
        "AI & Machine Learning",
        "Web Development",
        "Cyber Security"
    ],
    "Sports": [
        "Football",
        "Cricket",
        "Basketball",
        "Swimming"
    ],
    "Music": [
        "Guitar",
        "Piano",
        "Singing",
        "Music Production"
    ],
    "Travel": [
        "Northern Pakistan",
        "Turkey",
        "Switzerland",
        "Malaysia"
    ],
    "Books": [
        "Atomic Habits",
        "The Alchemist",
        "Rich Dad Poor Dad",
        "Deep Work"
    ]
}


def recommend():
    category = choice.get()

    if category == "":
        messagebox.showwarning("Warning", "Please select a category.")
        return

    result.delete("1.0", tk.END)
    result.insert(tk.END, f"Recommended for {category}:\n\n")

    for item in recommendations[category]:
        result.insert(tk.END, f"• {item}\n")


# GUI Window
root = tk.Tk()
root.title("Simple AI Recommendation System")
root.geometry("500x450")
root.config(bg="#E8F6F3")

title = tk.Label(
    root,
    text="AI Recommendation System",
    font=("Arial", 18, "bold"),
    bg="#E8F6F3"
)
title.pack(pady=10)

tk.Label(
    root,
    text="Select Your Interest",
    font=("Arial", 12),
    bg="#E8F6F3"
).pack()

choice = tk.StringVar()

dropdown = tk.OptionMenu(root, choice, *recommendations.keys())
dropdown.config(width=20)
dropdown.pack(pady=10)

btn = tk.Button(
    root,
    text="Get Recommendation",
    command=recommend,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 11, "bold")
)
btn.pack(pady=10)

result = tk.Text(root, width=45, height=12, font=("Arial", 11))
result.pack(pady=10)

root.mainloop()