import tkinter as tk


def calculate():
    result = ""
    height = float(input1.get()) / 100
    weight = float(input2.get())
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        result = f"недостаток веса: {bmi}"
    elif 18.5 < bmi < 25:
        result = f"норма веса: {bmi}"
    elif 25 < bmi < 30:
        result = f"выше среднего вес: {bmi}"
    else:
        result = f"Ожирение: {bmi}"
    result_label.config(text=result)


root = tk.Tk()
root.title("STEP IT")
root.geometry("300x200")

label1 =  tk.Label(root, text="Введите свой рост")
input1 = tk.Entry(root)
label1.pack()
input1.pack()

label2 = tk.Label(root, text="Введите свой вес")
label2.pack()
input2 = tk.Entry(root)
input2.pack()

button = tk.Button(root, text="Вычислить", command=calculate)
button.pack(pady=10)

result_label = tk.Label(root)
result_label.pack()

root.mainloop()
