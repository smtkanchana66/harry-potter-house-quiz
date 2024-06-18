# Harry Potter House Quiz
This is a Python-based GUI application that sorts users into one of the four Hogwarts houses: Gryffindor, Hufflepuff, Ravenclaw, or Slytherin based on their answers to a few questions. The application uses the Tkinter library to create the user interface.
## Features
- <b> Interactive Quiz: </b> Users answer three questions to determine their Hogwarts house.
- <b> Graphical User Interface: </b> Simple and clean interface built with Tkinter.
- <b> Harry Potter Theme: </b> Questions and results are themed around the Harry Potter universe.
## Installation
1.Clone the repository:
```sh
git clone https://github.com/yourusername/harry-potter-house-quiz.git
```
2.Navigate to the project directory:
```sh
cd harry-potter-house-quiz
```
3.Install the required dependencies:
```sh
pip install tk
```
## Usage
1. Run the application:
```sh
python quiz.py
```
2. Run the application: <br>
3. Get your house: After completing the quiz, the application will display your Hogwarts house.<br>
## Code Explanation
The main logic is in the `quiz.py` file. Here's a breakdown of the key parts:
- Initialization:
```python
  import tkinter as tk
from tkinter import messagebox

# Initialize points for each house
G = 0
R = 0
S = 0
H = 0
```
- Question 1:
```python
def question1():
    def submit_q1():
        global G, R, S, H
        q1_answer = q1_var.get()
        if q1_answer == 1:
            G += 1
            R += 1
        elif q1_answer == 2:
            H += 1
            S += 1
        else:
            messagebox.showerror("Error", "Wrong input.")
            return
        question2()
    # Rest of the code to display the question
```
- Question 2:
```python
def question2():
    def submit_q2():
        global G, R, S, H
        q2_answer = q2_var.get()
        if q2_answer == 1:
            H += 2
        elif q2_answer == 2:
            S += 2
        elif q2_answer == 3:
            R += 2
        elif q2_answer == 4:
            G += 2
        else:
            messagebox.showerror("Error", "Wrong input.")
            return
        question3()
    # Rest of the code to display the question
```
- Question 3:
```python
def question3():
    def submit_q3():
        global G, R, S, H
        q3_answer = q3_var.get()
        if q3_answer == 1:
            S += 4
        elif q3_answer == 2:
            H += 4
        elif q3_answer == 3:
            R += 4
        elif q3_answer == 4:
            G += 4
        else:
            messagebox.showerror("Error", "Wrong input.")
            return
        display_result()
    # Rest of the code to display the question
```
- Display Result:
```python
def display_result():
    for widget in window.winfo_children():
        widget.destroy()

    result = ""
    if S > H and S > R and S > G:
        result = "Slytherin"
    elif H > S and H > R and H > G:
        result = "Hufflepuff"
    elif R > S and R > H and R > G:
        result = "Ravenclaw"
    elif G > S and G > H and G > R:
        result = "Gryffindor"
    else:
        result = "Tie"

    result_label = tk.Label(window, text=f"You belong to {result}!", font=("Helvetica", 16))
    result_label.pack(pady=20)

    restart_button = tk.Button(window, text="Restart Quiz", command=start_quiz, font=("Helvetica", 12))
    restart_button.pack(pady=20)
```
- Start Quiz:
```python
def start_quiz():
    global G, R, S, H
    G = 0
    R = 0
    S = 0
    H = 0
    question1()

window = tk.Tk()
window.title("Harry Potter House Quiz")
window.geometry("500x400")

q1_var = tk.IntVar()
q2_var = tk.IntVar()
q3_var = tk.IntVar()

start_quiz()
window.mainloop()
```
## Inspiration
This project was inspired by a coding exercise from <a href="https://www.codedex.io/home">Codex.io</a>, an online platform for learning Python. It provides a practical example of how to create interactive applications using Python.
<!-- ## License
This project is licensed under the MIT License.


