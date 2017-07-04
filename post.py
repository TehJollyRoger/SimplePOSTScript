import requests


url = "URL"

postVars = { "postName:":postInput }
post = requests.post(url, params=postVars)
# theoretically you will read post to see the response/source code
# print(post.text)
