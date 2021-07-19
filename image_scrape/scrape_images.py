import os
import re
import requests
from bs4 import BeautifulSoup




def image_scrap(total_count, key_word):
    url = f"https://www.google.com/search?q={key_word}&tbm=isch&ved=2ahUKEwiG7f23kO7xAhVGEYgKHSRXCCIQ2-cCegQIABAA&oq=ball&gs_lcp=CgNpbWcQAzIECAAQQzIECAAQQzIECAAQQzICCAAyBAgAEEMyAggAMgQIABBDMgIIADICCAAyAggAOgQIIxAnUJ4UWP0YYMAeaABwAHgAgAFwiAGXA5IBAzIuMpgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=6uj0YIbQC8aioASkrqGQAg&bih=985&biw=1848"

    try :
        os.mkdir(os.path.join(os.getcwd(),key_word))
    except:
        pass

    os.chdir(os.path.join(os.getcwd(),key_word))

    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')

    image_url_list = soup.find_all('img', limit=total_count)

    for count,img_url in enumerate(image_url_list):
        link =img_url['src']
        name = key_word +f"_{count}"
        alt_name = img_url["alt"]
        print(alt_name)
        print(name,link)
        if not "gif" in link:
            # #save image
            with open(name+'.jpg','wb') as f:
                im = requests.get(link)
                f.write(im.content)
                f.close()



image_scrap(total_count = 10, key_word= "japanese_boy")