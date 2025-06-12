# Data Analysis Project Setup Guide

This guide will help you set up and run the project on both **Windows** and **Mac**. It includes steps for complete beginners who may not have Git or Python installed.

---

## 1. Prerequisites

### For Beginners (First-Time Setup)

#### Install Git
- **Windows:**
  1. Download from [git-scm.com](https://git-scm.com/download/win) and run the installer.
  2. Follow the default options.
- **Mac:**
  1. Open Terminal and run: `xcode-select --install` (or install from [git-scm.com](https://git-scm.com/download/mac))

#### Install Python 3.11+
- **Windows:**
  1. Download from [python.org](https://www.python.org/downloads/windows/).
  2. Run the installer. **Check the box that says "Add Python to PATH"**.
- **Mac:**
  1. Open Terminal and run: `brew install python` (if you have [Homebrew](https://brew.sh/)), or download from [python.org](https://www.python.org/downloads/mac-osx/).

#### Install pip (Python package manager)
- Usually comes with Python. To check, run: `pip --version`

#### (Optional but recommended) Install a code editor
- [Visual Studio Code](https://code.visualstudio.com/)

---

## 2. Clone the Project

Open Terminal (Mac) or Command Prompt (Windows) and run:

```sh
git clone <your-repo-url>
cd data-analysis
```

---

## 3. Set Up a Virtual Environment

### Windows
```sh
python -m venv .venv
.venv\Scripts\activate
```

### Mac
```sh
python3 -m venv .venv
source .venv/bin/activate
```

---

## 4. Install Dependencies

With the virtual environment activated, run:

```sh
pip install -r requirements.txt
```

---

## 5. Run the Project

The entry file is `main.py`. To start the project, run:

### Windows
```sh
uv run main.py
```

### Mac
```sh
uv run main.py
```

If you do not have `uv` installed, install it with:
```sh
pip install uv
```

---

## 6. Open the App

After running the command above, the app will start. Open your browser and go to the address shown in the terminal (usually [http://127.0.0.1:8050](http://127.0.0.1:8050)).

---

## 7. Common Issues
- If you get a `ModuleNotFoundError`, make sure you activated your virtual environment and installed all dependencies.
- If you have permission errors, try running your terminal as administrator (Windows) or use `sudo` (Mac, only if needed).

---

## 8. Useful Commands
- Deactivate virtual environment: `deactivate`
- Update dependencies: `pip install --upgrade -r requirements.txt`
- Check Python version: `python --version` or `python3 --version`

---

## 9. Resources
- [Git Documentation](https://git-scm.com/doc)
- [Python Documentation](https://docs.python.org/3/)
- [VS Code Documentation](https://code.visualstudio.com/docs)

---

**If you have any issues, please ask your team for help!**
