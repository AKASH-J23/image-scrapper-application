import streamlit as st
import requests
from bs4 import BeautifulSoup
import webbrowser
# from PIL import Image
# image=Image.open(r"C:\Users\AKASH J\Desktop\Orgware\streamlit\wallpaper.png")
# st.image(image,caption="image")
st.markdown("<h1 style='text-align: center;'> Web Scrapper </h1>",unsafe_allow_html=True)
with st.form("Scrapper"):
    element=st.text_input("Enter your word to Search")
    btn=st.form_submit_button("search")
variable=st.empty()
if element:
    page=requests.get("https://unsplash.com/s/photos/{element}")
    scrap=BeautifulSoup(page.content,'lxml')
    cols=scrap.find_all("div",class_="ripi6")
    col1,col2=variable.columns(2)
    for index,col in enumerate(cols):
        images=col.find_all("figure")
        for i in range(3):
            img=images[i].find("img",class_="tB6UZ a5VGX")
            list=img["srcset"].split("?")
            anchor=images[i].find("a",class_="rEAWd")
            print(anchor["href"])
            if i==0:
                col1.image(list[0])
                btn=col1.button("Download", key=str(index)+str(i))
                if btn:
                    webbrowser.open_new_tab("https://unsplash.com/"+anchor["href"])
            else:
                col2.image(list[0])
                btn=col2.button("Download", key=str(index)+str(i))
                if btn:
                    webbrowser.open_new_tab("https://unsplash.com/"+anchor["href"])