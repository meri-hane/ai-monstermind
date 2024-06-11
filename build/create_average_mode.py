from itertools import product
import pickle

# Define the colors and pegs
colors = ['B', 'G', 'P', 'R', 'Y', 'O']
num_pegs = 5

# Function to calculate hints
def calculate_hints(guess, answer):
    hints = []
    guess_no_match = []
    ans_no_match = []
    
    for guess_elem, ans_elem in zip(guess, answer):
        if guess_elem == ans_elem:
            hints.append("B")
        else:
            guess_no_match.append(guess_elem)
            ans_no_match.append(ans_elem)
    
    for guess_elem in guess_no_match:
        if guess_elem in ans_no_match:
            hints.append("W")
            ans_no_match.remove(guess_elem)
    
    return ''.join(hints)

# Generate all possible guesses and answers
all_combinations = list(product(colors, repeat=num_pegs))

# Create the lookup table
lookup_table = {}

for guess in all_combinations:
    guess_key = tuple(guess)
    lookup_table[guess_key] = []
    
    possible_answers = all_combinations.copy()
    while possible_answers:
        current_answer = possible_answers.pop(0)
        lookup_table[guess_key].append(''.join(current_answer))
        
        if current_answer == guess:
            break
        
        new_possible_answers = []
        correct_hints = calculate_hints(current_answer, guess)
        
        for ans in possible_answers:
            if calculate_hints(current_answer, ans) == correct_hints:
                new_possible_answers.append(ans)
        
        possible_answers = new_possible_answers

with open('stored_objects/easy_trial.pickle', 'wb') as f:
    pickle.dump(lookup_table, f)

print("Successfully loaded!")
# Example usage: Print the lookup table for a specific guess
example_guess = ('R', 'R', 'B', 'R', 'O')
print(f"Lookup table for guess {example_guess}:")
print(lookup_table[example_guess])