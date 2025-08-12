from stats import print_report
import sys

# Check if the user provided a file path as an argument
# If not, print usage instructions and exit
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    filepath = sys.argv[1]
    print_report(filepath)




