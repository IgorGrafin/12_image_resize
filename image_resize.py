import argparse
import os
from PIL import Image


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "original_path",
        type=str,
        help="original image's path"
    )
    parser.add_argument(
        "--width",
        type=int,
        help="width of output image"
    )
    parser.add_argument(
        "--height",
        type=int,
        help="height of output image"
    )
    parser.add_argument(
        "--scale",
        type=float,
        help="scale of output image. Don't use --width "
             "or --height if you use --scale")
    parser.add_argument(
        "--output",
        type=str,
        help="output image's path"
    )
    return parser.parse_args()


def open_image(path_to_original):
    image = Image.open(path_to_original)
    return image


def get_new_size(old_width, old_height, new_width, new_height, scale):
    if scale is not None:
        return int(old_width * scale), int(old_height * scale)
    if new_width and new_height:
        return new_width, new_height
    if new_width:
        return new_width, int(old_height * new_width / old_width)
    if new_height:
        return int(old_width * new_height / old_height), new_height


def resize_image(image, new_file_full_path, new_width, new_height):
    image = image.resize((new_width, new_height))
    image.save(new_file_full_path)


def make_output_full_path(orig_path, width, height):
    file_name, extension = os.path.splitext(original_path)
    return "{0}__{1}x{2}{3}".format(
        file_name,
        width,
        height,
        extension
    )


def get_arguments_errors(original_path, width, height, scale, output_path):
    if not os.path.isfile(original_path):
        return "{} not exists".format(os.path.abspath(original_path))
    if scale and (width or height):
        return "Arguments error: Don't use --scale with --width and --height"
    if not any([scale, width, height]):
        return "Arguments error: No arguments to resize. Start with --help"
    if not os.path.isdir(output_path):
        return "Error: {} is not existing folder".format(output_path)


if __name__ == "__main__":
    args = get_args()
    original_path = os.path.abspath(args.original_path)
    width = args.width
    height = args.height
    scale = args.scale
    output_path = os.path.abspath(args.output)
    if output_path is None:
        output_path = os.path.dirname(original_path)

    arguments_errors = get_arguments_errors(
        original_path,
        width,
        height,
        scale,
        output_path
    )

    if arguments_errors:
        exit(arguments_errors)

    if scale is None and (width and height):
        print("Warning: Proportions could be broken!")

    original_image = open_image(original_path)
    original_width, original_height = original_image.size

    new_width, new_height = get_new_size(
        original_width,
        original_height,
        width,
        height,
        scale
    )

    new_file_full_path = make_output_full_path(original_path, new_width, new_height)
    resize_image(original_image, new_file_full_path, new_width, new_height)
    print("Done: \n{}".format(new_file_full_path))
