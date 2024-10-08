import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as mbox
import math

win = tk.Tk()
win.title("Simple Math")
tabControl = ttk.Notebook(win)

# Thêm các tab
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)

# Đổi tên tab
tabControl.add(tab1, text='Phương trình bậc 2')  # Tab 1: Phương trình bậc 2
tabControl.add(tab2, text='Trọng lượng')  # Tab 2: Chuyển đổi trọng lượng
tabControl.add(tab3, text="Canvas")  # Tab 3: Canvas màu

tabControl.pack(expand=1, fill='both')

# === Giao diện Tab 1: Phương trình bậc 2 ===
main_label = ttk.Label(tab1, text="ax^2 + bx + c = 0")
main_label.grid(column=0, row=0, padx=10, pady=3)

a_label = ttk.Label(tab1, text="a")
a_label.grid(column=0, row=2)
a = tk.IntVar()
a_entered = ttk.Entry(tab1, width=12, textvariable=a)
a_entered.grid(column=1, row=2, padx=3)

b_label = ttk.Label(tab1, text="b")
b_label.grid(column=0, row=3)
b = tk.IntVar()
b_entered = ttk.Entry(tab1, width=12, textvariable=b)
b_entered.grid(column=1, row=3)

c_label = ttk.Label(tab1, text="c")
c_label.grid(column=0, row=4)
c = tk.IntVar()
c_entered = ttk.Entry(tab1, width=12, textvariable=c)
c_entered.grid(column=1, row=4)

result_label = ttk.Label(tab1, text="Nghiệm:")
result_label.grid(column=0, row=6)

result_var = tk.StringVar()
result_entry = ttk.Entry(tab1, width=25, textvariable=result_var, state='readonly')
result_entry.grid(column=1, row=6)


# Hàm giải phương trình bậc 2
def solve_quadratic():
    try:
        a_val = a.get()
        b_val = b.get()
        c_val = c.get()
        
        if a_val == 0:
            mbox.showerror("Error", "a phải khác 0 để là phương trình bậc 2")
            return

        # Tính delta (b^2 - 4ac)
        delta = b_val ** 2 - 4 * a_val * c_val

        if delta > 0:
            x1 = (-b_val + math.sqrt(delta)) / (2 * a_val)
            x2 = (-b_val - math.sqrt(delta)) / (2 * a_val)
            result_var.set(f"x1 = {x1:.2f}, x2 = {x2:.2f}")
        elif delta == 0:
            x = -b_val / (2 * a_val)
            result_var.set(f"x = {x:.2f}")
        else:
            result_var.set("Phương trình vô nghiệm")
    except ValueError:
        mbox.showerror("Lỗi nhập liệu", "Vui lòng nhập số hợp lệ")


# Thêm nút để giải phương trình
solve_button = ttk.Button(tab1, text="Giải", command=solve_quadratic)
solve_button.grid(column=0, row=5, columnspan=3, pady=10)

# === Giao diện Tab 2: Chuyển đổi trọng lượng ===

# Hàm chuyển đổi trọng lượng
def convert_weight():
    try:
        input_value = float(weight_entry.get())
        from_unit = from_combo.get()
        to_unit = to_combo.get()
        conversion_factors = {
            'Kilograms (kg)': {
                'Kilograms (kg)': 1,
                'Grams (g)': 1000,
                'Milligrams (mg)': 1000000
            },
            'Grams (g)': {
                'Kilograms (kg)': 1 / 1000,
                'Grams (g)': 1,
                'Milligrams (mg)': 1000
            },
            'Milligrams (mg)': {
                'Kilograms (kg)': 1 / 1000000,
                'Grams (g)': 1 / 1000,
                'Milligrams (mg)': 1
            }
        }

        # Tính toán kết quả
        result = input_value * conversion_factors[from_unit][to_unit]
        weight_result.set(format(result, '.10f').rstrip('0').rstrip('.'))
    except ValueError:
        mbox.showerror("Lỗi nhập liệu", "Vui lòng nhập số hợp lệ")
    except:
        mbox.showerror("Lỗi", "Đã xảy ra lỗi, vui lòng kiểm tra lại")


# Nhãn tiêu đề cho Tab 2
title_label = tk.Label(tab2, text="Chuyển đổi trọng lượng (kg, g, mg)")
title_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Nhập giá trị cần chuyển đổi
entry_label = tk.Label(tab2, text="Giá trị:")
entry_label.grid(row=1, column=0)

weight_entry = tk.Entry(tab2, width=10)
weight_entry.grid(row=1, column=1)

# Combo box chọn đơn vị gốc
from_combo = ttk.Combobox(tab2, width=15, state='readonly')
from_combo['value'] = ('Kilograms (kg)', 'Grams (g)', 'Milligrams (mg)')
from_combo.current(0)
from_combo.grid(row=1, column=2)

# Nhãn đích
to_label = tk.Label(tab2, text="Đổi sang:")
to_label.grid(row=2, column=0)

# Kết quả sau khi chuyển đổi
weight_result = tk.StringVar()
result_entry = tk.Entry(tab2, width=10, textvariable=weight_result, state="readonly")
result_entry.grid(row=2, column=1)

# Combo box chọn đơn vị đích
to_combo = ttk.Combobox(tab2, width=15, state='readonly')
to_combo['value'] = ('Kilograms (kg)', 'Grams (g)', 'Milligrams (mg)')
to_combo.current(0)
to_combo.grid(row=2, column=2)

# Nút chuyển đổi
convert_button = tk.Button(tab2, text="Chuyển đổi", command=convert_weight)
convert_button.grid(row=3, column=0, columnspan=3, pady=10)

# === Tab 3: Canvas màu đỏ và xanh biển ===
tab3_frame = tk.Frame(tab3, bg='blue')
tab3_frame.pack()

for i in range(2):
    color = 'red' if i == 0 else 'blue'
    canvas = tk.Canvas(tab3_frame, width=150, height=80, highlightthickness=0, bg=color)
    canvas.grid(row=i, column=i)

win.mainloop()
