import tkinter as tk


class AddAppWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry("300x100")
        self.title("Workspace App Manager")

        tk.Button(self, text="Close", command=self.destroy).pack(expand=True)

class ConfirmExitWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry("300x100")
        self.title("Quit?")
        self.label = tk.Label(self, text="Are you sure you want to quit?", font=("Arial", 16))
        self.label.pack()

        self.buttonFrame = tk.Frame(self, pady=10)
        tk.Button(self.buttonFrame, text="Cancel", command=self.destroy).pack(expand=True, side=tk.LEFT)
        tk.Button(self.buttonFrame, text="Quit", command=self.quit).pack(expand=True, side=tk.RIGHT)
        self.buttonFrame.pack()
