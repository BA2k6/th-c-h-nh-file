from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import csv
from datetime import datetime
import pandas as pd

def save_csv():
    d = {
        "Mã": entry_ma.get(),
        "Tên": entry_ten.get(),
        "Ngày sinh": dateentry.get(),
        "Giới tính": "Nam" if gender_var.get() == 1 else "Nữ",
        "Đơn vị": donv.get(),
        "Số CMND": so_entry.get(),
        "Ngày cấp": dateentry.get(),
        "Nơi cấp": S_entry.get(),
        "Chức danh": T_entry.get()
    }

    with open("employees.csv", mode="a", newline='', encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=d.keys())
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(d)

    messagebox.showinfo("Thông báo", "Lưu thông tin thành công!")
    xuli()

def SinhNhat():
    try:
        today = datetime.now().strftime("%d/%m/%Y")
        NhanVien = []
        with open("employees.csv", mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Ngày sinh'][:-5] == today[:-5]:  # So sánh ngày và tháng
                    NhanVien.append(row)

        if NhanVien:
            result = "Nhân viên có sinh nhật hôm nay:\n\n" + "\n".join([row['Tên'] for row in NhanVien])
        else:
            result = "Không có nhân viên nào sinh nhật hôm nay."

        messagebox.showinfo("Kết quả", result)
    except FileNotFoundError:
        messagebox.showerror("Lỗi", "File dữ liệu chưa được tạo!")


def exel():
    try:
        df = pd.read_csv("employees.csv", encoding="utf-8")
        df['Ngày sinh'] = pd.to_datetime(df['Ngày sinh'], format="%d/%m/%Y")
        df.sort_values(by="Ngày sinh", ascending=True, inplace=True)
        output_file = "sorted_employees.xlsx"
        df.to_excel(output_file, index=False)  # Xóa encoding="utf-8"
        messagebox.showinfo("Thông báo", f"Xuất danh sách thành công! File: {output_file}")
    except FileNotFoundError:
        messagebox.showerror("Lỗi", "File dữ liệu chưa được tạo!")

def xuli():
    entry_ma.delete(0, END)
    entry_ten.delete(0, END)
    dateentry.set_date(datetime.now())
    gender_var.set(0)
    combobox.set("")
    so_entry.delete(0, END)
    dateentry.set_date(datetime.now())
    S_entry.delete(0, END)
    T_entry.delete(0, END)

CuaSo = Tk()
CuaSo.title("Thông tin nhân viên")
CuaSo.geometry("850x400")

lbl = Label(CuaSo, text="Thông tin nhân viên", fg="black", font=("Timenewroman", 23))
lbl.grid(column=0, row=0, columnspan=4, pady=10,sticky="W")

lakh= Checkbutton(CuaSo,text="Là khách hàng")
lakh.grid(column=1,row=0,sticky="w")

lanv= Checkbutton(CuaSo,text="Là nhân viên")
lanv.grid(column=2,row=0)
ma = Label(CuaSo, text="Mã", fg="black", font=("Arial", 10))
ma.grid(column=0, row=1, sticky="W")
entry_ma = Entry(CuaSo, width=30)
entry_ma.grid(column=0, row=2, padx=5, pady=5, sticky="W")

ten = Label(CuaSo, text="Tên", fg="black", font=("Arial", 10))
ten.grid(column=1, row=1, sticky="W")
entry_ten = Entry(CuaSo, width=30,bd=2,relief="groove")
entry_ten.grid(column=1, row=2, padx=5, pady=5,sticky="w")

NgaySinh = Label(CuaSo, text="Ngày sinh", fg="black", font=("Arial", 10))
NgaySinh.grid(column=2, row=1, sticky="W")
dateentry = DateEntry(CuaSo, width=20, foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy')
dateentry.grid(column=2, row=2, sticky="W")

gt = Label(CuaSo, text="Giới tính", fg="black", font=("Arial", 10))
gt.grid(column=3, row=1, sticky="W")
gender_var = IntVar()
chk3 = Radiobutton(CuaSo, text="Nam", variable=gender_var, value=1)
chk3.grid(row=2, column=3, padx=10, pady=5, sticky="W")
chk4 = Radiobutton(CuaSo, text="Nữ", variable=gender_var, value=2)
chk4.grid(row=2, column=4, padx=10, pady=5, sticky="W")

DonVi = Label(CuaSo, text="Đơn vị", fg="black", font=("Arial", 10))
DonVi.grid(column=0, row=3, sticky="W")
donv = StringVar()
don = ["Lớp 1", "Lớp 2", "Lớp 3", "Lớp 4", "Lớp 5", "Lớp 6"]
combobox = ttk.Combobox(CuaSo, textvariable=donv, values=don, width=27, font=("Arial", 12), state="readonly")
combobox.grid(row=4, column=0, padx=5, pady=5, sticky="W")

cm = Label(CuaSo, text="Số CMND", fg="black", font=("Arial", 10))
cm.grid(column=1, row=3, sticky="W")
so_entry = Entry(CuaSo, width=30)
so_entry.grid(column=1, row=4, sticky="W")

NgayCap = Label(CuaSo, text="Ngày cấp", fg="black", font=("Arial", 10))
NgayCap.grid(column=2, row=3, sticky="W")
dateentry = DateEntry(CuaSo, width=20, foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy')
dateentry.grid(column=2, row=4, sticky="W")

ChucDanh = Label(CuaSo, text="Chức danh", fg="black", font=("Arial", 10))
ChucDanh.grid(column=0, row=5, sticky="W")
T_entry = Entry(CuaSo, width=40)
T_entry.grid(column=0, row=6, sticky="W")

NoiCap = Label(CuaSo, text="Nơi cấp", fg="black", font=("Arial", 10))
NoiCap.grid(column=1, row=5, sticky="W")
S_entry = Entry(CuaSo, width=40)
S_entry.grid(column=1, row=6, sticky="W")
send = Button(CuaSo, text="Send", command=save_csv, width=15, height=2)
send.grid(row=7, column=0, padx=10, pady=20)

birthday = Button(CuaSo, text="Sinh nhật hôm nay", command=SinhNhat, width=20, height=2)
birthday.grid(row=7, column=1, padx=10, pady=20)

export = Button(CuaSo, text="Xuất danh sách", command=exel, width=20, height=2)
export.grid(row=7, column=2, padx=10, pady=20)

CuaSo.mainloop()

