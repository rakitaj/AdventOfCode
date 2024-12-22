import argparse
import requests


# Create an ArgumentParser object
parser = argparse.ArgumentParser(description="This script downloads the data for the given Advent of Code.")

# Add arguments
parser.add_argument("-y", "--year", required=True, help="Year number")
parser.add_argument("-d", "--day", required=True, help="Day number")
parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")

# Parse the arguments
args = parser.parse_args()

# https://adventofcode.com/2024/day/6/input
url = f"https://adventofcode.com/{args.year}/day/{args.day}/input"

print(url)
r = requests.get(url)
print(r.text)