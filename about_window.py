import tkinter as tk

# Создаем окно
about_window = tk.Tk()
about_window.title("Goncharenko Security Anti-Virus — О программе")
about_window.geometry("600x350")

# Устанавливаем параметры
about_window.resizable(width=False, height=False)
screen_width = about_window.winfo_screenwidth()
screen_height = about_window.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (600 / 2))
y_coordinate = int((screen_height / 2) - (350 / 2))
about_window.geometry(f"600x350+{x_coordinate}+{y_coordinate}")
icon = tk.PhotoImage(file="icon.png")
about_window.iconphoto(True, icon)

# Добавляем текст
text1 = tk.Label(about_window, text="Goncharenko⠀⠀⠀⠀ \nSecurity Anti-Virus", bg="#ebebeb", font=("Ruberoid Bold", 19))
text1.place(x=105, y=25)

text2 = tk.Label(about_window, text="Goncharenko Anti-Virus - это программа, разработанная на языке\nпрограммирования Python, которая обеспечивает защиту\nкомпьютера от вредоносных программ. Она осуществляет\nпроверку запущенных процессов и файлов на наличие вирусов.", font=("Ruberoid Medium", 11), bg="#ebebeb", justify="left")
text2.place(x=30, y=120)

text3 = tk.Label(about_window, text="Язык: Русский\nВерсия: v0.2\n\nSecurity Software © Goncharenko Anti-Virus 2023" , font=("Ruberoid Medium", 11), bg="#ebebeb", justify="left")
text3.place(x=30, y=220)

image = tk.PhotoImage(file="shieldsmall.png")
image_label = tk.Label(about_window, image=image, bg="#ebebeb", highlightthickness=0)
image_label.place(x=25, y=30)

# Добавляем кнопку
ok_button = tk.Button(about_window, text="ОК", width=10, bd=1, command=about_window.destroy)
ok_button.place(x=500, y=300)
ok_button.config(cursor="hand2")

# Меняем параметры окна
about_window.configure(bg="#ebebeb")

about_window.mainloop()