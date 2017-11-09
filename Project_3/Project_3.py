import json
import requests
import pprint
import sys
def api_get_request(url):
    # In this exercise, you want to call the last.fm API to get a list of the
    # top artists in Spain. The grader will supply the URL as an argument to
    # the function; you do not need to construct the address or call this
    # function in your grader submission.
    # 
    # Once you've done this, return the name of the number 1 top artist in
    # Spain. 
    data = requests.get(url).text
    data = json.loads(data)
    
    print data['topartists']['artist'][0]['name']
    #return ... # return the top artist in Spain


if __name__ == "__main__":
    
    # Print the version of python used
    print (sys.version)
    
    #Eg: http://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key=f879e78f3ce1ed43e58e3fc7df625c71&artist=rihanna&album=Loud&format=json
    url = 'http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&country=spain&api_key=f879e78f3ce1ed43e58e3fc7df625c71&format=json'
   
    api_get_request(url)