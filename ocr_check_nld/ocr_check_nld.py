import pyimgur
from re import findall
import requests


class Check():    
    def __init__(self, img_path, lang):
        self.img_path = img_path
        self.lang = lang

                
    def get_total(self):
        text = self.__recognize_text_from_file(self.img_path)
        print(text)
        try:
            total = self.__get_total_from_text(text)
        except ValueError:
            total = -1.0
            
        return total
    

    def __get_text_from_url(self, url, overlay=False, api_key="helloworld"):
        payload = {"url": url,
                   "isOverlayRequired": overlay,
                   "apikey": api_key,
                   "language": self.lang,
        }
        r = requests.post("https://api.ocr.space/parse/image",
                          data=payload,
        )
        text = r.content.decode()

        return text


    def __recognize_text_from_file(self, file_path, overlay=False, api_key="helloworld"):
        payload = {"isOverlayRequired": overlay,
                   "apikey": api_key,
                   "language": self.lang,
        }

        with open(self.img_path, "rb") as f:
            r = requests.post("https://api.ocr.space/parse/image",
                              files={self.img_path: f},
                              data=payload
            )
        text = r.content.decode()

        return text        
        

    def __get_total_from_text(self, text):
        SALE_THRESHOLD = 0.8 
        ptr = r"\d+\s{0,2}[\.,]\s{0,2}\d{2}"

        matches = findall(ptr, text)
        print(matches)
        floats_in_check = [float(mtch.replace(",", ".").replace(" ", "")) for mtch in matches]
        total = max(floats_in_check)
        total_index = floats_in_check.index(total)

        for price in floats_in_check[total_index + 1:]:
            if price >= SALE_THRESHOLD * total:
                total = price

        return total


    def upload_image(self):
        IMGUR_CLIENT_ID = ""
        im = pyimgur.Imgur(IMGUR_CLIENT_ID)
        uploaded_image = im.upload_image(self.img_path)

        print(uploaded_image.link)
        return uploaded_image.link
        
