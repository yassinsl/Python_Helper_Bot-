import tkinter as tk
import os

class ShutdownApp:
    def __init__(self, master):
        self.master = master
        master.title("Shutdown, Restart, Logout App")

        self.shutdown_button = tk.Button(master, text="Shutdown", command=self.shutdown)
        self.shutdown_button.pack()

        self.restart_button = tk.Button(master, text="Restart", command=self.restart)
        self.restart_button.pack()

        self.logout_button = tk.Button(master, text="Logout", command=self.logout)
        self.logout_button.pack()

    def shutdown(self):
        self.countdown(9)  
        os.system("shutdown /s /t 10") 

    def restart(self):
        self.countdown(9) 
        os.system("shutdown /r /t 10") 

    def logout(self):
        self.countdown(9)  
        os.system("shutdown -l")  

    def countdown(self, remaining):
        if remaining >= 0:
            self.master.title(f"Shutting down in {remaining} seconds...")
            self.master.after(1000, self.countdown, remaining - 1)
        else:
            self.master.title("Shutdown, Restart, Logout App")

def main():
    root = tk.Tk()
    app = ShutdownApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
