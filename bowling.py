import tkinter as tk
from PIL import Image, ImageTk
from openai import OpenAI
import os
# Your OpenAI API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Function to calculate if it's a strike, spare, or normal round
def calculate_result(first_throw, second_throw):
    if first_throw == 10:
        return "strike"
    elif first_throw + second_throw == 10:
        return "spare"
    else:
        return "normal"

# Function to get detailed game explanation using GPT's API (gpt-3.5-turbo)
def get_explanation():
    game_summary = "In a game of bowling, players have 10 rounds to knock down pins. In each round, players have two chances to knock down 10 pins, except for the 10th round where they get an extra chance if they score a strike or spare. "
    detailed_rounds = "\n\nExplanation of each round:\n"

    for round_num, first_throw, second_throw, result in rounds_scores:
        detailed_rounds += f"Round {round_num}: {result.capitalize()}. "
        if result == "strike":
            detailed_rounds += f"The player knocked down all 10 pins on the first try. "
        elif result == "spare":
            detailed_rounds += f"The player knocked down all 10 pins in two tries, with {first_throw} on the first roll and {second_throw} on the second roll. "
        else:
            detailed_rounds += f"The player knocked down {first_throw} pins on the first roll and {second_throw} pins on the second roll. "

    prompt = game_summary + detailed_rounds + "\n\nProvide a detailed explanation of the game process based on these scores."

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": prompt}],
            max_tokens=400
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error generating explanation: {e}"

# Function to handle the game logic and save scores
def start_game():
    try:
        round_number = int(round_label.get())  # Get the current round number
        first_throw = int(first_throw_entry.get())  # Get the first throw value
        second_throw = int(second_throw_entry.get())  # Get the second throw value

        # Validate if throws are not empty and not exceeding 10 for both throws
        if first_throw < 0 or second_throw < 0 or first_throw + second_throw > 10:
            result_label.config(text="Invalid input. First and second throw must be valid numbers.")
            return

        # Calculate the result (strike, spare, or normal)
        result = calculate_result(first_throw, second_throw)

        # Update the result label
        result_label.config(text=f"Round {round_number}: {result}")

        # Save the result for explanation
        rounds_scores.append((round_number, first_throw, second_throw, result))

        # Clear the input fields after submitting the round
        first_throw_entry.delete(0, tk.END)
        second_throw_entry.delete(0, tk.END)

        # Only increment round if it is less than 10
        if round_number < 10:
            round_label.set(round_number + 1)

        # If it's the 10th round, get explanation and show it
        if round_number == 10:
            explanation = get_explanation()  # Get the explanation after round 10
            explanation_textbox.delete(1.0, tk.END)  # Clear previous explanation
            explanation_textbox.insert(tk.END, explanation)  # Insert new explanation

    except ValueError as e:
        result_label.config(text="Please enter valid numbers for both throws.")  # Handle invalid inputs

# Initialize the list to store scores for each round
rounds_scores = []

# Create the main window
root = tk.Tk()
root.geometry("600x600")  # Adjusted size to make the game window larger
root.config(bg="lightblue")  # Set background color for the window

# Add a background image (adjust the path if necessary)
image_path = "background_image.png"  # Adjusted to use 01.jpg for your background image
img = Image.open(image_path)
img = img.resize((600, 600))  # Resize image to fit the window
bg_image = ImageTk.PhotoImage(img)

# Create a label for the background image
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)  # Make it fill the entire window

# Round label and inputs
round_label = tk.IntVar()
round_label.set(1)

# Set labels with transparent background
tk.Label(root, text="Round:", bg="lightblue", font=("Arial", 14)).grid(row=0, column=0)
tk.Label(root, textvariable=round_label, bg="lightblue", font=("Arial", 14)).grid(row=0, column=1)

tk.Label(root, text="First Throw:", bg="lightblue", font=("Arial", 14)).grid(row=1, column=0)
first_throw_entry = tk.Entry(root, font=("Arial", 14), bd=1)  # Make entry transparent
first_throw_entry.grid(row=1, column=1)

tk.Label(root, text="Second Throw:", bg="lightblue", font=("Arial", 14)).grid(row=2, column=0)
second_throw_entry = tk.Entry(root, font=("Arial", 14), bd=1)  # Make entry transparent
second_throw_entry.grid(row=2, column=1)

# Result label and explanation (with larger text box for explanation)
result_label = tk.Label(root, bg="lightblue", font=("Arial", 14))
result_label.grid(row=3, column=0, columnspan=2)

explanation_label = tk.Label(root, text="Explanation:", bg="lightblue", font=("Arial", 14))
explanation_label.grid(row=4, column=0, columnspan=2)

explanation_textbox = tk.Text(root, height=10, width=40, font=("Arial", 12), bd=1)  # Transparent textbox
explanation_textbox.grid(row=5, column=0, columnspan=2)

# Button to submit the round
submit_button = tk.Button(root, text="Submit Round", command=start_game, bg="lightblue", font=("Arial", 14))
submit_button.grid(row=6, column=0, columnspan=2)

# Button to restart the game
def restart_game():
    global rounds_scores
    rounds_scores = []  # Reset the scores
    round_label.set(1)  # Reset round to 1
    first_throw_entry.delete(0, tk.END)  # Clear first throw input
    second_throw_entry.delete(0, tk.END)  # Clear second throw input
    result_label.config(text="")  # Clear result label
    explanation_textbox.delete(1.0, tk.END)  # Clear explanation

restart_button = tk.Button(root, text="Restart Game", command=restart_game, bg="lightblue", font=("Arial", 14))
restart_button.grid(row=7, column=0, columnspan=2)

# Start the Tkinter event loop
root.mainloop()
