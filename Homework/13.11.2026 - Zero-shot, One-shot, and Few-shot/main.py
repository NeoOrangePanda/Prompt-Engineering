# from hf import generate_response
from groq import generate_response

def run_activity():
    print("ZERO-SHOT, ONE-SHOT & FEW-SHOT LEARNING ACTIVITY")

    category = input("Enter a category (e.g. animal, food, city): ").strip()
    item = input(f"Enter a specific {category} to classify: ").strip()

    if not category or not item:
        print("Please fill the both fields to run the activity.")
        return

    zero_shot = f"Is {item} a {category}? Answer yes or no."
    print("\n--- ZERO-SHOT LEARNING ---")
    print(f"Response: {generate_response(zero_shot, temperature=0.3, max_tokens=1024)}")

    one_shot = f"""
Category: animal
Item: dog
Answer: Yes, dog is an animal.

Now you try:
Category: {category}
Item: {item}
Answer:"""
    print("\n--- ONE-SHOT LEARNING ---")
    print(f"Response: {generate_response(one_shot, temperature=0.3, max_tokens=1024)}")

    few_shot = f"""
Example 1:
Category: animal
Item: dog
Answer: Yes, dog is an animal.

Example 2:
Category: Card Game
Item: UNO
Answer: Yes, UNO is a card game.

Example 3:
Category: City
Item: Italy
Answer: No, Italy is not a city. It's a country.

Now you try:
Category: {category}
Item: {item}
Answer:"""
    print("\n--- FEW-SHOT LEARNING ---")
    print(f"Response: {generate_response(few_shot, temperature=0.3, max_tokens=1024)}")

    creative_prompt = f"""Write a one-sentence story about the given word.

Example 1: 
Word: moon
Story: The moon lit up the night sky as a little astronaut began an exciting space adventure.

Example 2: 
Word: Dhaka
Story: As the sun rose over Dhaka, the bustling streets came alive with colorful rickshaws, busy markets, and the cheerful sounds of a city full of dreams and endless possibilities.

Word: {item}
Story:"""
    print("\n--- CREATIVE FEW-SHOT LEARNING ---")
    print(f"Response: {generate_response(creative_prompt, temperature=0.7, max_tokens=1024)}") 

    print("\n--- REFLECTION QUESTIONS ---")
    print("1. How did the responses differ between zero-shot, one-shot, and few-shot?")
    print("2. Which approach gave the most helpful response?")
    print("3. How did the examples influence the model's output?")

if __name__ == "__main__":
    run_activity()