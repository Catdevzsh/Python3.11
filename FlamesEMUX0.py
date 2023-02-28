import tkinter as tk

class FlamesEMU_GUI:
    def __init__(self, master):
        self.master = master
        master.title("FlamesEMU")

        # Setting up emulator options
        self.supported_systems = ["SNES", "NES", "Gameboy", "Atari Lynx", "Game Gear", "Game Boy Advance", "Game Boy Color", "Neo Geo Pocket", "Nintendo 64", "Nintendo DS", "PlayStation", "Sega 32X", "Sega CD", "Sega Genesis", "Sega Master System", "Sony PSP", "Super Nintendo Entertainment System", "TurboGrafx-16"]
        self.selected_system = tk.StringVar(master)
        self.selected_system.set(self.supported_systems[0])

        # Setting up window layout
        self.system_label = tk.Label(master, text="Select System:", font=("Arial", 14, "bold"), padx=20, pady=20)
        self.system_dropdown = tk.OptionMenu(master, self.selected_system, *self.supported_systems)
        self.system_dropdown.config(font=("Arial", 14))
        self.run_button = tk.Button(master, text="Run Emulator", command=self.run_emulator, font=("Arial", 14), bg="#4CAF50", fg="white", padx=20, pady=10, bd=0)
        self.run_button.config(activebackground="#2E7D32", activeforeground="white")

        # Adding elements to the window layout
        self.top_screen = tk.Canvas(master, bg="#C9C9C9", width=200, height=100, highlightthickness=0)
        self.bottom_screen = tk.Canvas(master, bg="#C9C9C9", width=200, height=100, highlightthickness=0)
        self.top_screen.place(relx=0.5, rely=0.3, anchor="center")
        self.bottom_screen.place(relx=0.5, rely=0.7, anchor="center")

        self.system_label.pack()
        self.system_dropdown.pack()
        self.run_button.pack()

    def run_emulator(self):
        selected = self.selected_system.get()
        print(f"Starting FlamesEMU for {selected} system with OpenEmu BIOS")

root = tk.Tk()
root.geometry("600x400")
flamesemu_gui = FlamesEMU_GUI(root)
root.mainloop()
import tkinter as tk

class FlamesEMU_GUI:
    def __init__(self, master):
        self.master = master
        master.title("FlamesEMU")

        # Setting up emulator options
        self.supported_systems = ["SNES", "NES", "Gameboy", "Atari Lynx", "Game Gear", "Game Boy Advance", "Game Boy Color", "Neo Geo Pocket", "Nintendo 64", "Nintendo DS", "PlayStation", "Sega 32X", "Sega CD", "Sega Genesis", "Sega Master System", "Sony PSP", "Super Nintendo Entertainment System", "TurboGrafx-16"]
        self.selected_system = tk.StringVar(master)
        self.selected_system.set(self.supported_systems[0])

        # Setting up window layout
        self.system_label = tk.Label(master, text="Select System:", font=("Arial", 14, "bold"), padx=20, pady=20)
        self.system_dropdown = tk.OptionMenu(master, self.selected_system, *self.supported_systems)
        self.system_dropdown.config(font=("Arial", 14))
        self.run_button = tk.Button(master, text="Run Emulator", command=self.run_emulator, font=("Arial", 14), bg="#4CAF50", fg="white", padx=20, pady=10, bd=0)
        self.run_button.config(activebackground="#2E7D32", activeforeground="white")

        # Adding elements to the window layout
        self.top_screen = tk.Canvas(master, bg="#C9C9C9", width=200, height=100, highlightthickness=0)
        self.bottom_screen = tk.Canvas(master, bg="#C9C9C9", width=200, height=100, highlightthickness=0)
        self.top_screen.place(relx=0.5, rely=0.3, anchor="center")
        self.bottom_screen.place(relx=0.5, rely=0.7, anchor="center")

        self.system_label.pack()
        self.system_dropdown.pack()
        self.run_button.pack()

    def run_emulator(self):
        selected = self.selected_system.get()
        print(f"Starting FlamesEMU for {selected} system with OpenEmu BIOS")

root = tk.Tk()
root.geometry("600x400")
flamesemu_gui = FlamesEMU_GUI(root)
root.mainloop()
