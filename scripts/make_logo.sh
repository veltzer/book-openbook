#!/bin/bash -eu
# Regenerate the derived logo files from the master images/logo.svg:
#   images/logo.eps   - embedded on the title page of the books (lilypond reads eps, not svg)
#   docs/logo.svg     - the website logo and svg favicon
#   docs/favicon.ico  - 16/32/48 pixel favicon for browsers without svg favicon support
# Needs rsvg-convert and ImageMagick. Run from the repository root.
src="images/logo.svg"
rsvg-convert -f eps -w 512 -o images/logo.eps "${src}"
cp "${src}" docs/logo.svg
tmp=$(mktemp -d)
trap 'rm -rf "${tmp}"' EXIT
for size in 16 32 48; do
	rsvg-convert -w "${size}" -h "${size}" -o "${tmp}/${size}.png" "${src}"
done
magick "${tmp}/16.png" "${tmp}/32.png" "${tmp}/48.png" docs/favicon.ico
