import argparse
import os
from PIL import Image


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("original_path", type=str, help="original image's path")
    parser.add_argument("--width", type=int, help="width of output image")
    parser.add_argument("--height", type=int, help="height of output image")
    parser.add_argument("--scale", type=float, help="scale of output image. "
                                                    "Don't use --width or --height"
                                                    "if you use --scale")
    parser.add_argument("--output", type=str, help="output image's path")
    args = parser.parse_args()
    return args.original_path, args.width, args.height, args.scale, args.output


def get_new_size(old_width, old_height, new_width, new_height, scale):
    if scale is not None:
        return int(old_width * scale), int(old_height * scale)
    if new_width and new_height:
        return new_width, new_height
    if new_width:
        return new_width, int(old_height * new_width / old_width)
    if new_height:
        return int(old_width * new_height / old_height), new_height


def resize_image(path_to_original, path_to_result, arg_width, arg_height, arg_scale):
    image = Image.open(path_to_original)
    original_width, original_height = image.size
    new_width, new_height = get_new_size(
        original_height,
        original_width,
        arg_width,
        arg_height,
        arg_scale
    )
    image = image.resize((new_width, new_height))
    new_name = make_new_name(path_to_original, (new_width, new_height))
    new_file_full_path = os.path.join(path_to_result, new_name)
    image.save(new_file_full_path)
    return str(os.path.abspath(new_file_full_path))


def make_new_name(file_path, image_size):
    original_name = os.path.split(file_path)[1].split(".")[0]
    return "{0}__{1}x{2}.{3}".format(str(original_name),
                                     str(image_size[0]),
                                     str(image_size[1]),
                                     str(os.path.split(file_path)[1].split(".")[1])
                                     )


if __name__ == "__main__":
    original_path, width, height, scale, output_path = get_args()
    if not os.path.isfile(original_path):
        exit("{} not exists".format(os.path.abspath(original_path)))
    if scale and (width or height):
        exit("Arguments error: Don't use --scale with --width and --height")
    if scale is None and width is None and height is None:
        exit("Arguments error: No arguments to resize. Start with --help")
    if output_path is None:
        output_path = os.path.dirname(os.path.abspath(original_path))
    if not os.path.isdir(output_path):
        exit("Error: {} is not existing folder".format(output_path))
    if scale is None and (width and height):
        print("Warning: Proportions could be broken!")
    result_path = resize_image(original_path, output_path, width, height, scale)
    print("Done: \n{}".format(result_path))
