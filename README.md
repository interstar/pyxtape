# pyxtape

Make "mixtapes" with Python, sox and avconv

## Why?

I wanted to sequence a bunch of mp3s and other audio files together into a single mixed file. Without using awkward DJing software of even something as heavy as Audacity. A mix is a sequence of music with short cross-fades between each one. There's no attempt at beat-matching or other clever synchronization, but you can determine how much of a cross-fade you end up with.

## Workflow

1) I use [Totem](https://wiki.gnome.org/Apps/Videos), the GNOME desktop movie player, to collect a playlist which I can then export as a .pls file. (Other applications seem to support the .pls format too.)

The playlist file contains the full path to the music files. 

2)

    python makelist.py MYPLAYLIST.pls "1,1,2,3,5,8,13"
    
makelist reads the playlist file (MYPLAYLIST.pls) and then calls avconv and sox (make sure you have them installed on your machine) via the included [crossfade_cat.sh](https://github.com/jacksonh/sox/blob/master/scripts/crossfade_cat.sh) shell-script (originally from the sox site).

The second argument to makelist.py, is a string containing a list of numbers separated by commas. These are the time (in seconds) for the cross-fade between each track.

3) When finished (note, the process can take a long time), your tracks will have been colated into a file called mix.wav in your directory.


