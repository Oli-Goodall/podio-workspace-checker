import tkinter as tk
import backendProcesses
import entryWithPlaceholder
import popups

class LandingPage:

    def __init__(self):

        # Defines the root, i.e., the window that opens when code is run
        self.root = tk.Tk()
        self.root.geometry("500x300")

        self.topFrame = tk.Frame(self.root)
        self.landingTitle = tk.Label(self.topFrame, text='Select the franchise location you want to check:', font=("Arial", 20))
        self.landingTitle.pack(pady=10)

        self.middleFrame = tk.Frame(self.root)
        # Create the EntryWithPlaceholder widget without focus
        self.franchiseeSelectionInput = entryWithPlaceholder.EntryWithPlaceholder(self.middleFrame, "Start typing location...")
        self.franchiseeSelectionInput.pack()

        self.listboxFrame = tk.Frame(self.middleFrame)
        self.listboxScrollbar = tk.Scrollbar(self.listboxFrame, orient=tk.VERTICAL)
        self.franchiseeListBox = tk.Listbox(self.listboxFrame, width=20, height=10, yscrollcommand=self.listboxScrollbar.set)

        self.listboxScrollbar.config(command=self.franchiseeListBox.yview)
        self.listboxScrollbar.config(command=self.franchiseeListBox.yview)

        # Hide listbox initially
        self.franchiseeListBox.pack_forget()
        self.listboxScrollbar.pack_forget()

        # Retrieve list of franchisee space names from Podio
        self.franchiseSpaceNames = [{'id': space['id'], 'name': space['name'].split('Accountants', 1)[-1].strip()} for space in backendProcesses.franchiseeWorkspacesList]

        # Add franchisee space names to listbox
        self.update(self.franchiseSpaceNames)

        # Create a binding on the listbox onclick
        self.franchiseeListBox.bind("<<ListboxSelect>>", self.fillout)

        # Create a binding on the input field
        self.franchiseeSelectionInput.bind("<KeyRelease>", self.check)
        self.franchiseeSelectionInput.bind("<FocusIn>", self.on_entry_focus_in)

        # Set focus on the root when the window is clicked
        self.root.bind("<Button-1>", self.on_root_click)
        
        self.bottomFrame = tk.Frame(self.root)
        self.submitButton = tk.Button(self.bottomFrame, text="Submit", command=self.handleSubmit)
        self.exitButton = tk.Button(self.bottomFrame, text="Exit", command=self.handleExit)
        self.submitButton.pack(side=tk.LEFT)
        self.exitButton.pack(side=tk.RIGHT)

        self.topFrame.pack()
        self.middleFrame.pack()
        self.bottomFrame.pack()

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
            data = [space['name'] for space in self.franchiseSpaceNames]  # Extract 'name' from each dictionary
        else:
            data = []
            for space in self.franchiseSpaceNames:
                if typed.lower() in space['name'].lower():
                    data.append(space['name'])

        self.update(data)
        # Show the listbox only when there are matching results and the input field has focus
        if data and self.franchiseeSelectionInput.focus_get() == self.franchiseeSelectionInput:
            if len(data) < 10:
                self.franchiseeListBox.config(height=0)
            else:
                self.franchiseeListBox.config(height=10)
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

    def handleSubmit(self):
        selected_name = self.franchiseeSelectionInput.get()

        # Check if an item is selected from the listbox
        if selected_name:
            # Find the corresponding ID from self.franchiseSpaceNames
            selected_id = None
            for space in self.franchiseSpaceNames:
                if space['name'] == selected_name:
                    selected_id = space['id']
                    break

            if selected_id is not None:
                # Fetch the comparisonAppData using the selected ID
                comparison_data = backendProcesses.getFranchiseeAppList(selected_id)

                # Create the AddAppWindow instance with the fetched comparisonAppData
                add_app_window = popups.AddAppWindow(self.root, comparison_data)

                # Display the window
                add_app_window.grab_set()
            else:
                # Handle the case when the selected name does not have a corresponding ID
                print("Error: Selected franchise name does not have a corresponding ID.")
     

    def handleExit(self):
        popups.ConfirmExitWindow(self.root).grab_set()