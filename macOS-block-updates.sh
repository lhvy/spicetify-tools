#!/usr/bin/env sh

set -e

update_dir="${HOME}/Library/Application Support/Spotify/PersistentCache/Update"

echo "Killing Spotify"
killall -q Spotify || true

echo "Deleting update directory"
rm -rf "${update_dir}"

echo "Creating empty update directory"
mkdir -p "${update_dir}"

echo "Locking update directory"
chflags uchg "${update_dir}"

echo "Done - Please note this script may need to be run for all users who have edit access to the Spotify app."
