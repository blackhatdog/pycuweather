import tkinter as tk
import requests
import time

#--------------------definitions+api json data extraction--------------------------#
def getweather(root):
    city = textfield.get()
    #fill api key in halves in blanks
    api = ''+ city + ''
    json_data = requests.get(api).json()
    conditions = json_data['weather'][0]['main']
    temp=int (json_data['main']['temp'] - 273.15)
    mintemp=int (json_data['main']['temp_min'] - 273.15)
    maxtemp=int (json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    cn = json_data['sys']['country']
    
    loc = json_data['name']
    
    
    

    final_info = conditions + '\n'+str(temp)+'°C'
    final_data = '\n' + 'Max Temp:' + str(maxtemp)+'\n'+'Min temp:'+str(mintemp) +'\n'+'Pressure:'+str(pressure)+'\n'+'Humidity:'+str(humidity)+'\n'+'Wind speed:'+str(wind)+'\n'+'Location :'+str(loc)+'\n'+'Region:'+str(cn)  
    label1.config(text=final_info)
    label2.config(text=final_data)
    
    

#---------------------gui root----------------------------#

root = tk.Tk()
root.title('PyCuWeather')
root.geometry('600x500')

f=('poppins',13,'bold')
t=('poppins',35,'bold')

textfield=tk.Entry(root,font=t)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<Return>',getweather)

label1=tk.Label(root,font = t)
label1.pack()
label2=tk.Label(root,font = f)
label2.pack()
signture=tk.Label(root,text='PyCuWeather By Nihal Sabu Raj')
signture.pack(pady=120)

root.mainloop()
