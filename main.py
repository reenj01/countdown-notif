import tkinter as tk
from tkcalendar import Calendar
# from tkinter import simpledialog
from tkinter import ttk
from datetime import datetime, date

window = tk.Tk()
window.title("Select Date")

style = ttk.Style(window)
style.theme_use('default')
# style.map("Calendar.Treeview", background=[('selected', 'white')])

today = date.today()

# calendar
cal = Calendar(
  window, 
  selectmode='day', 
  year=today.year, 
  month=today.month, 
  day=today.day
  )
cal.pack(padx=10, pady=10) # 10px of padding all around

# text entry
tk.Label(window, text="Event Name:").pack(pady=(10, 0))
text = tk.Entry(window, width=30)
text.pack(pady=(0, 10))

def get_inputs():
  global date_input, desc_input
  date_input = cal.selection_get() # returns a datetime.date object
  desc_input = text.get()
  window.destroy()

# OK button
tk.Button(window, text="OK", command=get_inputs).pack(pady=10)

window.mainloop()

print("Selected date:", date_input)
print("Event name:", desc_input)

# subtract chosen date and today's date
future_date = date(date_input.year, date_input.month, date_input.day)
delta = future_date - today
countdown = delta.days

print(countdown)

# create popup notif
def show_notif():
   # fade popup
  alpha = 1.0

  def fade():
    nonlocal alpha
    alpha -= 0.03
    if alpha > 0:
      notif.attributes("-alpha", alpha)
      notif.after(50, fade)
    else:
      notif.destroy()
  
  notif = tk.Tk()
  notif.overrideredirect(True) # remove window borders
  notif.attributes("-topmost", True)
  notif.geometry("250x100+1000+50")

  label = tk.Label(notif, text=f"D-{countdown}: {desc_input}", font=("Helvetica", 14))
  label.pack(padx=10, pady=10)

  notif.after(2500, fade)
  notif.mainloop()

show_notif()