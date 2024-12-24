from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter as tk


class ChatBot:
    def __init__(self, root):
        self.root = root
        self.root.title("ChatBot")
        self.root.geometry("730x620+0+0")
        self.root.bind('<Return>', self.enter_func)

       
        main_frame = Frame(self.root, bd=4, bg='powder blue', width=730, height=100)
        main_frame.pack(fill=BOTH, expand=True)

        
        img_chat = Image.open('chat.jpg')
        img_chat = img_chat.resize((200, 70), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img_chat)

        Title_label = Label(
            main_frame, bd=3, relief=RAISED, anchor='nw', width=730,
            compound=LEFT, image=self.photoimg, text='CHAT ME',
            font=('arial', 30, 'bold'), fg='blue', bg='pink'
        )
        Title_label.pack(side=TOP, fill=X)

        
        self.scroll_y = ttk.Scrollbar(main_frame, orient=VERTICAL)
        self.text = Text(main_frame, width=65, height=20, bd=3, relief=RAISED,
                         font=('arial', 14), yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.scroll_y.config(command=self.text.yview)
        self.text.pack()

        
        btn_frame = Frame(self.root, bd=4, bg='pink', width=730, height=100)
        btn_frame.pack()

        label_1 = Label(btn_frame, text="Type Something", font=('arial', 14, 'bold'),
                        fg='green', bg='white')
        label_1.grid(row=0, column=0, padx=5, sticky=W)

        self.entry = StringVar()
        self.entry1 = ttk.Entry(btn_frame, textvariable=self.entry, width=40,
                                font=('times new roman', 16, 'bold'))
        self.entry1.grid(row=0, column=1, padx=5, sticky=W)

        self.send = Button(btn_frame, text="Send>>", command=self.send,
                           font=('arial', 15, 'bold'), width=8, bg='green')
        self.send.grid(row=0, column=2, padx=5, sticky=W)

        self.clear = Button(btn_frame, text="Clear Data", command=self.clear,
                            font=('arial', 15, 'bold'), width=8, bg='red', fg='white')
        self.clear.grid(row=1, column=0, padx=5, sticky=W)

        self.msg = ''
        self.label_11 = Label(btn_frame, text=self.msg, font=('arial', 14, 'bold'),
                              fg='red', bg='white')
        self.label_11.grid(row=1, column=1, padx=5, sticky=W)

    def enter_func(self, event):
        """Handles the Enter key press to send the message."""
        self.send.invoke()
        self.entry.set('')

    def clear(self):
        """Clears the chat window and entry field."""
        self.text.delete('1.0', END)
        self.entry.set('')

    def send(self):
        """Handles sending messages."""
        user_input = self.entry.get().strip()
        send_message = '\t\t\t' + 'You: ' + user_input
        self.text.insert(END, '\n' + send_message)
        self.text.yview(END)

        
        if user_input == '':
            self.msg = 'Please enter some input'
            self.label_11.config(text=self.msg, fg='red')
            return
        else:
            self.msg = ''
            self.label_11.config(text=self.msg, fg='red')

        
        bot_response = self.get_response(user_input.lower())
        self.text.insert(END, '\n\n' + 'Bot: ' + bot_response)
        self.text.yview(END)
        self.entry.set('')  

    def get_response(self, user_input):
        """Generates bot responses based on user input."""
        responses = {
            'hello': 'Hi, how can I assist you?',
            'who created you': 'I was created by AI.',
            'how are you': 'I am doing well, thank you!',
            'what is software': 'Software is a set of instructions for computers.',
            'what is chatbot': 'A chatbot is an AI-based tool that interacts with humans.',
            'thank you, bye': 'It was nice chatting with you. Have a great day! Bye!',
        }
        return responses.get(user_input, 'Sorry, I did not understand that.')


if __name__ == "__main__":
    root = tk.Tk()
    obj = ChatBot(root)
    root.mainloop()
