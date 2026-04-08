# -----------------------------------------
# Python Variables Assignment
# -----------------------------------------

# Step 1: Declare and assign default values to variables
name = "John Doe"
age = 25
city = "New York"
country = "USA"
isStudent = False


# Step 2: Function to print all variable values
def printInformation():
    print("---- User Information ----")
    print(f"Name      : {name}")
    print(f"Age       : {age}")
    print(f"City      : {city}")
    print(f"Country   : {country}")
    print(f"Is Student: {isStudent}")
    print("--------------------------\n")


# Step 3: Function to update variable values
def updateInformation(new_name, new_age, new_city, new_country, new_isStudent):
    global name, age, city, country, isStudent  # Allows updating global variables

    name = new_name
    age = new_age
    city = new_city
    country = new_country
    isStudent = new_isStudent


# Step 4: Main program execution

# Print initial values
print("Initial Values:")
printInformation()

# Update values
updateInformation(
    "Arikatla Subba Reddy",
    22,
    "Sarojinidevi",
    "India",
    True
)

# Print updated values
print("Updated Values:")
printInformation()