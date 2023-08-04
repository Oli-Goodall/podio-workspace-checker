import tkinter as tk

def create_widgets():
    bottom_frame = tk.Frame(root, bg="lightgreen", height=200, width=300)
    bottom_frame.place(x=10, y=100)

    top_frame = tk.Frame(root, bg="lightblue", height=150, width=300)
    top_frame.place(x=10, y=10)

    # Create a Listbox in the top frame
    listbox = tk.Listbox(top_frame, bg="white", selectbackground="orange")
    listbox.pack(padx=10, pady=10)

    # Insert some items into the Listbox
    for i in range(1, 11):
        listbox.insert(tk.END, f"Item {i}")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("320x320")
    root.title("Overlapping Listbox Example")
    create_widgets()
    root.mainloop()
