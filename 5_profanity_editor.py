import urllib.request
import urllib.parse
#def check_profanity(query):
    

def read_file_check_profanity():

    file = open(r"E:\Python\Level 0\curse_words_data\Check_Article.txt")
    file_contents = file.read()
    print(file_contents)
    #It is a good convention to close out any file that we have opened through our program.
    file.close()
    #check_profanity(file_contents)

    params = urllib.parse.urlencode({'q': file_contents})
    print("http://www.wdylike.appspot.com/?" + params)
    connections = urllib.request.urlopen("http://www.wdylike.appspot.com/?" + params)
    the_page = connections.read()
    print(the_page)
    connections.close()
read_file_check_profanity()
