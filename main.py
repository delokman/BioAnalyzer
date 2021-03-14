import argparse
from modules.instagram import getInstagramInfos

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", help="Target Username")
    args = parser.parse_args()

    username = args.username

    instagram_data = getInstagramInfos(username)
    print(instagram_data)
main()