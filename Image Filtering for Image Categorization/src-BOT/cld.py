import cloudinary
import cloudinary.uploader
import cloudinary.api
import pandas as pd
cloudinary.config( 
  cloud_name = "viki123", 
  api_key = "871819852199947", 
  api_secret = "Ht_ya2ZFlYRhIi3oy3NVNm9YVnM" 
)
result=cloudinary.uploader.upload("tes/pass1.jpg",
  ocr = "adv_ocr")
if(result['info']['ocr']['adv_ocr']['status'] == 'complete'):
    data = result['info']['ocr']['adv_ocr']['data']
f=open("hello.json","w")
f.write(str(data))
f.close
print(list(data)) 
    