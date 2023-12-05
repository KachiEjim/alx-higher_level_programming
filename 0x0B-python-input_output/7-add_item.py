#!/usr/bin/python3
""" a script that adds all arguments to a Python
list, and then save them to a file"""

if __name__ == "__main__":
    save = __import__("5-save_to_json_file").save_to_json_file
    load = __import__("6-load_from_json_file").load_from_json_file

    from sys import argv
    import json
    args = argv[1:]
    try:
        data = load("add_item.json")
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = []
    data.extend(args)
    save(data, "add_item.json")
