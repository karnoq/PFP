def read_text():
    quotes = open("movie_quotes.txt")
    contents_of_file = quotes.read()
    print contents_of_file
    quotes.close()

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    output = connection.read()
    print output
    connection.close()

read_text()
