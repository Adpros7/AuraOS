import tkinter as tk
import os


def main():
    user = os.getlogin()
    base_dir = f"c:/Users/{user}/AuraOS"
    if not os.path.exists(base_dir):
        os.mkdir(base_dir)

    root = tk.Tk()
    root.title("AuraOS")
    root.geometry("500x500")
    root.configure(bg="#000000")
    text_box = tk.Text(root, bg="#000000", fg="#FFFFFF")
    text_box.place(x=0, y=0, width=500, height=500)

    dir = base_dir  # persistent directory

    def block_edit(event):
        if "ro" in text_box.tag_names("insert"):
            return "break"

    def on_enter(event):
        nonlocal dir
        line_start = text_box.index("insert linestart")
        line_end = text_box.index("insert lineend")
        typed_text = text_box.get(line_start, line_end).strip()

        if typed_text == "ls":
            final = "\n".join(os.listdir(dir))

        elif typed_text.startswith("file "):
            spl = typed_text.split(" ", 2)
            name = spl[1]
            content = spl[2] if len(spl) > 2 else ""
            with open(os.path.join(dir, name), "w") as f:
                f.write(content)
            final = f"file {name} created"

        elif typed_text.startswith("read "):
            name = typed_text.split(" ", 1)[1]
            with open(os.path.join(dir, name), "r") as f:
                final = f.read()

        elif typed_text.startswith("del "):
            name = typed_text.split(" ", 1)[1]
            os.remove(os.path.join(dir, name))
            final = f"file {name} deleted"

        elif typed_text.startswith("dir "):
            name = typed_text.split(" ", 1)[1]
            os.makedirs(os.path.join(dir, name), exist_ok=True)
            final = f"directory {name} created"

        elif typed_text.startswith("nav "):
            name = typed_text.split(" ", 1)[1]
            new_dir = os.path.join(dir, name).replace("\\", "/")
            if os.path.isdir(new_dir):
                dir = new_dir
                final = f"navigated to {dir}"
            else:
                final = f"directory {name} not found"

        else:
            final = typed_text

        text_box.insert("end", f"\n{final}\n", "ro")
        text_box.tag_add("ro", "end-3l", "end-1l")
        text_box.tag_config("ro", foreground="gray")
        return "break"

    text_box.tag_add("ro", "1.0", "1.end")
    text_box.tag_config("ro", foreground="gray")
    text_box.bind("<Key>", block_edit)
    text_box.bind("<Return>", on_enter)
    root.mainloop()


if __name__ == "__main__":
    main()
