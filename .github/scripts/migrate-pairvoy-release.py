"""Copy an existing public release to the website repository, verifying every asset."""
import hashlib
import json
import os
import re
import subprocess
from pathlib import Path
from tempfile import TemporaryDirectory
from urllib.request import urlopen

source = "ornbaumkeith/pairvoy-releases"
destination = "ornbaumkeith/ornbaumkeith.github.io"
if os.environ["GITHUB_REPOSITORY"] != destination:
    raise SystemExit("Unexpected destination repository")

tag = os.environ["PAIRVOY_TAG"]
manifest = json.loads(Path(".github/pairvoy-release-migration.json").read_text())
release, = (item for item in manifest if item["tag"] == tag)

def gh(*args, check=True):
    return subprocess.run(["gh", *args, "--repo", destination], check=check,
                          text=True, capture_output=True)

with TemporaryDirectory() as directory:
    work = Path(directory)
    notes = work / "notes.md"
    notes.write_text(release["notes"].replace(
        "https://github.com/" + source + "/releases/",
        "https://github.com/" + destination + "/releases/"), encoding="utf-8")
    for asset in release["assets"]:
        name = asset["name"]
        if not re.fullmatch(r"[A-Za-z0-9._-]+", name) or name in (".", ".."):
            raise SystemExit("Unexpected asset name")
        url = f"https://github.com/{source}/releases/download/{tag}/{name}"
        digest = hashlib.sha256()
        size = 0
        with urlopen(url, timeout=90) as response, (work / name).open("wb") as output:
            while chunk := response.read(1024 * 1024):
                size += len(chunk)
                if size > asset["size"]:
                    raise SystemExit(f"Asset exceeded its recorded size: {name}")
                digest.update(chunk)
                output.write(chunk)
        if size != asset["size"] or "sha256:" + digest.hexdigest() != asset["digest"]:
            raise SystemExit(f"Public source asset failed verification: {name}")

    endpoint = f"repos/{destination}/releases/tags/{tag}"
    api = lambda: subprocess.run(["gh", "api", endpoint], text=True, capture_output=True)
    existing = api()
    if existing.returncode != 0:
        if "HTTP 404" not in existing.stderr:
            raise SystemExit(existing.stderr)
        gh("release", "create", tag, "--draft", "--target", os.environ["GITHUB_SHA"],
           "--title", release["title"], "--notes-file", str(notes), "--prerelease", "--latest=false")
        existing = api()
        if existing.returncode != 0:
            # The tag endpoint may omit draft releases. Match its tag in the release listing.
            listing = subprocess.check_output(["gh", "api", f"repos/{destination}/releases",
                                               "--paginate", "--slurp"], text=True)
            current, = (item for page in json.loads(listing) for item in page if item["tag_name"] == tag)
        else:
            current = json.loads(existing.stdout)
    else:
        current = json.loads(existing.stdout)

    present = {asset["name"]: asset for asset in current["assets"]}
    for asset in release["assets"]:
        name = asset["name"]
        if name in present:
            if present[name]["digest"] != asset["digest"] or present[name]["size"] != asset["size"]:
                raise SystemExit(f"Destination already has a different asset named {name}")
        else:
            gh("release", "upload", tag, str(work / name))
    gh("release", "edit", tag, "--draft=false", "--prerelease", "--latest=false")
    print(f"Migrated and checked {len(release['assets'])} assets for {tag}.")
