import subprocess

def get_commit_messages():
    result = subprocess.run(['git', 'log', '--pretty=format:%s', 'HEAD^1..HEAD'], capture_output=True, text=True)
    return result.stdout.split('\n')

def generate_release_notes():
    commits = get_commit_messages()
    release_notes = "# Release Notes\n\n"
    for commit in commits:
        release_notes += f"- {commit}\n"
    return release_notes

if __name__ == "__main__":
    notes = generate_release_notes()
    with open("RELEASE_NOTES.md", "w") as file:
        file.write(notes)
    print("Release notes generated in RELEASE_NOTES.md")