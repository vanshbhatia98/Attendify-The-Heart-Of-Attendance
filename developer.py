import os
from tkinter import *
from PIL import Image, ImageTk, ImageDraw, ImageFont

class DeveloperPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Attendify – Developer Team")
        self.root.state('zoomed')
        self.root.update_idletasks()

        # Dimensions
        self.WIDTH  = self.root.winfo_width()
        self.HEIGHT = self.root.winfo_height()

        # ─── 1) BACKGROUND ──────────────────────────────────────────────────────
        color_top = (0, 64, 128)
        color_bot = (102, 204, 255)
        gradient = Image.new("RGB", (self.WIDTH, self.HEIGHT), color_top)
        top_img  = Image.new("RGB", (self.WIDTH, self.HEIGHT), color_bot)
        mask     = Image.new("L",   (self.WIDTH, self.HEIGHT))
        mask_data = [int(255 * (y / (self.HEIGHT-1))) for y in range(self.HEIGHT) 
                     for _ in range(self.WIDTH)]
        mask.putdata(mask_data)
        gradient = Image.composite(top_img, gradient, mask)
        self.bg_photo = ImageTk.PhotoImage(gradient)
        Label(self.root, image=self.bg_photo).place(x=0, y=0, 
                                                   relwidth=1, relheight=1)

        # ─── 2) HEADER ──────────────────────────────────────────────────────────
        header_h = int(self.HEIGHT * 0.25)
        base_dir = os.path.join(os.path.dirname(__file__), "images")
        hdr_path = os.path.join(base_dir, "header.jpg")

        self.header = Canvas(self.root, width=self.WIDTH, height=header_h,
                             highlightthickness=0)
        if os.path.exists(hdr_path):
            img = Image.open(hdr_path).resize((self.WIDTH, header_h), 
                                              Image.Resampling.LANCZOS)
            self.hdr_img = ImageTk.PhotoImage(img)
            self.header.create_image(0, 0, image=self.hdr_img, anchor=NW)
        else:
            self.header.create_rectangle(0, 0, self.WIDTH, header_h,
                                         fill="#004080", outline="")

        # Larger header fonts
        self.header.create_text(self.WIDTH//2, header_h//2 - 40,
            text="Meet the Team",
            font=("Calibri", 56, "bold"),
            fill="white"
        )
        self.header.create_text(self.WIDTH//2, header_h//2 + 40,
            text="The heart of Attendify’s attendance system",
            font=("Calibri", 28, "italic"),
            fill="white"
        )
        self.header.place(x=0, y=0)

# ─── 3) TEAM CARDS ──────────────────────────────────────────────────────
        team = [
            {"img": "vansh.jpg", "name": "Vansh Bhatia",  "role": "Project Lead"},
            {"img": "tarun.jpg", "name": "Tarun Tomar",   "role": "Backend Developer"},
            {"img": "vikas.jpg", "name": "Vikas Sharma",  "role": "Frontend Dev"},
            {"img": "sahil.jpg", "name": "Sahil",         "role": "Tester"},
        ]
        rows, cols = 2, 2
        px, py = 50, 30
        card_w = (self.WIDTH  - (cols+1)*px) // cols
        card_h = (self.HEIGHT - header_h - (rows+1)*py) // rows

        img_size = int(card_h * 0.8)  # 80% of card height

        for idx, member in enumerate(team):
            r, c = divmod(idx, cols)
            x = px + c * (card_w + px)
            y = header_h + py + r * (card_h + py)

            card = Frame(self.root, bg="white", bd=2, relief=RIDGE)
            card.place(x=x, y=y, width=card_w, height=card_h)

            # Load or placeholder
            img_path = os.path.join(base_dir, member["img"])
            if os.path.exists(img_path):
                pil = Image.open(img_path).resize((img_size, img_size), Image.Resampling.LANCZOS)
            else:
                pil = Image.new("RGB", (img_size, img_size), (240,240,240))
                d = ImageDraw.Draw(pil)
                txt = "No Image"
                fnt = ImageFont.load_default()
                bb = d.textbbox((0,0), txt, font=fnt)
                w,h = bb[2]-bb[0], bb[3]-bb[1]
                d.text(((img_size-w)//2,(img_size-h)//2), txt, fill=(120,120,120), font=fnt)

            photo = ImageTk.PhotoImage(pil)
            lbl_img = Label(card, image=photo, bg="white")
            lbl_img.photo = photo
            lbl_img.place(x=10, y=(card_h - img_size)//2, width=img_size, height=img_size)

            # Name and Role
            text_frame = Frame(card, bg="white")
            text_frame.place(x=img_size + 20, y=0, width=card_w - img_size - 30, height=card_h)

            Label(text_frame, text=member["name"],
                font=("Calibri", 20, "bold"), bg="white", fg="#004080")\
                .pack(anchor="w", pady=(card_h//3 - 20, 5))

            Label(text_frame, text=member["role"],
                font=("Calibri", 18), bg="white", fg="#555")\
                .pack(anchor="w")

if __name__ == "__main__":
    root = Tk()
    DeveloperPage(root)
    root.mainloop()
