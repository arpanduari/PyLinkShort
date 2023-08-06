import tkinter as tk
import pyperclip
import pyshorteners
import ttkbootstrap as ttk
import ttkbootstrap.dialogs.dialogs as msg
from functools import partial


class LinkShortener:
    def __init__(self):
        # Window
        self.window = ttk.Window(themename='cyborg')
        self.window.resizable(False, False)
        self.window.title('PyLinkShort')
        self.window.geometry('700x450')
        # Widgets
        self.input_label = ttk.Label(
            master=self.window, text='Link Shortener', font='calibari 15 normal')
        self.input_label.pack()
        self.input_url_frame = ttk.Frame(self.window)
        self.input_label.pack()
        self.entry_url = tk.StringVar()
        self.shortener_btn = ttk.Button(
            master=self.input_url_frame, text='Short', command=self.short_link)

        self.entry = ttk.Entry(master=self.input_url_frame,
                               textvariable=self.entry_url, width=50)
        self.entry.focus()
        self.entry.pack(side='left', padx=10)
        self.shortener_btn.pack(side='left')
        self.input_url_frame.pack(pady=10)
        self.window.mainloop()

    def create_short_links(self, url):
        s = pyshorteners.Shortener()
        shorted_links_dict = {
            'tinyurl': s.tinyurl.short(url),
            'clckru': s.clckru.short(url),
            'dagd': s.dagd.short(url),
            'isgd': s.isgd.short(url),
            'osdb': s.osdb.short(url)
        }
        return shorted_links_dict

    def short_link(self):
        usr_url = self.entry_url.get()
        if len(usr_url) < 10:
            msg.Messagebox.show_info(
                'Hey this is not a valid url', 'Invalid URL')
        else:

            shorted_links_dict = self.create_short_links(usr_url)
            for service, value in shorted_links_dict.items():
                temp_frame = ttk.Frame(master=self.window)
                temp_frame.pack()
                service_label = ttk.Label(
                    master=temp_frame, text=f'{service} : {value}', font='Arial 12 normal')
                service_label.grid(row=0, column=0, pady=15, sticky='w')
                copy_btn = ttk.Button(
                    master=temp_frame, text='copy', command=partial(pyperclip.copy, value))
                copy_btn.grid(row=0, column=1, pady=15, padx=25, sticky='e')


linkshortener = LinkShortener()
