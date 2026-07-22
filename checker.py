import json
from pathlib import Path


FOLLOWERS_FILE = Path("followers_1.json")
FOLLOWING_FILE = Path("following.json")
OUTPUT_FILE = Path("not_following_back.txt")
REPORT_FILE = Path("relationship_report.txt")

EXTRA_RELATIONSHIP_FILES = {
    "Blocked profiles": Path("blocked_profiles.json"),
    "Hidden from story": Path("hide_story_from.json"),
    "Pending follow requests": Path("pending_follow_requests.json"),
    "Recent follow requests": Path("recent_follow_requests.json"),
    "Recently unfollowed profiles": Path("recently_unfollowed_profiles.json"),
    "Removed suggestions": Path("removed_suggestions.json"),
}


def load_json(file_path: Path):
    """Open a JSON file and convert it into Python data."""
    try:
        with file_path.open("r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: Could not find {file_path.name}")
        print("Make sure it is in the same folder as checker.py.")
        raise SystemExit(1)
    except json.JSONDecodeError:
        print(f"Error: {file_path.name} is not valid JSON.")
        raise SystemExit(1)


def get_username(item: dict) -> str | None:
    """Read a username from Instagram's relationship-export formats."""
    # followers_1.json normally uses ``value``; following.json uses ``title``.
    string_list = item.get("string_list_data", [])
    if string_list:
        username = string_list[0].get("value")
        if isinstance(username, str) and username:
            return username.lower()

    username = item.get("title")
    if isinstance(username, str) and username:
        return username.lower()

    # Other relationship files in newer exports use label_values instead.
    for label_value in item.get("label_values", []):
        if label_value.get("label") == "Username":
            username = label_value.get("value")
            if isinstance(username, str) and username:
                return username.lower()

    return None


def extract_usernames(items: list[dict]) -> set[str]:
    """Extract usernames from a list of Instagram relationship entries."""
    usernames = set()
    for item in items:
        username = get_username(item)
        if username:
            usernames.add(username)
    return usernames


def extract_following(following_data) -> set[str]:
    """Extract usernames from following.json."""
    relationships = following_data.get("relationships_following", [])
    return extract_usernames(relationships)


def extract_followers(followers_data) -> set[str]:
    """Extract usernames from the single followers_1.json file."""
    if not isinstance(followers_data, list):
        print(f"Error: {FOLLOWERS_FILE.name} has an unexpected format.")
        raise SystemExit(1)
    return extract_usernames(followers_data)


def save_results(usernames: list[str]) -> None:
    """Save the usernames to a text file."""
    with OUTPUT_FILE.open("w", encoding="utf-8") as file:
        for username in usernames:
            file.write(f"{username}\n")


def load_optional_relationships() -> dict[str, set[str]]:
    """Load optional relationship lists that are present in this folder."""
    relationships = {}
    for label, file_path in EXTRA_RELATIONSHIP_FILES.items():
        if not file_path.exists():
            continue

        data = load_json(file_path)
        if not isinstance(data, list):
            print(f"Warning: Skipping {file_path.name}; it has an unexpected format.")
            continue
        relationships[label] = extract_usernames(data)
    return relationships


def save_relationship_report(
    not_following_back: list[str], extra_relationships: dict[str, set[str]]
) -> None:
    """Save the main result and every available extra relationship category."""
    with REPORT_FILE.open("w", encoding="utf-8") as file:
        file.write("Accounts you follow that do not follow you back\n")
        file.write("=" * 47 + "\n")
        file.write("\n".join(not_following_back) + "\n")

        for label, usernames in extra_relationships.items():
            file.write(f"\n{label} ({len(usernames)})\n")
            file.write("=" * (len(label) + len(str(len(usernames))) + 3) + "\n")
            file.write("\n".join(sorted(usernames)) + "\n")


def main() -> None:
    followers_data = load_json(FOLLOWERS_FILE)
    following_data = load_json(FOLLOWING_FILE)

    followers = extract_followers(followers_data)
    following = extract_following(following_data)
    extra_relationships = load_optional_relationships()

    not_following_back = sorted(following - followers)

    print(f"Followers: {len(followers)}")
    print(f"Following: {len(following)}")
    print(f"Not following you back: {len(not_following_back)}")
    for label, usernames in extra_relationships.items():
        print(f"{label}: {len(usernames)}")
    print()

    if not not_following_back:
        print("Everyone you follow also follows you back.")
    else:
        for username in not_following_back:
            print(username)

    save_results(not_following_back)
    save_relationship_report(not_following_back, extra_relationships)
    print(f"\nResults saved to {OUTPUT_FILE.name} and {REPORT_FILE.name}")


if __name__ == "__main__":
    main()
