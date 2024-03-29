from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk, messagebox, filedialog, scrolledtext, Frame

__author__="CHES-PGN"
__description__="Παρακολούθηση εξέλιξης αγώνα σκακιού από αρχείο pgn."
__version__="0.1"

# Χρώματα
WHITE = "#ffffff"
BLACK = "#000000"

# Διαστάσεις
SQUARE_SIZE = 80
BOARD_SIZE = 8 * SQUARE_SIZE
BOARD_EDGE = SQUARE_SIZE // 4  # Προσθήκη χώρου για αριθμούς και γράμματα
PIECE_SIZE = 40

# Πλήρης Λίστα Πιονιών
pieces = [
    "b_rook", "b_knight", "b_bishop", "b_queen", "b_king", "b_bishop", "b_knight", "b_rook",
    "b_pawn", "b_pawn", "b_pawn", "b_pawn", "b_pawn", "b_pawn", "b_pawn", "b_pawn",
    "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty",
    "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty",
    "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty",
    "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty",
    "w_pawn", "w_pawn", "w_pawn", "w_pawn", "w_pawn", "w_pawn", "w_pawn", "w_pawn",
    "w_rook", "w_knight", "w_bishop", "w_queen", "w_king", "w_bishop", "w_knight", "w_rook",
]

# Λίστα εικόνων
pieces_images = {
    "empty": "icons/pieces/empty.png",
    "b_rook": "icons/pieces/b_rook.png",
    "b_knight": "icons/pieces/b_knight.png",
    "b_bishop": "icons/pieces/b_bishop.png",
    "b_queen": "icons/pieces/b_queen.png",
    "b_king": "icons/pieces/b_king.png",
    "b_pawn": "icons/pieces/b_pawn.png",
    "w_rook": "icons/pieces/w_rook.png",
    "w_knight": "icons/pieces/w_knight.png",
    "w_bishop": "icons/pieces/w_bishop.png",
    "w_queen": "icons/pieces/w_queen.png",
    "w_king": "icons/pieces/w_king.png",
    "w_pawn": "icons/pieces/w_pawn.png",
}







def load_pgn_file():
    file_path = filedialog.askopenfilename(title="Άνοιγμα Αρχείου PGN", filetypes=[("PGN Αρχεία", "*.pgn")])
    if file_path:
        with open(file_path, 'r') as file:
            pgn_data = file.read()
        return pgn_data
    return None

def parse_pgn_data(pgn_data):
    game_info = {}
    moves = []

    lines = pgn_data.split('\n')

    for line in lines:
        if line.startswith("["):
            key, value = line[1:-1].split(' ', 1)
            game_info[key] = value.strip('\"')
        elif line.strip():  # Ελέγχουμε αν η γραμμή δεν είναι κενή
            moves.append(line)

    return game_info, moves



# Αρχικοποίηση του Tkinter
root = tk.Tk()
root.title("Σκάκι-PGN")
root.iconbitmap("icons\\chess-pgn.ico")
root.resizable(False, False)



def load_right_frame():
    # def clear_label_text(label):
    #     label.set(text="")

    # def clear_scrolled_text(scrolled):
    #     scrolled.delete(1.0, tk.END)

    # clear_label_text(label_game_players)
    # clear_label_text(label_game_result)
    # clear_label_text(label_game_details)
    # clear_scrolled_text(moves_display)

    # Φόρτωση αρχείου PGN
    pgn_data = load_pgn_file()
    
    # Ανάλυση των πληροφοριών και των κινήσεων
    game_info, moves = parse_pgn_data(pgn_data)

    # Εμφάνιση των πληροφοριών σε 3 γραμμές
    game_players = "{}  ({} - {})  -  {}  ({} - {})".format(
        game_info.get("White", ""),
        game_info.get("WhiteTitle", ""),
        game_info.get("WhiteElo", ""),
        game_info.get("Black", ""),
        game_info.get("BlackTitle", ""),
        game_info.get("BlackElo", ""),
    )
    game_result = "{}".format(
        game_info.get("Result", "")
    )

    game_details = "{}  ({})  [{}]  {}  {}".format(
        game_info.get("Event", ""),
        game_info.get("Site", ""),
        game_info.get("Round", ""),
        game_info.get("ECO", ""),
        game_info.get("Date", "")
    )

    right_frame  =  Frame(root,  width=400,  height=300, background=WHITE)
    right_frame.grid(row=0,  column=1, pady=20, sticky='n')

    # Εμφάνιση σε 3 γραμμές με 3 labels

    label_game_players = ttk.Label(right_frame, text=game_players, font=("Arial 10 bold italic"), background=WHITE)
    label_game_players.grid(row=0, column=1, padx=1,  pady=1)


    label_game_result = ttk.Label(right_frame, text=game_result, font=("Arial 10"), background=WHITE)
    label_game_result.grid(row=1, column=1, padx=1,  pady=1)

 
    label_game_details = ttk.Label(right_frame, text=game_details, font=("Arial 10"), background=WHITE)
    label_game_details.grid(row=2, column=1, padx=1,  pady=1)

    # Προσθήκη ScrolledText widget
    moves_display = scrolledtext.ScrolledText(right_frame, wrap=tk.WORD, width=50, height=25, font=("Arial", 10), background=WHITE)
    moves_display.grid(row=3, column=1, padx=5,  pady=5)

    # Συνάρτηση για την εμφάνιση των κινήσεων
    def display_moves():
        if moves:
            moves_text = "\n".join(moves)
            moves_display.delete('1.0', tk.END)
            moves_display.insert(tk.END, moves_text)
        else:
            moves_display.delete('1.0', tk.END)
            moves_display.insert(tk.END, "No moves available.")

    # Εμφάνιση των κινήσεων
    display_moves()




# Δημιουργία canvas
canvas = tk.Canvas(root, width=BOARD_SIZE + 2 * BOARD_EDGE, height=BOARD_SIZE + 2 * BOARD_EDGE)
canvas.grid(row=0, column=0, rowspan=4)  # Χρήση grid αντί για pack

# Φόρτωση και resize εικόνων
# resized_images = {piece_name: ImageTk.PhotoImage(Image.open(file_path).resize((PIECE_SIZE, PIECE_SIZE), resample=Image.BICUBIC))
#                   for piece_name, file_path in pieces_images.items()}
resized_images = {}

for piece_name, file_path in pieces_images.items():
    try:
        # Attempt to open the image and resize it
        resized_image = Image.open(file_path).resize((PIECE_SIZE, PIECE_SIZE), resample=Image.BICUBIC)
        # Convert the resized image to PhotoImage
        resized_images[piece_name] = ImageTk.PhotoImage(resized_image)
    except Exception as e:
        print(f"Error processing {piece_name} image: {e}")



# Σχεδίαση τετραγώνων
def draw_board():
    for i in range(8):
        for j in range(8):
            color = WHITE if (i + j) % 2 == 0 else BLACK
            canvas.create_rectangle(
                BOARD_EDGE + i * SQUARE_SIZE,
                BOARD_EDGE + j * SQUARE_SIZE,
                BOARD_EDGE + (i + 1) * SQUARE_SIZE,
                BOARD_EDGE + (j + 1) * SQUARE_SIZE,
                fill=color,
            )

# Τοποθέτηση πιονιών
def draw_pieces():
    for i in range(8):
        for j in range(8):
            piece_name = pieces[j * 8 + i]
            if piece_name != "empty.png":
                canvas.create_image(
                    BOARD_EDGE + (i + 0.5) * SQUARE_SIZE,
                    BOARD_EDGE + (j + 0.5) * SQUARE_SIZE,
                    image=resized_images[piece_name],
                )

# Σχεδίαση αριθμών και γραμμάτων
def draw_labels():
    labels = 'abcdefgh'
    for i in range(8):
        canvas.create_text(
            BOARD_EDGE + (i + 0.5) * SQUARE_SIZE,
            BOARD_EDGE / 2,
            text=labels[i],
        )
        canvas.create_text(
            BOARD_EDGE + (i + 0.5) * SQUARE_SIZE,
            BOARD_SIZE + 1.5 * BOARD_EDGE,
            text=labels[i],
        )
        canvas.create_text(
            BOARD_EDGE / 2,
            BOARD_EDGE + (i + 0.5) * SQUARE_SIZE,
            text=str(8 - i),
        )
        canvas.create_text(
            BOARD_SIZE + 1.5 * BOARD_EDGE,
            BOARD_EDGE + (i + 0.5) * SQUARE_SIZE,
            text=str(8 - i),
        )

# Δημιουργία γραμμής μενού
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="Αρχείο", menu=file_menu)

def open_folder():
    pass
    #file_path = pass
    # Εδώ μπορείτε να προσθέσετε τον κώδικα για την εύρεση του αρχείου

def exit_game():
    root.destroy()    

file_menu.add_command(label="Άνοιγμα Αρχείου", command=load_right_frame)
file_menu.add_command(label="Άνοιγμα φακέλου", command=open_folder)
file_menu.add_command(label="Τερματισμός", command=exit_game)

help_menu = tk.Menu(menu)
menu.add_cascade(label="Βοήθεια", menu=help_menu)

def show_help():
    messagebox.showinfo("Πώς να παίξετε", "Εδώ θα πρέπει να προσθέσετε τις οδηγίες για το παιχνίδι σας.")

def show_version():
    messagebox.showinfo("Έκδοση", "Εδώ θα πρέπει να προσθέσετε την έκδοση του παιχνιδιού σας.")

help_menu.add_command(label="Πώς να παίξετε", command=show_help)
help_menu.add_command(label="Έκδοση", command=show_version)


# Σχεδίαση τετραγώνων
draw_board()

# Τοποθέτηση πιονιών
draw_pieces()

# Σχεδίαση αριθμών και γραμμάτων
draw_labels()

# Εκκίνηση κύκλου εκδηλώσεων
root.mainloop()
