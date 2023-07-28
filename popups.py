import tkinter as tk
import backendProcesses

class AddAppWindow(tk.Toplevel):
    def __init__(self, parent, comparisonData):
        super().__init__(parent)

        self.geometry("300x100")
        self.title("Workspace App Manager")

        self.listOfApps = tk.Label(self, text='\n'.join(app['config']['name'] for app in comparisonData), font=("Arial", 14))
        self.closeButton = tk.Button(self, text="Close", command=self.destroy)
        self.listOfApps.pack()
        self.closeButton.pack()

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
