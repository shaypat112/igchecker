# igchecker

Built By Shivang Patel and Safe To Use

A simple Python script that shows which Instagram accounts you follow that don't follow you back.

This tool uses your downloaded Instagram data. It never asks for your password or logs into your account.

## Requirements

- Python 3
- Your Instagram followers and following data (JSON format)

## Installation

Download this repository:

```bash
git clone https://github.com/YOUR-USERNAME/igchecker.git
cd igchecker
```

Or click **Code → Download ZIP** on GitHub and extract the folder.

## Get Your Instagram Data

1. Open Instagram
2. Go to **Settings**
3. Open **Accounts Center**
4. Select **Your information and permissions**
5. Click **Download your information**
6. Choose **Followers and following**
7. Select **JSON** as the format
8. Download and unzip the archive

Inside the download, find these files:

```text
followers_1.json
following.json
```

Move both files into the project folder so it looks like:

```text
igchecker/
├── checker.py
├── followers_1.json
└── following.json
```

## Run

Open a terminal inside the project folder and run:

```bash
python3 checker.py
```

The script will print every account you follow that doesn't follow you back.

## Privacy

Your Instagram data never leaves your computer. Everything is processed locally.

## Disclaimer

This project is not affiliated with or endorsed by Instagram or Meta.