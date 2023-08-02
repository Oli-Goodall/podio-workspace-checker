import tkinter as tk


class AddAppWindow(tk.Toplevel):
    def __init__(self, parent, comparisonData):
        super().__init__(parent)

        self.geometry("400x300")  # Adjust the window size as needed
        self.title("Workspace App Manager")

        self.comparisonData = comparisonData
        self.create_app_grid()

        self.closeButton = tk.Button(self, text="Close", command=self.destroy)
        self.closeButton.grid(row=len(comparisonData), column=0, columnspan=2, padx=5, pady=5)

    def add_app(self, app_name):
        # Define what happens when the "Add" button is clicked for a specific app
        print(f"App '{app_name}' added!")

    def create_app_grid(self):
        for row, app in enumerate(self.comparisonData):
            app_name = app['config']['name']

            # Create the app name label (aligned to the left)
            app_name_label = tk.Label(self, text=app_name, font=("Arial", 14), anchor="w")
            app_name_label.grid(row=row, column=0, padx=5, pady=5, sticky="w")

            # Create the "Add" button (aligned to the right)
            add_button = tk.Button(self, text="Add", command=lambda name=app_name: self.add_app(name))
            add_button.grid(row=row, column=1, padx=5, pady=5, sticky="e")

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
