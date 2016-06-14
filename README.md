# simplempv

## Basic usage

```
$ mpv --input-ipc-server /path/to/sockfile
```

```python
from simplempv import Mpv
mpv = Mpv('/path/to/sockfile')

# General form
mpv.[command]([args, ...])

# Examples
mpv.seek(42, 'absolute') # Go to 42th second of the video
mpv.seek(42) # Go to t + 42 secs
mpv.stop()   # Stop playback
mpv.loadfile('/path/to/media') # Load a file and play it
```

List of input commands: https://mpv.io/manual/stable/#list-of-input-commands

Names containing hyphen must be written with an underscore instead:

```python
# Mpv name: playlist-next
mpv.playlist_next()
```

