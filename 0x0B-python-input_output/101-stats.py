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
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            if len(parts) >= 7:
                file_size_str = parts[-1]
                status_code_str = parts[-2]
                try:
                    file_size = int(file_size_str)
                    status_code = int(status_code_str)
                    total_file_size += file_size
                    if status_code in status_code_counts:
                        status_code_counts[status_code] += 1
                except ValueError:
                    pass

            if line_count % 10 == 0:
                print(f"File size: {total_file_size}")
                for code, count in sorted(status_code_counts.items()):
                    if count > 0:
                        print(f"{code}: {count}")

    except KeyboardInterrupt:
        print(f"File size: {total_file_size}")
        for code, count in sorted(status_code_counts.items()):
            if count > 0:
                print(f"{code}: {count}")


if __name__ == "__main__":
    computes_metrics()
