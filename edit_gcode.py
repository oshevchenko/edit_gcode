import re
import os
import shutil
import argparse

multiplier = 0.5

def modify_speed(file_path, file_path_modified):
    modified_lines = []
    pattern_float = re.compile(r'F(\d+\.\d+)')
    pattern_int = re.compile(r'F(\d+)')
    with open(file_path, "r") as f:
        for line in f:
            match_float = pattern_float.search(line)
            match_int = pattern_int.search(line)
            if match_float:
                speed_text = match_float.group(1)
                speed = float(speed_text)
                speed *= multiplier
                new_line = pattern_float.sub(f"F{speed:.1f}", line)
                line = new_line
            elif match_int:
                speed_text = match_int.group(1)
                speed = float(speed_text)
                speed *= multiplier
                new_line = pattern_int.sub(f"F{int(speed)}", line)
                line = new_line
            modified_lines.append(line)
    with open(file_path_modified, "w") as f:
        f.writelines(modified_lines)

def run_through_gcode_files(directory, callback):
    modified_dir = os.path.join(directory, "modified")

    if os.path.isdir(modified_dir):
        print(f"The sub-directory 'modified' exists in {directory}")
        # force remove the 'modified' directory
        shutil.rmtree(modified_dir)
    else:
        print(f"The sub-directory 'modified' does not exist in {directory}")
    # create the 'modified' directory
    os.mkdir(modified_dir)

    for file in os.listdir(directory):
        if file.endswith(".gcode"):
            file_path = os.path.join(directory, file)
            file_path_modified = os.path.join(modified_dir, file)
            print(f"Processing file: {file_path}")
            callback(file_path, file_path_modified)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""Process G-code files in a directory.
        Modify the speed of the G-code files by multiplying a factor (default 0.5).
        This script will create a 'modified' sub-directory in the specified directory
        and save the modified files there.""")
    parser.add_argument("directory", type=str, help="The directory containing G-code files.")
    parser.add_argument("--multiplier", type=float, help="Speed multiplier.")
    args = parser.parse_args()
    if args.multiplier:
        multiplier = args.multiplier
    run_through_gcode_files(args.directory, modify_speed)
