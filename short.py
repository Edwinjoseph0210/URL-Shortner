import pyshorteners
url = input("Enter a URL: ")
short = pyshorteners.Shortener().tinyurl.short(url)
print("Shortened URL:", short)
