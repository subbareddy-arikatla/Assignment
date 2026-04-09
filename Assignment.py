# Step 1 & 2: Declare variables with default values
name = "John"
age = 20
city = "New York"
country = "USA"
isStudent = True

# Step 3: Function to print information
def printInformation():
    print("Name:", name)
    print("Age:", age)
    print("City:", city)
    print("Country:", country)
    print("Is Student:", isStudent)
    print("---------------------------")

# Step 4: Function to update information
def updateInformation(new_name, new_age, new_city, new_country, new_isStudent):
    global name, age, city, country, isStudent
    name = new_name
    age = new_age
    city = new_city
    country = new_country
    isStudent = new_isStudent

# Step 5: Main execution
if __name__ == "__main__":
    print("Before Update:")
    printInformation()

    updateInformation("Alice", 25, "London", "UK", False)

    print("After Update:")
    printInformation()