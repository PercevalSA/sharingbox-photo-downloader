# Sharingbox Pictures Downloader

download all files from the [Sharingbox Gallery](https://my.sharingbox.com) : photo and gif (actually mp4 video)

requires python 3.6 or newer

## Usage

Go to the gallery you want the pictures from and copy the following items :
 * The event ID (contained in the URL : idFTPevent) 
 * Your session cookie (PHPSESSID)
 * The number of pages of the album (you can see it directly on the first page)

Put those informations at the right places in the `dl_pictures.py` file.

then open a terminal :
```bash
pip3 install requests wget
python3 dl_pictures.py
```

you are done, your pictures are in the `pictures` folder.
