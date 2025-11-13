
# 📝 Simple Python To-Do App

This is a **basic yet fully functional To-Do List application** built using **Python and Tkinter**.  
It allows you to **add, delete, and mark tasks as done**, with all tasks saved automatically in a local JSON file.  
The app works seamlessly on both **Windows** and **Linux (Ubuntu)** systems.

---

## 🧩 Prerequisites

Before setting up, make sure you have:

- **Python 3**
- **pip**
- **venv**
- **Git (for Windows setup)**

> ⚠️ **Note:**  
> - On **Linux**, Python usually comes pre-installed.  
> - If Python is already installed, **no need to reinstall** — just verify using the version commands below.  
> - Python command can vary by device (`python`, `python3`, or `py`).

---

### 🧠 Check if Python, pip, and venv are installed

#### 🪟 On Windows:
Open Command Prompt and run:
```bash
python --version
pip --version
python -m venv --help
````

#### 🐧 On Linux:

Open Terminal and run:

```bash
python3 --version
pip3 --version
python3 -m venv --help
```

If all show version numbers or help messages, you’re good to go ✅
If not, follow the installation steps below.

---

## ⚙️ Installation (If Not Installed)

### 🪟 On Windows

Download and install Python from:
👉 [https://www.python.org/downloads/](https://www.python.org/downloads/)

During setup:

* ✅ Check **“Add Python to PATH”**
* ✅ Choose **“Install pip”** (default)
* ✅ Choose **“Install venv”** (default)

---

### 🐧 On Linux (Ubuntu/Debian)

If Python is missing or outdated, install it with these commands:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3
sudo apt install python3-pip
sudo apt install python3.10-venv
```

> You can verify installation again with:
>
> ```bash
> python3 --version
> pip3 --version
> ```

---

## 🪟 Windows Setup Instructions

### 1️⃣ Clone the Repository

```bash
cd C:\
git clone https://github.com/prathmesh-ghatmal/simplepythonapp.git
cd simplepythonapp
```

---

### 2️⃣ Create and Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Project Requirements

If a `requirements.txt` file is present, run:

```bash
pip install -r requirements.txt
```

> This To-Do app uses only built-in Python libraries (`tkinter`, `json`, `os`),
> so no external dependencies are required.

---

### 4️⃣ Run the Application

```bash
python main.py
```

*(Use `py main.py` if `python` command doesn’t work.)*

---

## 🐧 Linux (Ubuntu) Setup Instructions

> You don’t need to clone again in Linux.
> The project will be **migrated from Windows** using **FileZilla** or another SFTP tool.

### 1️⃣ Transfer the Project Folder

From Windows, move your project folder (e.g., `simplepythonapp`) to:

```
/home/imcc/simplepythonapp
```

using **FileZilla**.

---

### 2️⃣ Navigate to the Project Directory

```bash
cd /home/imcc/simplepythonapp
```

---

### 3️⃣ Create and Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---
Install Tkinter  manually:

```bash
sudo apt install python3-tk
```

---

### 5️⃣ Run the Application

```bash
python3 main.py
```

---

## 💡 Notes

* Python command can differ depending on OS:
  Try `python`, `python3`, or `py` if one doesn’t work.
* Your tasks will be saved automatically in `tasks.json`.
* No database or internet connection required — works completely offline.

---

## 🧠 Author

**Prathmesh Ghatmal**
[GitHub Profile](https://github.com/prathmesh-ghatmal)

---

## 📜 License

This project is open-source and free to use for educational purposes.




