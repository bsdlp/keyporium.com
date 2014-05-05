# keyporium.com

website source.

### Git-Hook:

For `ghp-import` magic, create `.git/hooks/post-push`:

```
#!/usr/bin/env bash

_COMMIT_HASH=$(git rev-parse HEAD)
_COMMIT_MSG=$(git cat-file commit ${_COMMIT_HASH} | sed '1,/^$/d')
pelican content -o output -s pelicanconf.py && \
    ghp-import -n -m "${_COMMIT_MSG}" output && \
    git push origin gh-pages
```
