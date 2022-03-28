# cosmos-tour-website

The guide you know and love, now in static website format powered by the sheer awesomeness of [Mkdocs](https://www.mkdocs.org/).

Building is not automated on push to save contributors from countless headaches caused by merge conflicts. Ideally this directory would be hosted on its own repo (with a [repository dispatch event action set up in this one](https://github.community/t/triggering-by-other-repository/16163) to facilitate autobuilds) <sup>but who's gonna do that for no extra credit?</sup>

## Requirements

 - computer
 - Python >= 3.6
 - requirements.txt

## Build

```
mkdocs build
```

okthxbai 
