import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Save the Earth: A Global Warming Game")

global_temperature = 1.0
carbon_footprint = 100
years = 0
happy = 5
images = {}


def update_status():
    status_text = (f"Global Temperature Rise: {global_temperature:.2f}°C\n"
                   f"City's Carbon Footprint: {carbon_footprint}\n"
                   f"Years: {years}\n"
                   f"City Happiness: {happy}")
    status_label.config(text=status_text)


def check_game_over():
    global global_temperature
    if global_temperature >= 2.0:
        messagebox.showinfo("Game Over", "The global temperature has risen too much! Game Over.")
        root.quit()
    elif happy <= 0:
        messagebox.showinfo("Game Over", "The city is too sad! Game Over.")
        root.quit()
    elif years >= 10:
        if global_temperature < 2.0:
            messagebox.showinfo("Congratulations!", "You successfully managed the city for 10 turns!")
        root.quit()


def display_image(square_index, image_name):
    if square_index < len(square_positions):
        photo_image = images.get(image_name)
        if photo_image:
            canvas.create_image(square_positions[square_index], image=photo_image)


def invest_in_renewable_energy():
    global carbon_footprint, global_temperature, years, happy
    carbon_footprint -= 15
    global_temperature += 0.05  # Slight temperature rise due to resource use
    years += 1
    happy += 1
    if years - 1 < len(square_positions):
        display_image(years - 1, "renewable energy")
    messagebox.showinfo("Action Taken", "Invested in renewable energy! Carbon footprint reduced.")
    update_status()
    check_game_over()


def plant_trees():
    global carbon_footprint, global_temperature, years, happy
    carbon_footprint -= 10
    global_temperature += 0.02
    years += 1
    happy += 1
    if years - 1 < len(square_positions):
        display_image(years - 1, "tree")
    messagebox.showinfo("Action Taken", "Planted trees! Carbon footprint reduced.")
    update_status()
    check_game_over()


def enforce_carbon_tax():
    global carbon_footprint, global_temperature, years, happy
    carbon_footprint -= 20
    global_temperature += 0.1
    years += 1
    happy -= 1
    if years - 1 < len(square_positions):
        display_image(years - 1, "carbon tax")
    messagebox.showinfo("Action Taken", "Enforced carbon tax! Significant reduction in carbon footprint.")
    update_status()
    check_game_over()


def do_nothing():
    global carbon_footprint, global_temperature, years
    carbon_footprint += 10
    global_temperature += 0.15
    years += 1
    display_image(years - 1, "nothing")
    messagebox.showinfo("Action Taken", "Did nothing. Carbon footprint increased.")
    update_status()
    check_game_over()


def promote_public_transport():
    global carbon_footprint, global_temperature, years, happy
    carbon_footprint -= 12
    global_temperature += 0.03
    years += 1
    happy += 1
    if years - 1 < len(square_positions):
        display_image(years - 1, "train")
    messagebox.showinfo("Action Taken", "Promoted Public Transport! Significant reduction in carbon footprint.")
    update_status()
    check_game_over()


def ban_plastics():
    global carbon_footprint, global_temperature, years, happy
    carbon_footprint -= 8
    global_temperature += 0.01
    years += 1
    happy -= 1
    if years - 1 < len(square_positions):
        display_image(years - 1, "plastic")
    messagebox.showinfo("Action Taken", "Ban single-use plastics! Slight reduction in carbon footprint.")
    update_status()
    check_game_over()


status_label = tk.Label(root, text="", justify=tk.LEFT, padx=20)
status_label.pack(pady=10)

action_label = tk.Label(root, text="Choose your action for this turn:")
action_label.pack(pady=10)

renewable_button = tk.Button(root, text="Invest in Renewable Energy", command=invest_in_renewable_energy)
renewable_button.pack(pady=5)

trees_button = tk.Button(root, text="Plant Trees", command=plant_trees)
trees_button.pack(pady=5)

carbon_tax_button = tk.Button(root, text="Enforce Carbon Tax", command=enforce_carbon_tax)
carbon_tax_button.pack(pady=5)

do_nothing_button = tk.Button(root, text="Do Nothing", command=do_nothing)
do_nothing_button.pack(pady=5)

public_transport_button = tk.Button(root, text="Promote Public Transport", command=promote_public_transport)
public_transport_button.pack(pady=5)

plastics_button = tk.Button(root, text="Ban Single-Use Plastics", command=ban_plastics)
plastics_button.pack(pady=5)

images["renewable energy"] = tk.PhotoImage(file="renewable energy.png")
images["tree"] = tk.PhotoImage(file="tree.png")
images["carbon tax"] = tk.PhotoImage(file="carbon tax.png")
images["nothing"] = tk.PhotoImage(file="nothing.png")
images["train"] = tk.PhotoImage(file="train.png")
images["plastic"] = tk.PhotoImage(file="plastic.png")
images["square"] = tk.PhotoImage(file="white square.png")

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

side_length = 50
spacing = 10
square_positions = []

for i in range(5):
    x1 = i * (side_length + spacing) + 20
    y1 = 50
    square_positions.append((x1 + side_length // 2, y1 + side_length // 2))
    canvas.create_image(x1 + side_length // 2, y1 + side_length // 2, image=images["square"], anchor=tk.CENTER)

    y2 = 150
    square_positions.append((x1 + side_length // 2, y2 + side_length // 2))
    canvas.create_image(x1 + side_length // 2, y2 + side_length // 2, image=images["square"], anchor=tk.CENTER)

update_status()

root.mainloop()
