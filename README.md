# Image Resizer
## Installation
Install Pillow.
```pip install -r requirements.txt```

It is better to use virtual enviroments

## How to use
```python3 image_resize.py --help```
will show options.
```
positional arguments:
  original_path    original image's path

optional arguments:
  -h, --help       show this help message and exit
  --width WIDTH    width of output image
  --height HEIGHT  height of output image
  --scale SCALE    scale of output image. Don't use --width or --heightif you
                   use --scale
  --output OUTPUT  output image's path
```

You should use --scale or --width and/or --height.

--output is optional defines the result image's folder


# Examples

You have 200x100 image file "testing.jpg" in the same folder as the current script
```
python image_resize.py testing.jpg --scale 0.5
Done: 
E:\GitHub\devman\12_image_resize\testing__100x50.jpg
```

```
python image_resize.py testing.jpg --height 200 --output test
Done: 
E:\GitHub\devman\12_image_resize\test\testing__400x200.jpg
```


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
