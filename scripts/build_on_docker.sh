#!/bin/bash
# update must be done first or it doesn't know anything about any package
apt-get update
# because tzdata is interactive
export DEBIAN_FRONTEND=noninteractive
apt-get -y install tzdata
# base tools; the build's own dependencies (lilypond, tidy, ...) are
# installed by rsconstruct below from [dependencies] in rsconstruct.toml,
# so that knowledge lives in exactly one place
apt-get install -y python3 git curl
# get the rsconstruct build tool
curl -L -o /usr/local/bin/rsconstruct \
	https://github.com/veltzer/rsconstruct/releases/latest/download/rsconstruct-linux-x86_64
chmod +x /usr/local/bin/rsconstruct
# install the project's machine dependencies (lilypond etc.)
rsconstruct tool install machine
# install the project's locked uv, create the python environment (.venv)
# with it from pyproject.toml + uv.lock, and install the project's other
# locked tools; rsconstruct puts .venv/bin on PATH itself
rsconstruct tool install project
# build the books (renders the songs and engraves the five books)
rsconstruct build
# build every tune individually as well (the song generators scan the
# rendered songs, so this must come after the plain build above)
rsconstruct build \
	--iset generator.songs_pdf.enabled=true \
	--iset generator.songs_ps.enabled=true \
	--iset generator.songs_midi.enabled=true
