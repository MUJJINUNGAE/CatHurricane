import tkinter as tk
from PIL import Image, ImageTk
import os
import random

class CatMeme:
    def __init__(self, canvas, img_path, screen_width, screen_height, start_delay=0):
        self.canvas = canvas
        self.img_path = img_path
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        self.frames = []
        self.current_frame_idx = 0
        self.has_image = False
        
        if os.path.exists(self.img_path):
            self.has_image = True
            gif = Image.open(self.img_path)
            base_width = random.randint(60, 90)
            
            try:
                while True:
                    frame = gif.convert("RGBA")
                    w_percent = (base_width / float(frame.size[0]))
                    h_size = int((float(frame.size[1]) * float(w_percent)))
                    resized_frame = frame.resize((base_width, h_size), Image.Resampling.LANCZOS)
                    
                    self.cat_width, self.cat_height = resized_frame.size
                    self.frames.append(ImageTk.PhotoImage(resized_frame))
                    gif.seek(gif.tell() + 1)
            except EOFError:
                pass
        
        if not self.has_image:
            self.cat_width, self.cat_height = 60, 60
            self.cat_id = self.canvas.create_rectangle(0, 0, self.cat_width, self.cat_height, fill="white", outline="")
        else:
            self.cat_id = self.canvas.create_image(0, 0, anchor="nw", image=self.frames[0])
            
        self.x = -start_delay * random.randint(5, 8)
        self.y = 0
        self.speed = random.randint(6, 10)
        self.direction = "RIGHT"

    def update(self):
        if self.direction == "RIGHT":
            self.x += self.speed
            if self.x >= self.screen_width - self.cat_width:
                self.x = self.screen_width - self.cat_width
                self.direction = "DOWN"
        elif self.direction == "DOWN":
            self.y += self.speed
            if self.y >= self.screen_height - self.cat_height:
                self.y = self.screen_height - self.cat_height
                self.direction = "LEFT"
        elif self.direction == "LEFT":
            self.x -= self.speed
            if self.x <= 0:
                self.x = 0
                self.direction = "UP"
        elif self.direction == "UP":
            self.y -= self.speed
            if self.y <= 0:
                self.y = 0
                self.direction = "RIGHT"

        render_x = max(0, self.x)
        self.canvas.moveto(self.cat_id, render_x, self.y)

        if self.has_image and len(self.frames) > 0:
            self.current_frame_idx = (self.current_frame_idx + 1) % len(self.frames)
            self.canvas.itemconfig(self.cat_id, image=self.frames[self.current_frame_idx])


class MultiCatMemeApp:
    def __init__(self, root):
        self.root = root
        
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        
        self.root.geometry(f"{self.screen_width}x{self.screen_height}+0+0")
        self.root.overrideredirect(True)
        self.root.wm_attributes("-topmost", True)
        self.root.wm_attributes("-transparentcolor", "black")
        
        self.canvas = tk.Canvas(self.root, width=self.screen_width, height=self.screen_height, bg="black", highlightthickness=0)
        self.canvas.pack()
        
        self.meme_files = ["spinning-maxwell.gif", "banana-cat-cat-banana.gif", "giphy.gif", "popcat.gif", "stresscat.gif", "nyangcat.gif", "huh.gif", "cool-fun.gif"] 
        
        self.cats = []
        for i, file_name in enumerate(self.meme_files):
            cat = CatMeme(self.canvas, file_name, self.screen_width, self.screen_height, start_delay=i*30)
            self.cats.append(cat)
            
        self.root.bind("<Escape>", lambda e: self.root.destroy())
        self.update_loop()

    def update_loop(self):
        for cat in self.cats:
            cat.update()
            
        self.root.after(30, self.update_loop)

if __name__ == "__main__":
    root = tk.Tk()
    app = MultiCatMemeApp(root)
    root.mainloop()