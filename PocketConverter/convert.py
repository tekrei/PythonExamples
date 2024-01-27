#!/usr/bin/env python3

import sys
from bs4 import BeautifulSoup


def pocket_to_bookmarks(pocket_file, bookmarks_file):
    with open(pocket_file, "r") as file:
        data = file.read()
        soup = BeautifulSoup(data, "html.parser")
        with open(bookmarks_file, "w") as file:
            file.write("""<!DOCTYPE NETSCAPE-Bookmark-file-1>\n<DL>\n""")
            for link in soup.find_all("a"):
                file.write(
                    f"""\t<DT><A HREF="{link["href"]}" ADD_DATE="{link["time_added"]}" LAST_VISIT="" LAST_MODIFIED="">{link.text}</A>\n""")
            file.write("</DL>")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please enter the Pocket export file, prefer absolute path, the output will be written to bookmarks.html file to the same folder of this script.")
        exit(-1)

    pocket_to_bookmarks(sys.argv[1], "bookmarks.html")
