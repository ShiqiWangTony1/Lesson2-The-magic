# Task 1: Code Correction
# Buggy Code:

# place = input("Choose a place: forest or cave? ")

# if place = "forest":
#     action = input("climb a tree or cross a river?")
#     if action = "climb a tree":
#         print("You found a bird's nest!")
#     else action = "cross a river":
#         print("You found a boat!")
# elif place = "cave":
#     print("You find a hidden treasure!")

## Answer
# place = input("Choose a place: forest or cave? ")

# if place == "forest":
#     action = input("climb a tree or cross a river?")
#     if action == "climb a tree":
#         print("You found a bird's nest!")
#     elif action == "cross a river":
#         print("You found a boat!")
# elif place == "cave":
#     print("You find a hidden treasure!")
# else:
#     print("Invalid choice.")


# Task 2: Setting the Scene
# place = input("Choose a place: forest or cave? ")

# if place == "forest":
#     action = input("climb a tree or cross a river? ")
#     if action == "climb a tree":
#         print("You found a bird's nest!")
#     elif action == "cross a river":
#         print("You found a boat!")
#     else:
#         print("Invalid choice. Please choose either 'climb a tree' or 'cross a river'.")
# elif place == "cave":
#     action = input("light a torch or proceed in the dark? ")
#     if action == "light a torch":
#         print("You find a box of golden coins!")
#     elif action == "proceed in the dark":
#         print("You are dead!")
#     else:
#         print("Invalid choice.")
# else:
#     print("Invalid choice.")


# Task 3: Default Path

# place = input("Choose a place: forest or cave? ")

# if place == "forest":
#     action = input("climb a tree or cross a river? ")
#     if action == "climb a tree":
#         print("You found a bird's nest!")
#     elif action == "cross a river":
#         print("You found a boat!")
#     else:
#         pass
# elif place == "cave":
#     action = input("light a torch or proceed in the dark? ")
#     if action == "light a torch":
#         print("You find a box of golden coins!")
#     elif action == "proceed in the dark":
#         print("You are dead!")
#     else:
#         pass
# else:
#     pass

# Quick Decisions

# Task 1: Code Correction
# attendees = input("Enter number of attendees: ")
# venue = "large hall" if attendees > 100 elif "conference room"
# print(venue)

# attendees = int(input("Enter number of attendees: "))
# venue = "large hall" if attendees > 100 else "conference room"
# print(venue)

# Task 2: Enhanced Code with Additional Recommendations
# attendees = int(input("Enter number of attendees: "))
# venue = "large hall" if attendees > 100 else "conference room"

# if attendees > 100:
#     recommendation = "Using an audio system and projector."
# elif 50 < attendees <= 100:
#     recommendation = "Using a projector."
# else:
#     recommendation = "No additional equipments."

# print(f"Selected venue: {venue}")
# print(recommendation)


# Task 3: Catering Choices
# catering_choice = input("Do you want vegetarian food? (yes or no): ").strip().lower()

# if catering_choice == "yes":
#     caterer = "Veggie Delight Caterers"
# else:
#     caterer = "Gourmet Meals Caterers"

# print(f"Caterer Choice: {caterer}")