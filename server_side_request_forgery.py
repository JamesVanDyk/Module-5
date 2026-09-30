"""
url = input("Enter URL: ")
response = requests.get(url)
print(response.text)
"""

#no checks are put in place to check that an actual url is entered. whatever is entered is put into the .get method which can
#include queries.

"""
while validURL = false:
    url = input("Enter URL: ")
    if "http" in url:
        validURL = true
    else: 
        validURL = false
response = requests.get(url)
print(response.text)
"""

#This checks that http is in the url address so that it is actually a link. no queries can be entered without asking the user to 
#re-enter the url