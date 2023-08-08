###installation
```bash
KOMMENTAR: Endre til requirements.txt, da uten .txt ikke fungerte på ifi-maskinen
$ pip install -r requirements.txt
$ pip install .
```

###Usage
```bash
$ instapy -h
$ instapy -f path/to/image.jpg -se -o output.jpg
```

###Testing
```bash
python -m pytest
```