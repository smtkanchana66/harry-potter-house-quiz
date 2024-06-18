import tkinter as tk
from tkinter import messagebox

# Initialize points for each house
G = 0
R = 0
S = 0
H = 0

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

    for widget in window.winfo_children():
        widget.destroy()
    
    q1_var.set(0)
    question_label = tk.Label(window, text="Q1) Do you like Dawn or Dusk?", font=("Helvetica", 14))
    question_label.pack(pady=10)
    tk.Radiobutton(window, text="1) Dawn", variable=q1_var, value=1, font=("Helvetica", 12)).pack(anchor=tk.W)
    tk.Radiobutton(window, text="2) Dusk", variable=q1_var, value=2, font=("Helvetica", 12)).pack(anchor=tk.W)
    submit_button = tk.Button(window, text="Submit", command=submit_q1, font=("Helvetica", 12))
    submit_button.pack(pady=20)

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

    for widget in window.winfo_children():
        widget.destroy()

    q2_var.set(0)
    question_label = tk.Label(window, text="Q2) When I’m dead, I want people to remember me as:", font=("Helvetica", 14))
    question_label.pack(pady=10)
    tk.Radiobutton(window, text="1) The Good", variable=q2_var, value=1, font=("Helvetica", 12)).pack(anchor=tk.W)
    tk.Radiobutton(window, text="2) The Great", variable=q2_var, value=2, font=("Helvetica", 12)).pack(anchor=tk.W)
    tk.Radiobutton(window, text="3) The Wise", variable=q2_var, value=3, font=("Helvetica", 12)).pack(anchor=tk.W)
    tk.Radiobutton(window, text="4) The Bold", variable=q2_var, value=4, font=("Helvetica", 12)).pack(anchor=tk.W)
    submit_button = tk.Button(window, text="Submit", command=submit_q2, font=("Helvetica", 12))
    submit_button.pack(pady=20)

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

    for widget in window.winfo_children():
        widget.destroy()

    q3_var.set(0)
    question_label = tk.Label(window, text="Q3) Which kind of instrument most pleases your ear?", font=("Helvetica", 14))
    question_label.pack(pady=10)
    tk.Radiobutton(window, text="1) The violin", variable=q3_var, value=1, font=("Helvetica", 12)).pack(anchor=tk.W)
    tk.Radiobutton(window, text="2) The trumpet", variable=q3_var, value=2, font=("Helvetica", 12)).pack(anchor=tk.W)
    tk.Radiobutton(window, text="3) The piano", variable=q3_var, value=3, font=("Helvetica", 12)).pack(anchor=tk.W)
    tk.Radiobutton(window, text="4) The drum", variable=q3_var, value=4, font=("Helvetica", 12)).pack(anchor=tk.W)
    submit_button = tk.Button(window, text="Submit", command=submit_q3, font=("Helvetica", 12))
    submit_button.pack(pady=20)

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
