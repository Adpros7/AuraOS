import tkinter as tk


def main():
    
    def on_key(event):
        print(f"Key pressed: {event.keysym}")

    root = tk.Tk()
    root.title("AuraOS")
    root.geometry("500x500")
    root.bind("<Key>", on_key)
    root.configure(bg="#000000")  # Set the
    root.mainloop()


if __name__ == "__main__":
    main()
