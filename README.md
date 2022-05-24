# spicetify-tools

A small collection of personal tools to for use with Spicetify

## macOS

### macOS-block-updates.sh

A shell script to block Spotify updates by locking the update folder. This script may need to be run for all users with edit access to the Spotify application.

```bash
curl -fsSL https://raw.githubusercontent.com/lhvy/spicetify-tools/master/macOS-block-updates.sh | sh
```

### macOS-unblock-updates.sh

A shell script to undo the process of the previous script.

```bash
curl -fsSL https://raw.githubusercontent.com/lhvy/spicetify-tools/master/macOS-unblock-updates.sh | sh
```

### macOS-version-archiver.py

A Python 3.x script which can be used to backup the current latest version of Spotify for both Intel and Apple Silicon. Running this script on regular intervals will allow for backing up each version of Spotify in order to easily upgrade and downgrade.
