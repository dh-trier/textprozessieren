import requests 

myurl = "https://archiveofourown.org/works/8584093?view_full_work=true"

try: 
    result = requests.get(myurl, timeout=3)
    content = result.text
    print(content)
except: 
    print("There was an error when get was tried.")
