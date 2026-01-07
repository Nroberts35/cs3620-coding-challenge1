#Part 1
print("PART 1\n")
principle = int(input("Enter Principle : "))
num_of_years = int(input("Enter Number of Years : "))
interest_rate = int(input("Enter Interest Rate : "))

simple_interest_rate = (principle * num_of_years * interest_rate) / 100
print(f"Simple interest rate is: {simple_interest_rate}")

# Part 2
print("\nPART 2\n")

favorite_foods = ["Pizza", "Sushi", "Steak", "Pasta", "Cheesecake"]
print(favorite_foods)
print(f"The 3rd element is: {favorite_foods[2]}")
favorite_foods.append("Chicken")
print(f"List of favorite foods is: {favorite_foods}")
favorite_foods.insert(3, "Tacos")
print(f"The updated list of favorite foods is {favorite_foods}")

print("Each food item in the list is: ")
for food in favorite_foods:
    print(food)

print(f'The number of favorite foods is: {len(favorite_foods)}')

# Part 3
print("\nPART 3\n")
for i in range(5):
    print("I am a programmer")

def print_squares_1_to_9():
    for num in range(1,10):
        print(f"{num} squared is {num**2}")

print_squares_1_to_9()