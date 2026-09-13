"""Regenerates README.md from this repository's published releases.

Run by .github/workflows/update-readme.yml whenever a release is published, edited or deleted.
The top section always shows the newest `smartide-eap-*` release; the table below lists the
latest five releases of every app, labelled by app, so older builds of a different app are not
mistaken for older versions of SmartIDE EAP.
"""
import json
import os
import urllib.request

REPO = os.environ.get("REPO", "SmartIDE-org/SmartIDE-release")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
ABIS = ["arm64-v8a", "armeabi-v7a", "x86_64", "x86", "universal"]
APPS = {"smartide-eap-": "SmartIDE EAP", "smartide-termux-": "SmartIDE Termux"}
ABI_NOTES = {
    "arm64-v8a": "most phones and tablets — pick this if unsure",
    "armeabi-v7a": "older 32-bit ARM devices",
    "x86_64": "Intel/AMD devices and emulators",
    "x86": "older 32-bit Intel devices",
    "universal": "works everywhere, largest download",
}


def fetch_releases():
    request = urllib.request.Request(
        f"https://api.github.com/repos/{REPO}/releases?per_page=100",
        headers={"Accept": "application/vnd.github+json", **({"Authorization": f"Bearer {TOKEN}"} if TOKEN else {})},
    )
    with urllib.request.urlopen(request) as response:
        releases = json.load(response)
    releases = [release for release in releases if not release["draft"]]
    releases.sort(key=lambda release: release["published_at"], reverse=True)
    return releases


def app(release):
    return next((name for prefix, name in APPS.items() if release["tag_name"].startswith(prefix)), release["tag_name"])


def version(release):
    for prefix in APPS:
        if release["tag_name"].startswith(prefix):
            return release["tag_name"][len(prefix):]
    return release["tag_name"]


def mb(size):
    return f"{size / 1_000_000:.0f} MB"


def asset(release, abi):
    return next((a for a in release["assets"] if a["name"].endswith(f"_{abi}.apk")), None)


def render(releases):
    eap = next((release for release in releases if release["tag_name"].startswith("smartide-eap-")), None)
    top = ""
    if eap:
        lines = []
        for abi in ABIS:
            a = asset(eap, abi)
            if a:
                lines.append(f"| **[{abi}]({a['browser_download_url']})** | {mb(a['size'])} | {ABI_NOTES[abi]} |")
        top = f"""## Download SmartIDE EAP

**Latest: [{version(eap)}]({eap['html_url']})**, published {eap['published_at'][:10]}.

| APK | Size | For |
|---|---|---|
{chr(10).join(lines)}

SmartIDE EAP (`org.smartide.code.eap`) is the early-access build of SmartIDE. It installs alongside the Play Store app and keeps its own data.

"""
    rows = []
    for release in releases[:5]:
        cells = []
        for abi in ABIS:
            a = asset(release, abi)
            cells.append(f"[{mb(a['size'])}]({a['browser_download_url']})" if a else "—")
        rows.append(f"| {app(release)} | [{version(release)}]({release['html_url']}) | {release['published_at'][:10]} | " + " | ".join(cells) + " |")
    return f"""# SmartIDE-release
This repo is for publishing SmartIDE APKs.

{top}## All recent releases

The latest five releases of every app published here. **SmartIDE EAP** and **SmartIDE Termux** are different apps, not versions of one another.

| App | Version | Published | arm64-v8a | armeabi-v7a | x86_64 | x86 | universal |
|---|---|---|---|---|---|---|---|
{chr(10).join(rows)}

See [all releases](https://github.com/{REPO}/releases).
"""


if __name__ == "__main__":
    with open("README.md", "w", encoding="utf-8") as readme:
        readme.write(render(fetch_releases()))
