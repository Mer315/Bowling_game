import tkinter as tk
from PIL import Image, ImageTk
import pygame # type: ignore
import os
import cv2 # type: ignore
import time
import random

class AnimatedGIF(tk.Label):
    def __init__(self, master, path, delay=100):
        super().__init__(master)
        self._master = master
        self._path = path
        self._delay = delay
        self._image = Image.open(self._path)
        self._frames = self._prepare_frames(self._image)
        self._frame_index = 0
        self.config(image=self._frames[self._frame_index])
        self._animate()

    def _prepare_frames(self, image):
        frames = []
        try:
            while True:
                frame = image.copy().convert("RGBA")
                frame = frame.resize((self._master.winfo_screenwidth(), self._master.winfo_screenheight()), Image.LANCZOS)
                frames.append(ImageTk.PhotoImage(frame))
                image.seek(image.tell() + 1)
        except EOFError:
            pass
        return frames

    def _animate(self):
        self._frame_index = (self._frame_index + 1) % len(self._frames)
        self.config(image=self._frames[self._frame_index])
        self._master.after(self._delay, self._animate)

def play_sound():
    pygame.mixer.init()
    sound_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), r"C:\Users\ssume\OneDrive\Desktop\Bowling game\130515-Bowling-Machinery-BehindLane-Roll-Strike-MultiplePins-Fienup-002.mp3")
    pygame.mixer.music.load(sound_path)
    pygame.mixer.music.play()
    new_sound_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), r"C:\Users\ssume\OneDrive\Desktop\Bowling game\moosic.mp3")
    new_sound = pygame.mixer.Sound(new_sound_path)
    new_sound.play(-1)

def open_player_details_window():
    pygame.mixer.music.stop()

    for widget in root.winfo_children():
        widget.destroy()

    root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")

    image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), r"C:\Users\ssume\OneDrive\Desktop\Bowling game\2players.jpeg")
    image = Image.open(image_path)
    image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)

    image_label = tk.Label(root, image=photo)
    image_label.image = photo
    image_label.place(x=0, y=0, relwidth=1, relheight=1)

    frame = tk.Frame(root, bg="#00FFDC")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    title_label = tk.Label(frame, text="Enter Player Names", font=("Quarterback", 16, "bold"),bg="#00FFDC",fg="black")
    title_label.pack(pady=10)

    player1_label = tk.Label(frame, text="PLAYER 1", font=("Quarterback", 15),bg="#00FFDC",fg="black")
    player1_label.pack(pady=5)
    player1_entry = tk.Entry(frame, font=("Quarterback", 12),bg="black",fg="#00FFDC")
    player1_entry.pack(pady=5)

    player2_label = tk.Label(frame, text="PLAYER 2", font=("Quarterback", 15),bg="#00FFDC",fg="black")
    player2_label.pack(pady=5)
    player2_entry = tk.Entry(frame, font=("Quarterback", 12),bg="black",fg="#00FFDC")
    player2_entry.pack(pady=5)

    next_button = tk.Button(frame, text="Next", font=("Quarterback", 12), command=lambda: next_page(player1_entry, player2_entry),bg="black",fg="#00FFDC")
    next_button.pack(pady=20)

    frame.pack(expand=True)

def next_page(player1_entry, player2_entry):
    global player1, player2
    player1 = player1_entry.get()
    player2 = player2_entry.get()
    

    for widget in root.winfo_children():
        widget.destroy()

    root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")

    # Adding background image
    background_image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), r"C:\Users\ssume\OneDrive\Desktop\Bowling game\turnss.PNG")
    background_image = Image.open(background_image_path)
    background_image = background_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
    background_photo = ImageTk.PhotoImage(background_image)

    background_label = tk.Label(root, image=background_photo)
    background_label.image = background_photo
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    frame = tk.Frame(root, bg="#00FFDC")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    title_label = tk.Label(frame, text="Enter Number of Turns", font=("Quarterback", 16, "bold"),bg="#00FFDC",fg="black")
    title_label.pack(pady=10)

    turns_label = tk.Label(frame, text="Number of Turns", font=("Quarterback", 12),bg="#00FFDC",fg="black")
    turns_label.pack(pady=5)
    turns_entry = tk.Entry(frame, font=("Quarterback", 12),bg="black",fg="#00FFDC")
    turns_entry.pack(pady=5)

    submit_button = tk.Button(frame, text="Submit", font=("Quarterback", 12), command=lambda: submit_turns(turns_entry),bg="black",fg="#00FFDC")
    submit_button.pack(pady=20)

    frame.pack(expand=True)

def submit_turns(turns_entry):
    global num_turns, current_turn, player1_scores, player2_scores, current_player
    num_turns = int(turns_entry.get())
    current_turn = 0
    player1_scores = []
    player2_scores = []
    current_player = 1
    

    for widget in root.winfo_children():
        widget.destroy()

    open_game_window()

def open_game_window():
    global pin_entry, pin_scale, stop_button, player_label, current_player, video_canvas1, video_canvas2, player1_score_label, player2_score_label, moving_scale

    for widget in root.winfo_children():
        widget.destroy()

    image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), r"C:\Users\ssume\OneDrive\Desktop\Bowling game\videos part.jpg")
    image = Image.open(image_path)
    image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)

    image_label = tk.Label(root, image=photo)
    image_label.image = photo
    image_label.place(x=0, y=0, relwidth=1, relheight=1)

    frame = tk.Frame(root, bg="black")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    if current_player == 1:
        player_label = tk.Label(frame, text=f"{player1} 's Turn", font=("Quarterback", 16, "bold"),bg ="black", fg= "#00FFDC")
    else:
        player_label = tk.Label(frame, text=f"{player2} 's Turn", font=("Quarterback", 16, "bold"),bg ="black", fg= "#00FFDC")

    player_label.pack(pady=10)

    title_label = tk.Label(frame, text=f"Select Number of Pins Struck \n Turn {current_turn + 1}", font=("Quarterback", 12, "bold"),bg ="black", fg= "#00FFDC")
    title_label.pack(pady=10)

    pin_scale = tk.Scale(frame, from_=0, to=10, orient=tk.HORIZONTAL, length=300, tickinterval=1, resolution=1)
    pin_scale.set(5)
    pin_scale.pack(pady=20)
    
    stop_button = tk.Button(frame, text="Stop", font=("Quarterback", 12), command=stop_scale,bg ="#00FFDC", fg= "black")
    stop_button.pack(pady=10)
    
    random_button = tk.Button(frame, text="Random", font=("Quarterback", 12), command=generate_random_video,bg ="#00FFDC", fg= "black")
    random_button.pack(pady=10)

    player_frame1 = tk.Frame(root, bg="black")
    player_frame1.place(relx=0.05, rely=0.1, anchor="nw")

    player1_score_label = tk.Label(player_frame1, text="Player 1 Scores: ", font=("Quarterback", 12),bg='black',fg ='#00FFDC')
    player1_score_label.pack()

    video_canvas1 = tk.Canvas(root, width=400, height=600, bg="black")
    video_canvas1.place(relx=0.005,rely=0.15, anchor="nw")

    player_frame2 = tk.Frame(root, bg="black")
    player_frame2.place(relx=0.9, rely=0.1, anchor="ne")

    video_canvas2 = tk.Canvas(root, width=400, height=600, bg="black")
    video_canvas2.place(relx=0.7, rely=0.15, anchor="nw")

    player2_score_label = tk.Label(player_frame2, text="Player 2 Scores: ", font=("Quarterback", 12),bg='black', fg = '#00FFDC')
    player2_score_label.pack()

    frame.pack(expand=True)

    move_scale()

def move_scale():
    global moving_scale
    pin_scale.set((pin_scale.get() + 1) % 11)
    moving_scale = root.after(100, move_scale)
    pin_scale.config(bg="black", fg="#00FFDC",troughcolor="#00FFDC")

def stop_scale():
    global moving_scale
    if moving_scale:
        root.after_cancel(moving_scale)
        moving_scale = None
        pins_hit = pin_scale.get()
        
        # Ensure the sliding bar stops at the current position
        pin_scale.set(pins_hit)
        
        play_video(pins_hit)

def generate_random_video():
    global moving_scale
    if moving_scale:
        root.after_cancel(moving_scale)  # Cancel any ongoing sliding bar movement
    pins_hit = random.randint(0, 10)
    
    # Ensure the sliding bar stops at the randomly generated position
    pin_scale.set(pins_hit)
    
    play_video(pins_hit)

def play_video(pins_hit):
    global current_turn, current_player, num_turns, player1_scores, player2_scores, moving_scale

    video_pins_map = {
        0: r"C:\Users\ssume\OneDrive\Desktop\Bowling game\0.mp4",
        1: r"CC:\Users\ssume\OneDrive\Desktop\Bowling game\1.mp4",
        2: r"C:\Users\ssume\OneDrive\Desktop\Bowling game\2.mp4",
        3: r"C:\Users\ssume\OneDrive\Desktop\Bowling game\3.mp4",
        4: r"C:\Users\ssume\OneDrive\Desktop\Bowling game\4.mp4",
        5: r"C:\Users\ssume\OneDrive\Desktop\Bowling game\5.mp4",
        6: r"C:\Users\ssume\OneDrive\Desktop\Bowling game\6.mp4",
        7: r"C:\Users\ssume\OneDrive\Desktop\Bowling game\7.mp4",
        8: r"C:\Users\ssume\OneDrive\Desktop\Bowling game\8.mp4",
        9: r"C:\Users\ssume\OneDrive\Desktop\Bowling game\9.mp4",
        10: r"C:\Users\ssume\OneDrive\Desktop\Bowling game\10.mp4"
    }

    video_path = video_pins_map.get(pins_hit)
    if video_path:
        cap = cv2.VideoCapture(video_path)
        canvas_width = 400
        canvas_height = 600
        start_time = time.time()
        slow_motion_factor = 2  # Slow motion factor (2 means half speed, 3 means one-third speed, etc.)

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            elapsed_time = time.time() - start_time
            if elapsed_time >= 7 * slow_motion_factor:  # Ensure video plays for at least 7 seconds * slow_motion_factor
                break

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (canvas_width, canvas_height))
            frame_image = Image.fromarray(frame)
            frame_photo = ImageTk.PhotoImage(frame_image)

            if current_player == 1:
                video_canvas = video_canvas1
                scores_label = player1_score_label
                player_scores = player1_scores
            else:
                video_canvas = video_canvas2
                scores_label = player2_score_label
                player_scores = player2_scores

            video_canvas.create_image(0, 0, anchor=tk.NW, image=frame_photo)
            video_canvas.image = frame_photo

            scores_label.config(text=f"Player {current_player} Scores: {', '.join(map(str, player_scores))}")

            root.update()
            cv2.waitKey(int(30 * slow_motion_factor))  # Adjust delay for slow motion

        cap.release()

        if current_player == 1:
            player1_scores.append(pins_hit)
            current_player = 2
        else:
            player2_scores.append(pins_hit)
            current_player = 1
            current_turn += 1

        if current_turn < num_turns:
            open_game_window()
        else:
            show_results()
    else:
        return 0

def calculate_score(player):
    n = len(player)
    score = 0
    prev1 = 0
    prev2 = 0

    for i in range(n):
        present_turn = player[i]
        if prev1 == 10 or prev2 == 10:
            turn_score = 2 * present_turn
        else:
            turn_score = present_turn

        score += turn_score

        prev2 = prev1
        prev1 = present_turn

    return score

def winner(player1_scores, player2_scores):
    score1 = calculate_score(player1_scores)
    score2 = calculate_score(player2_scores)

    if score1 > score2:
        return 1, score1, score2
    elif score2 > score1:
        return 2, score1, score2
    else:
        return 0, score1, score2

def show_results():
    # Calculate winner and total scores
    result, total_score1, total_score2 = winner(player1_scores, player2_scores)
    if result == 1:
        winner_name = player1
    elif result == 2:
        winner_name = player2
    else:
        winner_name = "It's a Tie!"

    # Clear the previous contents of the window
    for widget in root.winfo_children():
        widget.destroy()

    # Load and resize the background image
    background_image_path = r"C:\Users\ssume\OneDrive\Desktop\Bowling game\scoress.PNG"  # Replace with your image path
    background_image = Image.open(background_image_path)
    background_image = background_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
    background_photo = ImageTk.PhotoImage(background_image)

    # Create a label to display the background image
    background_label = tk.Label(root, image=background_photo)
    background_label.image = background_photo
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    winner_label = tk.Label(root, text=f"", font=("Quarterback", 40, "bold"),bg='#00FFDC')
    winner_label.pack(pady=50)
    # Display winner's name
    winner_label = tk.Label(root, text=f"Winner : {winner_name} !!!", font=("Quarterback", 40, "bold"),bg='black',fg ='#00FFDC')
    winner_label.pack(pady=5)

    # Display pins hit by each player
    player1_pins_label = tk.Label(root, text=f"{player1}'s Pins Hit: {', '.join(map(str, player1_scores))}", font=("Quarterback", 11),bg='black',fg ='#00FFDC')
    player1_pins_label.pack(pady=5)

    player2_pins_label = tk.Label(root, text=f"{player2}'s Pins Hit: {', '.join(map(str, player2_scores))}", font=("Quarterback", 11),bg='black',fg ='#00FFDC')

    player2_pins_label.pack(pady=5)

    # Display total scores
    total_scores_label = tk.Label(root, text=f"Total Scores:\n{player1}: {total_score1}\n{player2}: {total_score2}", font=("Quarterback", 12,"bold"),bg='black',fg ='#00FFDC')
    total_scores_label.pack(pady=10)

    # Display breakdown of scores
    if result != 0:
        player1_turn_scores = [calculate_score(player1_scores[:i+1]) for i in range(len(player1_scores))]
        player2_turn_scores = [calculate_score(player2_scores[:i+1]) for i in range(len(player2_scores))]

        player1_score_breakdown = "\n".join([f"Turn {i+1}: {score}" for i, score in enumerate(player1_turn_scores)])
        player2_score_breakdown = "\n".join([f"Turn {i+1}: {score}" for i, score in enumerate(player2_turn_scores)])

        player1_score_breakdown_label = tk.Label(root, text=f"{player1}'s Score Breakdown:\n{player1_score_breakdown}", font=("Quarterback", 10),bg='black',fg ='#00FFDC')
        player1_score_breakdown_label.pack(pady=5)

        player2_score_breakdown_label = tk.Label(root, text=f"{player2}'s Score Breakdown:\n{player2_score_breakdown}", font=("Quarterback", 10),bg='black',fg ='#00FFDC')
        player2_score_breakdown_label.pack(pady=5)
    
    # Add a Finish button to go to the ending screen
    finish_button = tk.Button(root, text="Finish", font=("Helvetica", 12), command=show_ending_screen,bg='#00FFDC',fg ='black')
    finish_button.pack(pady=20)

def show_ending_screen():
    # Clear the window
    for widget in root.winfo_children():
        widget.destroy()

    # Load and resize the background image
    background_image_path = r"C:\Users\ssume\OneDrive\Desktop\Bowling game\FINISH.jpeg"
    background_image = Image.open(background_image_path)
    background_image = background_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
    background_photo = ImageTk.PhotoImage(background_image)

    # Create a label to display the background image
    background_label = tk.Label(root, image=background_photo)
    background_label.image = background_photo
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Add an exit button
    exit_button = tk.Button(root, text="Exit", font=("Quarterback", 35), command=root.destroy,bg='black',fg='#00FFDC')
    exit_button.pack(pady=80, side = "bottom")

def main():
    global root, current_player
    root = tk.Tk()
    root.title("Bowling Game")
    root.attributes('-fullscreen', True)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    gif_path = os.path.join(script_dir, r"C:\Users\ssume\OneDrive\Desktop\Bowling game\FINALISED GIF.gif")
    animated_gif = AnimatedGIF(root, gif_path, delay=100)
    animated_gif.pack(expand=True)
    start_label= tk.Label(root, text= "Bowling Game", font=("Quarterback",34,'bold'), bg = "black",fg ="#00FFDC")
    start_label.place(relx=0.505,rely=0.405,anchor = "center")
    start_button = tk.Button(root, text="START", font=("Quarterback", 20, 'bold'), bg="#00FFDC", fg="black", command=open_player_details_window)
    start_button.place(relx=0.5,rely=0.5,anchor = "center")
    play_sound()
    root.mainloop()

if __name__ == "__main__":
    main()
