from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    
    try:
        password_entry.delete(0, END)
        password_entry.insert(0, password)
        pyperclip.copy(password)
    except Exception as e:
        # Handle clipboard errors gracefully
        password_entry.delete(0, END)
        password_entry.insert(0, password)
        messagebox.showwarning(title="Clipboard Warning", 
                              message="Password generated but couldn't copy to clipboard.")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email": email,
        "password": password,
    }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            # Try to read existing data
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                if not isinstance(data, dict):
                    data = {}
        except (FileNotFoundError, json.JSONDecodeError):
            # If file doesn't exist or is corrupted, start fresh
            data = {}
        except (IOError, PermissionError) as e:
            messagebox.showerror(title="Error", message=f"Could not access data file: {str(e)}")
            return
        
        # Check if website already exists and ask for confirmation
        if website in data:
            is_ok = messagebox.askyesno(title="Website Exists", 
                                        message=f"Credentials for '{website}' already exist.\n"
                                               f"Do you want to override them?")
            if not is_ok:
                return
        
        try:
            # Update data with new entry and save
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        except (IOError, PermissionError, TypeError, KeyError) as e:
            messagebox.showerror(title="Error", message=f"Could not save data: {str(e)}")
            return
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def show_credentials_popup(website, email, password):
    """Custom popup with copy buttons for email and password"""
    popup = Toplevel(window)
    popup.title(website)
    popup.config(padx=20, pady=20)
    
    # Make popup modal and center it
    popup.transient(window)
    popup.grab_set()
    
    # Auto-copy password to clipboard on open
    try:
        pyperclip.copy(password)
    except Exception:
        pass
    
    # Email row
    Label(popup, text="Email:", font=('Arial', 10, 'bold')).grid(row=0, column=0, sticky='e', padx=5, pady=5)
    email_display = Entry(popup, width=30)
    email_display.grid(row=0, column=1, padx=5, pady=5)
    email_display.insert(0, email)
    email_display.config(state='readonly')
    
    def copy_email():
        try:
            pyperclip.copy(email)
            copy_email_btn.config(text="✓ Copied!")
            popup.after(1500, lambda: copy_email_btn.config(text="Copy"))
        except Exception:
            pass
    
    copy_email_btn = Button(popup, text="Copy", command=copy_email, width=8,
                           bg='#4CAF50', fg='white', relief='flat')
    copy_email_btn.grid(row=0, column=2, padx=5, pady=5)
    
    # Password row
    Label(popup, text="Password:", font=('Arial', 10, 'bold')).grid(row=1, column=0, sticky='e', padx=5, pady=5)
    password_display = Entry(popup, width=30)
    password_display.grid(row=1, column=1, padx=5, pady=5)
    password_display.insert(0, password)
    password_display.config(state='readonly')
    
    def copy_password():
        try:
            pyperclip.copy(password)
            copy_password_btn.config(text="✓ Copied!")
            popup.after(1500, lambda: copy_password_btn.config(text="Copy"))
        except Exception:
            pass
    
    copy_password_btn = Button(popup, text="Copy", command=copy_password, width=8,
                              bg='#4CAF50', fg='white', relief='flat')
    copy_password_btn.grid(row=1, column=2, padx=5, pady=5)
    
    # Status label
    status_label = Label(popup, text="✓ Password copied to clipboard!", fg='green', font=('Arial', 9))
    status_label.grid(row=2, column=0, columnspan=3, pady=(10, 5))
    
    # Close button
    close_btn = Button(popup, text="Close", command=popup.destroy, width=15,
                      bg='#2196F3', fg='white', relief='flat')
    close_btn.grid(row=3, column=0, columnspan=3, pady=10)
    
    # Center the popup on screen
    popup.update_idletasks()
    x = window.winfo_x() + (window.winfo_width() // 2) - (popup.winfo_width() // 2)
    y = window.winfo_y() + (window.winfo_height() // 2) - (popup.winfo_height() // 2)
    popup.geometry(f"+{x}+{y}")

def search():
    website = website_entry.get()
    
    if len(website) == 0:
        messagebox.showinfo(title="Oops", message="Please enter a website to search.")
        return
    
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found. Save a password first.")
        return
    except (json.JSONDecodeError, IOError, PermissionError) as e:
        messagebox.showerror(title="Error", message=f"Could not read data file: {str(e)}")
        return
    
    try:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            show_credentials_popup(website, email, password)
        else:
            messagebox.showinfo(title="Not Found", message=f"No details for '{website}' exist.")
    except (KeyError, TypeError) as e:
        messagebox.showerror(title="Error", message=f"Could not retrieve data: {str(e)}")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
try:
    logo_img = PhotoImage(file="logo.png")
    canvas.create_image(100, 100, image=logo_img)
except Exception as e:
    # If logo image is missing or corrupted, continue without it
    pass
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky='e')
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky='e')
password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky='e')

#Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1, sticky='ew', padx=5, pady=5)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky='ew', padx=5, pady=5)
email_entry.insert(0, "angela@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky='ew', padx=5, pady=5)

# Buttons
search_button = Button(text="Search", command=search,
                       highlightthickness=0, relief='flat',
                       bg='#4CAF50', fg='white', font=('Arial', 9, 'normal'))
search_button.grid(row=1, column=2, sticky='ew', padx=5, pady=5)
generate_password_button = Button(text="Generate Password", command=generate_password, 
                                   highlightthickness=0, relief='flat', 
                                   bg='#4CAF50', fg='white', font=('Arial', 9, 'normal'))
generate_password_button.grid(row=3, column=2, sticky='ew', padx=5, pady=5)
add_button = Button(text="Add", width=36, command=save,
                    highlightthickness=0, relief='flat',
                    bg='#2196F3', fg='white', font=('Arial', 9, 'normal'))
add_button.grid(row=4, column=1, columnspan=2, sticky='ew', padx=5, pady=5)

window.mainloop()