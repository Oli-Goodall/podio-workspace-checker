import tkinter as tk
import backendProcesses
import entryWithPlaceholder

class WorkspaceCheckerGUI:

    def __init__(self):

        # Defines the root, i.e., the window that opens when code is run
        self.root = tk.Tk()
        self.root.geometry("500x300")

        # Create the EntryWithPlaceholder widget without focus
        self.franchiseeSelectionInput = entryWithPlaceholder.EntryWithPlaceholder(self.root, "Start typing location...")
        self.franchiseeSelectionInput.pack(pady=20)

        self.listboxFrame = tk.Frame(self.root)
        self.listboxScrollbar = tk.Scrollbar(self.listboxFrame, orient=tk.VERTICAL)
        self.franchiseeListBox = tk.Listbox(self.listboxFrame, width=20, height=10, yscrollcommand=self.listboxScrollbar.set)

        self.listboxScrollbar.config(command=self.franchiseeListBox.yview)
        self.listboxScrollbar.config(command=self.franchiseeListBox.yview)

        # Hide listbox initially
        self.franchiseeListBox.pack_forget()
        self.listboxScrollbar.pack_forget()


        # Retrieve list of franchisee space names from Podio
        self.franchiseSpaceNames = [space['name'].split('Accountants', 1)[-1].strip() for space in backendProcesses.franchiseeWorkspacesList]

        # Add franchisee space names to listbox
        self.update(self.franchiseSpaceNames)

        # Create a binding on the listbox onclick
        self.franchiseeListBox.bind("<<ListboxSelect>>", self.fillout)

        # Create a binding on the input field
        self.franchiseeSelectionInput.bind("<KeyRelease>", self.check)
        self.franchiseeSelectionInput.bind("<FocusIn>", self.on_entry_focus_in)

        # Set focus on the root when the window is clicked
        self.root.bind("<Button-1>", self.on_root_click)

        # Tells the root window to render
        self.root.mainloop()

    def update(self, data):
        self.franchiseeListBox.delete(0, tk.END)
        for item in data:
            self.franchiseeListBox.insert(tk.END, item)

    def fillout(self, e):
        self.franchiseeSelectionInput.delete(0, tk.END)
        self.franchiseeSelectionInput.insert(0, self.franchiseeListBox.get(tk.ANCHOR))

    def check(self, e):
        typed = self.franchiseeSelectionInput.get()

        if typed == '':
            data = self.franchiseSpaceNames
        else:
            data = []
            for item in self.franchiseSpaceNames:
                if typed.lower() in item.lower():
                    data.append(item)

        self.update(data)
        # Show the listbox only when there are matching results and the input field has focus
        if data and self.franchiseeSelectionInput.focus_get() == self.franchiseeSelectionInput:
            self.listboxFrame.pack()
            self.franchiseeListBox.pack(side=tk.LEFT)
            self.listboxScrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        else:
            self.franchiseeListBox.pack_forget()
            self.listboxScrollbar.pack_forget()

    def on_root_click(self, event):
        # Set focus on the root window explicitly
        self.root.focus_set()

        # Hide the listbox and scrollbar when clicking outside the input field
        self.franchiseeListBox.pack_forget()
        self.listboxScrollbar.pack_forget()

    def on_entry_focus_in(self, event):
        # Set focus to the Entry widget when it gains focus
        self.franchiseeSelectionInput.focus_set()
        self.franchiseeSelectionInput.foc_in()
