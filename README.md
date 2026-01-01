# Password Manager 🔐

A simple, secure, and user-friendly password manager built with Python and Tkinter. This application helps you generate strong passwords and securely store your credentials locally.

![Password Manager Logo](logo.png)

## ✨ Features

- **Strong Password Generation**: Automatically generates secure passwords with a mix of:
  - Uppercase and lowercase letters
  - Numbers
  - Special symbols
  - Random length between 12-18 characters for maximum security

- **Password Storage**: Save website credentials locally in an organized format
- **Clipboard Integration**: Generated passwords are automatically copied to clipboard
- **User-Friendly GUI**: Clean and intuitive interface built with Tkinter
- **Input Validation**: Ensures all fields are filled before saving
- **Confirmation Prompts**: Asks for confirmation before saving credentials

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system
- Tkinter (usually comes pre-installed with Python)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/arvie993/Password-Manager.git
cd Password-Manager
```

2. Run the application:
```bash
python main.py
```

Or on some systems:
```bash
python3 main.py
```

## 📖 Usage

1. **Launch the Application**: Run `python main.py` to start the password manager

2. **Enter Website Details**:
   - Enter the website name/URL in the "Website" field
   - Enter your email/username (default email is pre-filled for convenience)
   - Either generate a password or enter your own

3. **Generate a Strong Password**:
   - Click the "Generate Password" button
   - A secure password will be created and automatically copied to your clipboard
   - The password will appear in the password field

4. **Save Your Credentials**:
   - Click the "Add" button
   - Confirm the details in the popup dialog
   - Your credentials will be saved to `passwords.txt`

5. **View Saved Passwords**:
   - Open `passwords.txt` to view all your saved credentials
   - Format: `Website | Email | Password`

## 🔒 Security Considerations

- **Local Storage**: All passwords are stored locally in `passwords.txt`
- **Plain Text Storage**: Currently, passwords are stored in plain text. For production use, consider implementing encryption
- **Backup**: Regularly backup your `passwords.txt` file
- **File Permissions**: Ensure `passwords.txt` has appropriate file permissions to prevent unauthorized access

## 📁 File Structure

```
Password-Manager/
├── main.py           # Main application file
├── logo.png          # Application logo
├── passwords.txt     # Stored credentials (created after first save)
├── .gitignore        # Git ignore file
└── README.md         # This file
```

## 🛠️ Technical Details

- **Language**: Python 3.x
- **GUI Framework**: Tkinter
- **Dependencies**: Standard Python libraries only (no external packages required)

## 🤝 Contributing

Contributions are welcome! Here are some ways you can contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

### Ideas for Improvements

- Add password encryption for secure storage
- Implement search functionality to find saved passwords
- Add password strength indicator
- Create a master password for app access
- Add edit and delete functionality for saved passwords
- Export/import functionality for backups
- Dark mode support

## 📝 License

This project is open source and available for personal use and modification.

## 👤 Author

**arvie993**

- GitHub: [@arvie993](https://github.com/arvie993)
- Email: arv993@gmail.com

## 🙏 Acknowledgments

- Built as a learning project to understand GUI development with Tkinter
- Inspired by the need for a simple, local password management solution

---

**⚠️ Disclaimer**: This is a basic password manager designed for learning purposes. For sensitive production use, consider using established password managers with proper encryption and security features.
