#!/usr/bin/python3
"""Reads stdin line by line and computes metrics"""


import sys


def computes_metrics():
    """Reads stdin line by line and computes metrics:
    - Total file size
    - Number of lines by status code (200, 301, 400, 401, 403, 404, 405, 500)
    Prints these statistics after every 10
    lines or on keyboard interruption (CTRL + C).
    """

    total_file_size = 0
    status_code_counts = {200: 0, 301: 0,
                          400: 0, 401: 0, 403: 0,
                          404: 0, 405: 0, 500: 0}

    try:
        line_count = 1
        if line_count % 10 == 0:
            print(f"File size: {total_file_size}")
            for code, count in sorted(status_code_counts.items()):
                if count > 0:
                    print(f"{code}: {count}")
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            try:
                try:
                    file_size_str = parts[-1]
                except IndexError:
                    pass
                try:
                    status_code_str = parts[-2]
                except IndexError:
                    pass
                file_size = int(file_size_str)
                status_code = int(status_code_str)
                total_file_size += file_size

                if status_code in status_code_counts:
                    status_code_counts[status_code] += 1
            except (ValueError):
                pass



    except KeyboardInterrupt:
        print(f"File size: {total_file_size}")
        for code, count in sorted(status_code_counts.items()):
            if count > 0:
                print(f"{code}: {count}")
        raise


if __name__ == "__main__":
    computes_metrics()
