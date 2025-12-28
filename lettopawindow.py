import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
#pillow library is used to open and manipulate images


def main():
   """Sets up the main window of the application."""
   root = tk.Tk()
   root.title('Denomination Counter')
   root.configure(bg='light blue')
   root.geometry('650x400')


   # Load and display the image
   try:
       upload = Image.open("app_img.jpg")
       upload = upload.resize((300, 300))
       image = ImageTk.PhotoImage(upload)
       label = tk.Label(root, image=image, bg='light blue')
       label.image = image  # Keep a reference to prevent garbage collection
       label.place(x=180, y=20)
   except FileNotFoundError:
       tk.Label(root, text="Image not found", bg='light blue').place(x=180, y=20)


   # Welcome label
   label1 = tk.Label(
       root,
       text="Hey User! Welcome to Denomination Counter Application.",
       bg='light blue'
   )
   label1.place(relx=0.5, y=340, anchor=tk.CENTER)


   # Start button
   button1 = tk.Button(
       root,
       text="Let's get started!",
       command=lambda: topwin(root),  # Pass root to topwin
       bg='brown',
       fg='white'
   )
   button1.place(x=260, y=360)


   root.mainloop()


def topwin(root):
   """Creates and manages the top-level window for denomination calculation."""
   top = tk.Toplevel(root)  # Pass the main window as the parent
   top.title("Denominations Calculator")
   top.configure(bg='light grey')
   top.geometry("600x350+50+50")


   # Labels and entry fields
   amount_label = tk.Label(top, text="Enter total amount", bg='light grey')
   amount_entry = tk.Entry(top)
   result_label = tk.Label(top, text="Here are number of notes for each denomination", bg='light grey')


   label_1000 = tk.Label(top, text="1000", bg='light grey')
   label_500 = tk.Label(top, text="500", bg='light grey')
   label_100 = tk.Label(top, text="100", bg='light grey')


   entry_1000 = tk.Entry(top)
   entry_500 = tk.Entry(top)
   entry_100 = tk.Entry(top)


   def calculator():
       """Calculates and displays the denomination breakdown."""
       try:
           amount = int(amount_entry.get())
           if amount < 0:
               messagebox.showerror("Error", "Please enter a non-negative number.")
               return


           note_1000 = amount // 1000
           amount %= 1000
           note_500 = amount // 500
           amount %= 500
           note_100 = amount // 100


           entry_1000.delete(0, tk.END)
           entry_500.delete(0, tk.END)
           entry_100.delete(0, tk.END)


           entry_1000.insert(tk.END, str(note_1000))
           entry_500.insert(tk.END, str(note_500))
           entry_100.insert(tk.END, str(note_100))


       except ValueError:
           messagebox.showerror("Error", "Please enter a valid number.")


   calculate_button = tk.Button(top, text='Calculate', command=calculator, bg='brown', fg='white')


   # Place widgets in the top window
   amount_label.place(x=230, y=50)
   amount_entry.place(x=200, y=80)
   calculate_button.place(x=240, y=120)
   result_label.place(x=140, y=170)


   label_1000.place(x=180, y=200)
   label_500.place(x=180, y=230)
   label_100.place(x=180, y=260)


   entry_1000.place(x=270, y=200)
   entry_500.place(x=270, y=230)
   entry_100.place(x=270, y=260)


   # top.mainloop() # Removed this.  Only root should have mainloop.
if __name__ == "__main__":
   main()



