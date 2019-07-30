#!/bin/sh

if [ -d .git/ ]; then
    if [ -f .git/hooks/post-merge ] && ! [ -z $(diff .git/hooks/post-merge hooks/post-merge) ]; then
        echo "Move your post-merge to something with the extension post-merge, e.g. something.post-merge. If this is an old version generated from this script, delete it."
        exit 1
    fi
    if [ -f .git/hooks/post-merge ] && ! [ -z $(diff .git/hooks/post-merge hooks/post-merge) ]; then
        echo "Move your pre-commit to something with the extension post-merge, e.g. something.post-merge. If this is an old version generated from this script, delete it."
        exit 1
    fi
    cp hooks/install-requirements.post-merge .git/hooks/install-requirements.post-merge
    cp hooks/post-merge .git/hooks/post-merge

    cp hooks/check-requirements.pre-commit .git/hooks/check-requirements.pre-commit
    cp hooks/pre-commit .git/hooks/pre-commit
else
    echo "Not in the root of git repo"
    exit 1
fi
