# autoElevate Hunter

This Python3 script was created to assist with fileless UAC bypass research. It searches for PE files and checks whether the `.manifest` section contains `<autoElevate>true</autoElevate>`, indicating that the executable might be useful for certain UAC bypass techniques. I'll leave the actual exploitation as an exercise for the reader.

There are no external dependencies (sigcheck, etc) or fancy PE parsing, which makes this tool surprisingly fast.

## Installation

```
git clone https://github.com/disasterbyte/aehunter
```

### Usage

```
usage: aehunter.py [-h] (-d  | -f ) [-r] [-o]

optional arguments:
  -h, --help         show this help message and exit
  -d, --directory    directory to search
  -f, --file         file to check
  -r, --recursive    recursively search directory
  -o, --output       write output to file
```
