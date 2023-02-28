import heapq
import tkinter as tk

def find_top_sentence(text):
    # Split text into sentences
    sentences = text.split('. ')

    # Calculate the score of each sentence
    scores = {key:value}
    for sentence in sentences:
        words = sentence.split()
        score = sum(len(word) for word in words)
        scores[sentence] = score

    # Find the top sentence
    top_sentence = heapq.nlargest(1, scores, key=scores.get)[0]

    return top_sentence

def on_submit():
    text = text_box.get("1.0", "end-1c")
    top_sentence = find_top_sentence(text)
    output_label.configure(text=top_sentence)

# Create the GUI
root = tk.Tk()
root.title("Top Sentence Finder")

# Create the text box and submit button
text_box = tk.Text(root, height=10, width=50)
text_box.pack()
submit_button = tk.Button(root, text="Find Top Sentence", command=on_submit)
submit_button.pack()

# Create the output label
output_label = tk.Label(root, text="")
output_label.pack()

root.mainloop()
