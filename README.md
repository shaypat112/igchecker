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

Inside the download, find these two files and copy them into this project folder:

```text
followers_1.json
following.json
```

Your folder should look like this:

```text
igchecker/
├── checker.py
├── followers_1.json
└── following.json
```

The script also reads these optional files when they are in the folder:

```text
blocked_profiles.json
hide_story_from.json
pending_follow_requests.json
recent_follow_requests.json
recently_unfollowed_profiles.json
removed_suggestions.json
```

They are included as separate sections in `relationship_report.txt`. They do not change the “doesn't follow you back” total, because they describe blocks, story privacy, follow requests, accounts you unfollowed, or suggestions—not accounts that currently follow you.

## Run

Open a terminal inside the project folder and run:

```bash
python3 checker.py
```

The script will print every account you follow that doesn't follow you back. It saves that list to `not_following_back.txt` and saves all available relationship categories to `relationship_report.txt`.

## Privacy

Your Instagram data never leaves your computer. Everything is processed locally.

## Disclaimer

This project is not affiliated with or endorsed by Instagram or Meta.
