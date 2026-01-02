# 🔐 MyPass - Password Manager

A simple, secure desktop password manager built with Python and Tkinter.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📸 Screenshot

<p align="center">
  <img src="logo.png" alt="MyPass Logo" width="150">
</p>

## ✨ Features

- **🔑 Password Generator**: Generate strong, random passwords with letters, numbers, and symbols
- **💾 Save Credentials**: Store website credentials securely in a local JSON file
- **🔍 Search Function**: Quickly find saved passwords by website name
- **📋 One-Click Copy**: Custom popup with dedicated copy buttons for email and password
- **✨ Auto-Copy**: Password is automatically copied to clipboard when searched
- **⚠️ Duplicate Warning**: Warns before overwriting existing credentials
- **🛡️ Error Handling**: Comprehensive exception handling for a robust experience

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/arvie993/Password-Manager.git
   cd Password-Manager
   ```

2. **Install dependencies**
   ```bash
   pip install pyperclip
   ```
   
   Or using Poetry:
   ```bash
   poetry install
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

## 📖 Usage

### Adding a New Password

1. Enter the website name
2. Enter your email/username (default email is pre-filled)
3. Click **Generate Password** or enter your own password
4. Click **Add** to save

### Searching for a Password

1. Enter the website name
2. Click **Search**
3. A custom popup appears with:
   - Email and password displayed in read-only fields
   - **Copy** buttons next to each field for one-click copying
   - Password is auto-copied to clipboard on popup open
   - Visual feedback ("✓ Copied!") when you click copy

### Generating a Password

- Click **Generate Password** to create a random, secure password
- The password is automatically copied to your clipboard

## 📁 Project Structure

```
Password-Manager/
├── main.py           # Main application code
├── logo.png          # Application logo
├── data.json         # Stored passwords (auto-generated, gitignored)
├── pyproject.toml    # Poetry configuration
├── .gitignore        # Git ignore file
└── README.md         # This file
```

## 🔒 Security Notes

- **Local Storage**: All passwords are stored locally in `data.json`
- **No Encryption**: Passwords are stored in plain text - this is a learning project
- **gitignored**: The `data.json` file is excluded from version control
- **For Production**: Consider adding encryption (e.g., using `cryptography` library)

## 🛠️ Technologies Used

- **Python 3.8+** - Programming language
- **Tkinter** - GUI framework
- **JSON** - Data storage format
- **Pyperclip** - Clipboard functionality

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Built as part of the 100 Days of Code Python challenge
- Inspired by Angela Yu's Python course on Udemy

---

<p align="center">Made with ❤️ and Python</p>
