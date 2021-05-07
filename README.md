# mediapy

mediapy is a Python library for simple frame-/video-editing. See summary section of docs for full list of functionalities.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install mediapy
```

## Usage

```python
from mediapy.frames import Frames

pathInput  = "~/Videos/video1.avi"
pathOutput = "~/Videos/video1.avi"

## Extract individual frames & add overlays per frame
## then combine them again.
vid2 = Frames(pathInput, pathOutput)
vid2.overlayVideo()
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)