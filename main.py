import tkinter as tk


def main():

    root = tk.Tk()
    root.title("AuraOS")
    root.geometry("500x500")
    root.configure(bg="#000000")  # Set the
    text_box = tk.Text(root, bg="#000000", fg="#FFFFFF")
    text_box.place(x=0, y=0, width=500, height=500)
    text_box.insert("end", "Read-only: ", "ro")
    text_box.insert("end", "you can type here\n")

    # make only the "ro" tag read-only
    def block_edit(event):
        # if cursor inside read-only tag, block keypress
        if "ro" in text_box.tag_names("insert"):
            return "break"

    def on_enter(event):
        # insert text and make it read-only
        line_start = text_box.index("insert linestart")
        line_end = text_box.index("insert lineend")
        typed_text = text_box.get(line_start, line_end)
        text_box.insert(
            "end",
            f"\n{typed_text if not typed_text == "ls" or "file" else "wsggg"}",
            "ro",
        )
        text_box.tag_add("ro", "end-3l", "end-1l")  # tag last 2 lines as read-only
        text_box.tag_config("ro", foreground="gray")
        return "break"  # optional: stop newline from being added

    text_box.tag_add("ro", "1.0", "1.end")
    text_box.tag_config("ro", foreground="gray")
    text_box.bind("<Key>", lambda event: block_edit(event))
    text_box.bind("<Return>", on_enter)
    root.mainloop()


if __name__ == "__main__":
    main()
