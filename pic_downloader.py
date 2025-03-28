import requests
url="https://c8.alamy.com/comp/2JPKFE6/gangtok-india-june-17-2022-people-walking-in-the-mg-marg-street-during-rainy-season-2JPKFE6.jpg"
r=requests.get(url)
if r.status_code==200:
    with open("pictures.html","wb") as f:
        f.write(r.content)
    print("Downloaded successfully")
else:
    print("Failed to download")