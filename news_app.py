import io
from tkinter import *
import webbrowser
import requests
from urllib.request import urlopen
from PIL import ImageTk, Image
 
class news:
    def __init__(self):
        self.data = requests.get('https://newsdata.io/api/1/latest?apikey=pub_49044d38ef95f6176c8df4643a5f0a26413a5&q=pegasus&language=en').json()
        self.root = Tk()
        self.root.title("Short News")
        self.root.geometry("300x450")
        self.root.configure(background='white')
        self.load_news(1)
    
    def load_news(self,index):
        self.clear()
        try:
            image=ImageTk.PhotoImage(Image.open(io.BytesIO(urlopen(self.data['results'][index]['image_url']).read())).resize((300,200)))
        except:
            image=ImageTk.PhotoImage(Image.open(io.BytesIO(urlopen("https://www.hhireb.com/wp-content/uploads/2019/08/default-no-img.jpg").read())).resize((350,200)))
        label = Label(self.root, image=image)
        label.pack()
        title = Label(self.root, text=self.data['results'][index]['title'], font=('Arial', 12 ,'bold'), bg='white',wraplength=280,justify='left')
        title.pack(padx=(10,10))
        description = Label(self.root, text=self.data['results'][index]['description'], font=('Arial', 10), bg='white',wraplength=280,justify='left')
        description.pack(padx=(10,10))
        frame=Frame(bg='white',height=100)
        frame.pack(side=BOTTOM,fill=X,pady=(0,10))  
        if index==len(self.data['results'])-1:
            index=-1
        next = Button(frame, text="Next", command=lambda:self.load_news(index+1), bg='black',fg='white',width=10,height=3)
        next.pack(side=RIGHT)
        rm=Button(frame, text="Read More", command=lambda:self.read(self.data['results'][index]['link']), bg='black',fg='white',width=19,height=3)
        rm.pack(side=RIGHT)
        if index==0:
            j=len(self.data['results'])
        else:
            j=index
        prev = Button(frame, text="Prev", command=lambda:self.load_news(j-1), bg='black',fg='white',width=10,height=3)
        prev.pack(side=RIGHT)
        
        self.root.mainloop()
    def read(self,link):
        webbrowser.open(link)
    def clear(self):
        for widget in self.root.pack_slaves():
            widget.destroy()
news()