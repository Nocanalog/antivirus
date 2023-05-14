import requests, subprocess, hashlib, os, time, threading, tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog

# Создаем главное окно
main_window = tk.Tk()
main_window.geometry("800x500")

# Устанавливаем положение главного окна
screen_width = main_window.winfo_screenwidth()
screen_height = main_window.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (800 / 2))
y_coordinate = int((screen_height / 2) - (500 / 2))
main_window.geometry(f"800x500+{x_coordinate}+{y_coordinate}")

def show_load_screen():
    # Создаем загрузочный экран
    load_frame = tk.Frame(main_window, width=800, height=500, bg="#ededed")
    load_frame.pack(side="top", fill="both", expand=True)
    # Устанавливаем надпись на экране загрузки
    load_label = tk.Label(load_frame, text="⠀  Goncharenko Anti-Virus", font=("Ruberoid Bold", 34), bg="#ededed",
                          fg="black", anchor="w", padx=0, pady=0)
    load_label.place(x=115, y=170)
    # Добавляем изображение щита
    image = Image.open("shieldsmall.png")
    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(load_frame, image=photo, bg="#ededed")
    image_label.image = photo
    image_label.place(x=82, y=171)
    # Добавляем надпись "Запуск..."
    load_text = tk.Label(load_frame, text="Запуск...", font=("Ruberoid Medium", 16), bg="#ededed", fg="black")
    load_text.place(x=350, y=280)
    main_window.after(1000, update_load_text, load_text)
    main_window.after(2000, hide_load_screen, load_frame)

def update_load_text(load_text):
    load_text.config(text="Подключение к базам...")
    load_text.place(x=263, y=280)

def hide_load_screen(load_frame):
    # Скрываем загрузочный экран
    load_frame.pack_forget()
    # Отображаем главное окно
    top_frame1.pack(side="top", fill="both", expand=True)
    bottom_frame.pack(side="bottom", fill="both", expand=True)
# Показ загрузочного экрана
show_load_screen()

# Показ главного окна после загрузочного экрана
main_window.deiconify()
main_window.after(0, show_load_screen)

# Создаем области для главного окна
top_frame1 = tk.Frame(main_window, bg="#f7f7f7")
bottom_frame = tk.Frame(main_window, bg="#f7f7f7")

# Делаем программу нерастяжимой
main_window.resizable(False, False)

# Устанавливаем название и иконку главного окна
main_window.title("Goncharenko Security Anti-Virus")
main_window.iconbitmap("icon.ico")

# Создаем и размещаем зеленую область
top_frame = tk.Frame(main_window, width=800, height=220, bg="#38be39")
top_frame.pack(side="top", fill="both", expand=True)

# Меняем курсор при наведении
def on_enter(event):
    item_id = event.widget.find_withtag('current')
    canvas.itemconfig(item_id, fill="#f7f7f7")
    canvas.config(cursor="hand2")
def on_leave(event):
    item_id = event.widget.find_withtag('current')
    canvas.itemconfig(item_id, fill="#ffffff")
    canvas.config(cursor="")

# Создаем серую область
canvas = tk.Canvas(main_window, width=800, height=280, bg="#ebebeb")
canvas.pack(side="bottom", fill="both", expand=True)

# Открываем окно "О программе"
def open_about_window():
    subprocess.Popen(["python", "about_window.py"])

# Добавляем меню
img1 = tk.PhotoImage(file="image1.png")
img2 = tk.PhotoImage(file="image2.png")
img3 = tk.PhotoImage(file="image3.png")
# Положение прямоугольников
x_start = 30
y_start = 25
width = 230
height = 230
padding = 25
# Добавляем прямоугольники меню
rect1 = canvas.create_rectangle(x_start, y_start, x_start + width, y_start + height, fill="#ffffff", outline="")
img1_id = canvas.create_image(x_start + width//2, y_start + height//2.3, image=img1)
rect2 = canvas.create_rectangle(x_start + width + padding, y_start, x_start + 2*width + padding, y_start + height,
                                fill="#ffffff", outline="")
img2_id = canvas.create_image(x_start + width + padding + width//2, y_start + height//2.3, image=img2)
rect3 = canvas.create_rectangle(x_start + 2*(width + padding), y_start, x_start + 3*width + 2*padding,
                                y_start + height, fill="#ffffff", outline="")
img3_id = canvas.create_image(x_start + 2*(width + padding) + width//2, y_start + height//2.3, image=img3)
# Добавляем надписи меню
text1 = canvas.create_text(143, 185, text="⠀⠀ Проверка\nфайлов вручную", fill="black", font=("Ruberoid Semi Bold", 13))
text2 = canvas.create_text(400, 185, text="Настройки", fill="black", font=("Ruberoid Semi Bold", 13))
text3 = canvas.create_text(655, 185, text="О программе", fill="black", font=("Ruberoid Semi Bold", 13))

# Добавляем пункт "Проверка файлов вручную"
def on_rect1_click(event):
    check_window = tk.Toplevel()
    check_window.title("Goncharenko Security Anti-Virus — Проверка файлов")
    check_window.geometry("600x350")
    check_window.grab_set()
    check_window.focus_set()
    # Настраиваем окно проверки
    check_window.configure(bg="#ebebeb")
    check_window.resizable(width=False, height=False)
    screen_width = check_window.winfo_screenwidth()
    screen_height = check_window.winfo_screenheight()
    x_coordinate = int((screen_width / 2) - (600 / 2))
    y_coordinate = int((screen_height / 2) - (350 / 2))
    check_window.geometry(f"600x350+{x_coordinate}+{y_coordinate}")
    check_window.iconbitmap("icon.ico")
    # Создаем кнопку проверки
    rectangle_frame = tk.Frame(check_window, width=540, height=80, bg="#ebebeb", bd=0, highlightthickness=2,
                               highlightbackground="#d0d0d0")
    rectangle_frame.place(x=30, y=130)
    rectangle_frame.config(cursor="hand2")

    # Функция для вычисления MD5-хеша файла
    def get_md5(filename):
        hash_md5 = hashlib.md5()
        with open(filename, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    # Функция для проверки VirusTotal API
    def check_viruses(filename):
        md5 = get_md5(filename)
        url = "https://www.virustotal.com/api/v3/files/" + md5
        params = {"apikey": "799505f8157038b45efaedfc452ac3f52324555b4d7383bda1a04757d7b1e81d"}
        headers = {"x-apikey": params["apikey"]}
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            json_data = response.json()
            if "data" in json_data and "attributes" in json_data["data"] and "last_analysis_results" in \
                    json_data["data"]["attributes"]:
                last_analysis_results = json_data["data"]["attributes"]["last_analysis_results"]
                num_detected_viruses = sum(
                    1 for result in last_analysis_results.values() if result["category"] == "malicious")
                if num_detected_viruses > 0:
                    result_label.config(text="Файл заражен", fg="red")
                    degr_label.config(text="Высокая", fg="red")

                    # создаем кнопку "Начать лечение"
                    cure_button = tk.Button(check_window, text="Начать лечение", font=("Ruberoid Semi Bold", 10),
                                            width=15, bd=1, command=lambda: delete_file(filename))
                    cure_button.place(x=425, y=285)

                else:
                    result_label.config(text="Вирусов не обнаружено", fg="green")
                    degr_label.config(text="Угроз нет", fg="green")
            else:
                result_label.config(text="Файл не найден в базе", fg="black")
                degr_label.config(text="Неизвестно", fg="black")
        except requests.exceptions.HTTPError as e:
            result_label.config(text="Файл не найден в базе", fg="black")
            degr_label.config(text="Неизвестно", fg="black")
        except Exception as e:
            result_label.config(text="Файл не найден в базе", fg="black")
            degr_label.config(text="Неизвестно", fg="black")

    # Обрабатывааем файл
    def select_file(event):
        filename = filedialog.askopenfilename()
        check_viruses(filename)
        file_label.config(text=f"{os.path.basename(filename)}")

    # Удаляем файл в случае обнаружения вируса
    def delete_file(filename):
        try:
            os.remove(filename)
            result_label.config(text="Файл успешно удален", fg="green")
            degr_label.config(text="Угроз нет", fg="green")
        except Exception as e:
            result_label.config(text="Не удалось удалить файл", fg="red")
            degr_label.config(text="Неизвестно", fg="red")

    # Выводим результаты проверки
    file_label = tk.Label(check_window, text=(""), bg="#ebebeb", font=("Ruberoid Semi Bold", 11),
                          justify="left")
    file_label.place(x=120, y=230)
    name_label = tk.Label(check_window, text=("Название:"), bg="#ebebeb", font=("Ruberoid Semi Bold", 11),
                          justify="left")
    name_label.place(x=30, y=230)

    result_label = tk.Label(check_window, text=(""), bg="#ebebeb", font=("Ruberoid Semi Bold", 11),
                            justify="left")
    result_label.place(x=205, y=260)
    resultat_label = tk.Label(check_window, text=("Результат проверки:"), bg="#ebebeb", font=("Ruberoid Semi Bold", 11),
                              justify="left")
    resultat_label.place(x=30, y=260)

    degr_label = tk.Label(check_window, text=(""), bg="#ebebeb", font=("Ruberoid Semi Bold", 11),
                          justify="left")
    degr_label.place(x=170, y=290)
    degree_label = tk.Label(check_window, text=("Степень угрозы:"), bg="#ebebeb", font=("Ruberoid Semi Bold", 11),
                            justify="left")
    degree_label.place(x=30, y=290)

    # Добавляем надпись
    text1 = tk.Label(check_window, text="Проверка файлов", bg="#ebebeb", font=("Ruberoid Bold", 19))
    text1.place(x=30, y=20)
    # Добавляем описание
    text_info = tk.Label(check_window, text="После выбора файла, он будет загружен в систему, где проводится"
                                            "\nпроверка на наличие вирусов и других вредоносных программ. ",
                     bg="#ebebeb", font=("Ruberoid Medium", 11), justify="left")
    text_info.place(x=30, y=65)
    # Добавляем надпись на кнопке проверки
    text_on_button = tk.Label(check_window, text="Выберите файл для проверки", font=("Ruberoid Semi Bold", 12),
                              bg="#ebebeb", justify="left", fg="#999999")
    text_on_button.place(x=175, y=155)
    text_on_button.config(cursor="hand2")
    # Добавляем обработчик на прямоугольник и надпись
    rectangle_frame.bind("<Button-1>", select_file)
    text_on_button.bind("<Button-1>", select_file)

    pass

# Добавляем обработчик событий к 1-ой кнопке меню
canvas.tag_bind(rect1, '<ButtonPress-1>', on_rect1_click)
canvas.tag_bind(img1_id, '<ButtonPress-1>', on_rect1_click)
canvas.tag_bind(text1, '<ButtonPress-1>', on_rect1_click)

# Добавляем обработчик событий к 3-ей кнопке меню
canvas.tag_bind(rect3, '<Button-1>', lambda event: open_about_window())
canvas.tag_bind(img3_id, '<Button-1>', lambda event: open_about_window())
canvas.tag_bind(text3, '<Button-1>', lambda event: open_about_window())

# Изменяем курсор при наведении
def on_enter_rect(event):
    item_id = event.widget.find_withtag('current')
    canvas.itemconfig(item_id, fill="#ffffff")
    canvas.config(cursor="hand2")
def on_leave_rect(event):
    item_id = event.widget.find_withtag('current')
    canvas.itemconfig(item_id, fill="#ffffff")
    canvas.config(cursor="")
def on_enter_img(event):
    canvas.config(cursor="hand2")
def on_leave_img(event):
    canvas.config(cursor="")
def on_text_enter(event):
    item_id = event.widget.find_withtag('current')
    canvas.itemconfig(item_id, fill="black")
    canvas.config(cursor="hand2")
def on_text_leave(event):
    item_id = event.widget.find_withtag('current')
    canvas.itemconfig(item_id, fill="black")
    canvas.config(cursor="")

# Связываем прямоугольники, изображения и текст с функцией
for rect, img_id in [(rect1, img1_id), (rect2, img2_id), (rect3, img3_id)]:
    canvas.tag_bind(rect, "<Enter>", on_enter_rect)
    canvas.tag_bind(rect, "<Leave>", on_leave_rect)
    canvas.tag_bind(img_id, "<Enter>", on_enter_img)
    canvas.tag_bind(img_id, "<Leave>", on_leave_img)
for text in [text1, text2, text3]:
    canvas.tag_bind(text, "<Enter>", on_text_enter)
    canvas.tag_bind(text, "<Leave>", on_text_leave)

# Добавляем блоки и картинки
bottom_frame.pack(side="bottom", fill="both", expand=True)

image = Image.open("shield150icon.png")
photo = ImageTk.PhotoImage(image)
label = tk.Label(top_frame, image=photo, bg="#38be39", highlightthickness=0)
label.place(x=65, y=30)

# Создаем текст "Вы защищены"
text_label1 = tk.Label(top_frame, text="Вы защищены", font=("Ruberoid Bold", 26), bg="#38be39", fg="white")
text_label1.place(x=270, y=30)

# Создаем текст "Проведите проверку"
current_time = time.strftime("%H:%M")
text_label2 = tk.Label(top_frame, text=f"Последняя проверка не прошла",
                       font=("Ruberoid Bold", 13), bg="#38be39", fg="white")
text_label2.place(x=270, y=90)

# Создаем кнопку "Начать проверку"
start_button = tk.Button(top_frame, text="Начать проверку", font=("Ruberoid Semi Bold", 13),
                          background="#ffffff", fg="#38be39", activeforeground="#38be39",
                          width=18, height=1, bd=0, relief="solid",
                          activebackground="#ededed", anchor="center", justify="center", borderwidth=0)
start_button.place(x=275, y=140)
start_button.config(cursor="hand2")
# Изменяем фон при наведении на кнопку
start_button.bind("<Enter>", lambda e: start_button.config(bg="#ededed"))
start_button.bind("<Leave>", lambda e: start_button.config(bg="#ffffff"))

# Начинаем быструю проверку на вирусы
def start_check():
    start_button.config(text="Выполнение...", state="disabled")
    # Создаем поток для выполнения команды PowerShell.exe
    scan_thread = threading.Thread(target=run_scan)
    scan_thread.start()

def run_scan():
    # Выполняем сканирование
    output = subprocess.check_output("PowerShell.exe -Command Start-MpScan -ScanType QuickScan", shell=True)

    # Проверяем наличие угроз
    threats_detected = False
    for line in output.splitlines():
        if b"ThreatsDetected" in line:
            # Извлечение числа из строки
            num_threats = int(line.split()[-1])
            if num_threats > 0:
                threats_detected = True
            break

    main_window.after(0, end_treatment, threats_detected)

# Выводим после проверки
def end_treatment(threats_detected):
    start_button.config(text="Начать проверку", state="normal")
    text_label2.config(text=f"Последняя проверка прошла в {current_time}")

# Привязываем функцию start_check
start_button.config(command=start_check)

# Создаем подсказку
quest_button = tk.Button(top_frame, text="?", font=("Ruberoid Semi Bold", 13),
                          background="#ffffff", fg="#38be39", activeforeground="#38be39",
                          width=3, height=1, bd=0, relief="solid",
                          activebackground="#ffffff", anchor="center", justify="center", borderwidth=0)
quest_button.place(x=481, y=140)
quest_button.config(cursor="hand2")
tooltip = tk.Label(top_frame, text=" Антивирус проверяет запущенные\n процессы на вирусы. Если процесс\n"
                                   "заражен, то антивирус\n останавливает и удаляет его.", bg="#ffffff", fg="#000000",
                   font=("Ruberoid Semi Bold", 9),
                   width=29, height=4, bd=1, relief="solid")
tooltip.config(cursor="arrow", anchor="nw", justify="left")
tooltip.place_forget()
# Размещаем подсказку
def show_tooltip(event):
    tooltip.after(0, lambda: tooltip.place(x=520, y=110))
def hide_tooltip(event):
    tooltip.place_forget()
# Меняем курсор при наведении
quest_button.bind("<Enter>", show_tooltip)
quest_button.bind("<Leave>", hide_tooltip)

# Создаем кнопку уведомлений
image_bell = Image.open("image_bell.png")
photo_bell = ImageTk.PhotoImage(image_bell)
image_label = tk.Label(top_frame, image=photo_bell, bg="#38be39", highlightthickness=0)
image_label.place(x=730, y=40)
image_label.config(cursor="hand2")

# Запускаем цикл обработки кода
main_window.mainloop()