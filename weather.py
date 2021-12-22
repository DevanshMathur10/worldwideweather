from tkinter import *
import requests
import json

root=Tk()
root.geometry("1200x75")
root.title("Weather")

#https://api.weatherbit.io/v2.0/current?postal_code=302016&key=""YOUR API KEY""&include=minutely

def zipfind():
    #zipentry.get()
    #ziplbl=Label(root,text=zipentry.get())
    #ziplbl.grid(row=2,column=0)
    
    try: 
        apireq=requests.get("https://api.weatherbit.io/v2.0/current?postal_code="+zipentry.get()+"&key= YOUR API KEY ")   
        api=json.loads(apireq.content)
        city=api['data'][0]['city_name']
        aqi=api['data'][0]['aqi']
        weather=api['data'][0]['weather']['description']
        temp=api['data'][0]['temp']
        country=api['data'][0]['country_code']
        
        if temp<=38 and temp>=32:
            weathercolor="#cc0000"
        elif temp<32 and temp>=27:
            weathercolor="#ff3300"
        elif temp<27 and temp>=21:
            weathercolor="#ff9900"
        elif temp<21 and temp>=16:
            weathercolor="#ffff00"
        elif temp<16 and temp>=10:
            weathercolor="#99ff99"
        elif temp<10 and temp>=4:
            weathercolor="#339966"
        elif temp<4 and temp>=-1:
            weathercolor="#0099ff"
        elif temp<-1 and temp>=-7:
            weathercolor="#0000ff"
        elif temp<-7 and temp>=-12:
            weathercolor="#9966ff"
        elif temp<-12 and temp>=-18:
            weathercolor="#9900ff"
        elif temp<-18 and temp>=-23:
            weathercolor="#6600cc"
        elif temp<-23 and temp>=-50:
            weathercolor="#660066"

        apilabel=Label(root,text=city+" "+country+",Temperature "+str(temp)+"°C,Weather "+weather+",Air Quality "+str(aqi),font=("Comic Sans",20),background=weathercolor)
        apilabel.grid(row=1,column=0,columnspan=3,sticky=W+E)
        root.configure(background=weathercolor)

    except Exception as e:
        api="error..."


ziplabel=Label(root,text="ENTER ZIP CODE")
ziplabel.grid(row=0,column=0,padx=10)
zipentry=Entry(root,borderwidth=2,border=2)
zipentry.grid(row=0,column=1,padx=10)
zipbtn=Button(root,text="Select ZIPCODE",command=zipfind)
zipbtn.grid(row=0,column=2,padx=10)






root.mainloop()
