#!/usr/bin/env sh

set -e

update_dir="${HOME}/Library/Application Support/Spotify/PersistentCache/Update"

echo "Killing Spotify"
killall -q Spotify || true

echo "Unlocking update directory"
chflags nouchg "${update_dir}"

echo "Done"
