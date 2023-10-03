import sys

if len(sys.argv) < 3:
    print("Please specify file name and search text")
    sys.exit(1)  # exit with error code

file_to_search = sys.argv[1]
text_to_find = sys.argv[2]

print(f"Looking for '{text_to_find}' in {file_to_search}")

