import collections
import itertools
import pickle

def score_guess(guess, ans):
    hints = []
    ans_no_match = []
    guess_no_match = []

    # First pass: Check for exact matches (black hints "B")
    for guess_elem, ans_elem in zip(guess, ans):
        if guess_elem == ans_elem:
            hints.append("B")
        else:
            guess_no_match.append(guess_elem)
            ans_no_match.append(ans_elem)

    # Debug: Print unmatched elements
    print(f"Unmatched Guess: {guess_no_match}")
    print(f"Unmatched Answer: {ans_no_match}")

    # Use counters for remaining unmatched elements
    ans_counter = collections.Counter(ans_no_match)

    # Second pass: Check for color matches in wrong positions (white hints "W")
    for guess_elem in guess_no_match:
        if ans_counter[guess_elem] > 0:
            hints.append("W")
            ans_counter[guess_elem] -= 1

    # Debug: Print final hints
    print(f"Hints: {hints}")

    return "".join(hints)

def build_dict():
    # Default dict avoids storing keys as tuple, saves lookup time
    score_dict = collections.defaultdict(dict)
    all_guesses = itertools.product(["R", "G", "B", "Y", "P", "O"], repeat=5)

    for guess, answer in itertools.product(all_guesses, repeat=2):
        guess_str = "".join(guess)
        ans_str = "".join(answer)
        score_dict[guess_str][ans_str] = score_guess(guess, answer)

    # Ensure the directory exists before saving the file
    import os
    os.makedirs("stored_objects", exist_ok=True)
    
    with open("stored_objects/average.pickle", "wb") as FileStore:
        pickle.dump(score_dict, FileStore)

def test_score_guess():
    assert score_guess("RRRRR", "RRRRR") == "BBBBB"
    assert score_guess("RRGBY", "RRGBY") == "BBBBB"
    assert score_guess("RRGBY", "RGBYR") == "BBWWW"
    assert score_guess("RRRRO", "RRRRO") == "BBBBB"
    assert score_guess("OORRG", "OORRG") == "BBBBB"
    assert score_guess("OORRG", "GROOR") == "WWWW"
    assert score_guess("OOOOO", "GGGGG") == ""
    assert score_guess("OOOOO", "OOOOO") == "BBBBB"
    assert score_guess("RRRRR", "GGGGG") == ""
    assert score_guess("RGYPO", "OGRYP") == "WWWWW"
    print("All tests passed!")

if __name__ == "__main__":
    test_score_guess()  # Run the tests to ensure the function works correctly
    build_dict()  # Build the dictionary and save it to a pickle file
