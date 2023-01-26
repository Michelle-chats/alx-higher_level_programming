<<<<<<< HEAD

=======
#!/usr/bin/python3
"""Contain a single function that read files"""


def read_file(filename=""):
    """Reads and prints content of file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
>>>>>>> 52de03cb9438db5a31f736c893d7998590a04bb2
