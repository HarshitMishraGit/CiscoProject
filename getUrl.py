from bs4 import BeautifulSoup
import requests


url=input("Enter the url")
def get_video_url(url):
    response = requests.get(url)
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all anchor tags in the page
    links = soup.find_all('a')
    # Find the <a> tag with specific classes
    a_tag = soup.find('a', class_="maxbutton-1 maxbutton maxbutton-stream-online")
    # Extract the link URL if the tag exists
    # if a_tag:
    #     link_url = a_tag['href']
    #     print(link_url)
    # else:
    #     print("No matching <a> tag found.")
    first_link=''
    if a_tag:
        first_link=a_tag['href']
        print("first_link : ",first_link)
        req=requests.get(first_link)
        soup=BeautifulSoup(req.content,'html.parser')
        # Find the <img> tag with inline CSS property 'cursor: pointer;'
        img_tag = soup.find('img', style='cursor: pointer;')
        # Extract the 'src' attribute if the tag exists
        if img_tag:
            print(img_tag)
            # img_src = img_tag['src']
            # print(img_src)
        else:
            print("No image is found")

get_video_url(url)

