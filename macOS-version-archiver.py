#!/usr/bin/env python3

"""
macOS Spotify Version Archiver
Author: @lhvy
Date: 2022-05-23

This script is used to archive builds of Spotify for macOS. It works by doing the following:
1. Downloading and extracting the latest online installer
2. Extracting the version number and download links for the latest builds for each architecture
3. Checking if the latest build for each architecture is already downloaded
4. Downloading the latest builds into a new folder named after the version number

Why?
Spicetify is a great command line tool to customise Spotify.
Sadly it can break across different versions of Spotify, and downgrading Spotify requires access to old versions of Spotify.

TODO:
- Handle possible edge case where installer and build versions are different
- Windows support?
"""

import urllib.request
import zipfile
import plistlib
import os
from dotenv import load_dotenv

load_dotenv()

INSTALLER_URL = "https://download.scdn.co/SpotifyInstaller.zip"
DOWNLOAD_PATH = os.environ.get("SPOTIFY_DOWNLOAD_PATH", "~/SpotifyArchive")

# Ensure the local download path exists
DOWNLOAD_PATH = os.path.expanduser(DOWNLOAD_PATH)
os.makedirs(DOWNLOAD_PATH, exist_ok=True)

# Download the installer
try:
    installer = urllib.request.urlretrieve(INSTALLER_URL)
except urllib.error.HTTPError as e:
    print("HTTP error " + str(e.code) + " downloading installer: " + e.reason)
    exit(1)

# Unzip the installer
installer = zipfile.ZipFile(installer[0])

# Read the Info.plist
info = plistlib.load(installer.open("Install Spotify.app/Contents/Info.plist"))

version = info["CFBundleShortVersionString"]
urls = info["SpotifyDownloadURL"]

if os.path.exists(DOWNLOAD_PATH + "/" + version):
    # Version may have been downloaded, need to check file by file
    for key in list(urls):  # force a copy of the keys so we can mutate the dict
        filename = urls[key].split("/")[-1]
        if os.path.exists(DOWNLOAD_PATH + "/" + version + "/" + filename):
            print("Skipping " + filename)
            urls.pop(key)
else:
    os.makedirs(DOWNLOAD_PATH + "/" + version)

# Download the apps
for url in urls.values():
    try:
        try:
            urllib.request.urlretrieve(
                url,
                DOWNLOAD_PATH + "/" + version + "/" + url.split("/")[-1],
            )
        except urllib.error.HTTPError as e:
            # Don't exit, just skip the file as there may be others to download
            print(
                "HTTP error " + str(e.code) + " downloading " + url + " : " + e.reason
            )
            raise  # Raise error so we can clean up after ourselves regardless of the error type
    except:
        if os.path.exists(DOWNLOAD_PATH + "/" + version + "/" + url.split("/")[-1]):
            os.remove(DOWNLOAD_PATH + "/" + version + "/" + url.split("/")[-1])
