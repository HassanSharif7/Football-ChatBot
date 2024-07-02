from tkinter import *
from FootballBot import get_response, bot_name

BG_COLOR = "#4CAF50"  # Football field green
TEXT_COLOR = "#FFFFFF"  # White text for visibility
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

class ChatApplication:

    def __init__(self):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("Football Chat")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=600, height=550, bg=BG_COLOR)  # Increased width to 600

        # Head label
        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                           text="Football Chat", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)

        # Tiny divider line
        line = Label(self.window, width=550, bg=TEXT_COLOR)  # Adjusted width to match new window width
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        # Text widget for displaying chat messages
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR,
                                font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # Scrollbar for the text widget
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)

        # Bottom label (placeholder)
        bottom_label = Label(self.window, bg=BG_COLOR, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        # Message entry box
        self.msg_entry = Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        # Send button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=TEXT_COLOR,
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

        # Football icon (example)
        try:
            football_icon = PhotoImage(file='football_icon.png')
            icon_label = Label(self.window, image=football_icon, bg=BG_COLOR)
            icon_label.place(relx=0.8, rely=0.01)
        except Exception as e:
            print(f"Failed to load football icon: {e}")

    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")

    def _insert_message(self, msg, sender):
        if not msg:
            return

        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        msg2 = f"{bot_name}: {get_response(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)

if __name__ == "__main__":
    app = ChatApplication()
    app.run()
