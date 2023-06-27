#------------------------------------------- Steps to build a typing speed test game -------------------------------------------#
# Create a function to calculate the error rate
# Create a function to calculate the speed
# Generating sentence paragraph
# GUI Elements
# Start the timer
#------------------------------------------------------------- Code -------------------------------------------------------------#

from wonderwords import RandomSentence
import tkinter as tk
import time


# Create a function to calculate the error rate
def error_rate(sentence_paragraph, typed_paragraph):
    error_count = 0
    length = len(sentence_paragraph)

    for character in range(length):
        try: 
            if sentence_paragraph[character] != typed_paragraph[character]:
                error_count += 1
        except:
            error_count += 1

    error_percent = error_count / length * 100
    return error_percent

# Create a function to calculate the speed
def calculate_speed(event=None):
    typed_paragraph = text_input.get("1.0", "end").strip()
    end_time = time.time()

    time_taken = end_time - start_time

    error_percent = error_rate(sentence_paragraph, typed_paragraph)
    result_text.delete("1.0", "end")

    if error_percent > 50:
        result_text.insert("end", f"Your error rate {error_percent} was quite high and hence your accurate speed could not be computed.")
    else:
        speed = len(typed_paragraph) / time_taken
        result_text.insert("end", "******YOUR SCORE REPORT******\n")
        result_text.insert("end", f"Your speed is {speed} words/sec\n")
        result_text.insert("end", f"The error rate is {error_percent}")


# Generating sentence paragraph
sentence_list = []
sentence_paragraph = ""

for _ in range(5):
    sent = RandomSentence()
    random_sent = sent.sentence()
    sentence_list.append(random_sent)
    sentence_paragraph += random_sent + " "

root = tk.Tk()
root.title("Typing Speed Test")

# GUI Elements
instructions = tk.Label(root, text="Type the below paragraph as quickly as possible with as few mistakes to get a high score:")
instructions.pack()

paragraph_text = tk.Label(root, text=sentence_paragraph, wraplength=400)
paragraph_text.pack()

text_input = tk.Text(root, height=10, width=50)
text_input.pack()

submit_button = tk.Button(root, text="Submit", command=calculate_speed)
submit_button.pack()

result_text = tk.Text(root, height=4, width=50)
result_text.pack()

# Start the timer
start_time = time.time()

root.mainloop()
