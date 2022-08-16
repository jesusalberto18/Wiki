
"""

This encyclopedia is a small project for applying
to open source.

"""

import wikipedia as wiki

print(":Wikipedia with Python:")

try:
    search = input("\nWhat do you want to search?\nSearch: ")
    wiki = wiki.summary(search,sentences=4)
    print("\nWiki:\n")
    print(wiki)
except:
    print("\nThere is not coincidence found.\nPlease, try searching other term.")
