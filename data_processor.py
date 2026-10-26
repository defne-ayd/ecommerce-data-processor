#task 1
with open("users.txt", "r") as users:
    user_list = []
    for line in users:
        user = line.split(",")
        user_list.append(user[0]) #I put the information into a list to access it easily
    user_list.pop(0) #the first line contained the headers so I deleted it from the list
    print("Existing Users: ",end="")
    for i in range(len(user_list)):
        if i < len(user_list) - 1: #this is to make sure that I do not get the last item of the list yet
            print(user_list[i],end=", ")
        else:
            print(user_list[i])
def add_new_user(username,age,email):
    with open("users.txt", "a") as users:
        print("Adding new user: ", username)
        new_user = [username, age, email]
        users.write("\n")
        for i in range(len(new_user)):
            if i < len(new_user) - 1:
                users.write(str(new_user[i]))
                users.write(", ")
            else:
                users.write(new_user[i]+"\n")
        print("User successfully registered!")
def login(username):
    with open("users.txt", "r") as users:
        print("Enter username to login:", username)
        for line in users:
            user = line.split(", ") #turned the line into a list to be able to access the name seperately
            name = user[0].strip()
            if username == name:
                print("Login successful! Welcome, ", username, ".",sep="")
                break
add_new_user("defne_aydin",18,"defneaydin06@gmail.com")
login("defne_aydin")

#task 2
with open("products.txt", "r") as products:
    print("Original Products:")
    for line in products:
        if not line.startswith("ID"): #to not print the headers
            print(line)
with open("products.txt", "r") as products:
        sum = 0
        for line in products: #I found the number of original products
            sum += 1
def add_product(product):
    with open("products.txt", "a") as products:
        products.write("\n"+product)

add_product("21, Smart Watch, 2000, 15")
add_product("22, Gaming Mouse, 1500, 20")
add_product("23, Mechanical Keyboard, 3500, 10")
add_product("24, Wireless Earbuds, 2500, 30")
add_product("25, Monitor, 5000, 8")

with open("products.txt", "r") as products:
        new_sum = 0
        for line in products: #I found the number of products in the updated list
            new_sum += 1
        print("New Products:")
        for j in range(1,new_sum+1):
            line = products.readline()
            if j > sum: #the products that were added later can be selected and printed this way
                print(line)    

#task 3
catalog = {}
with open("products.txt", "r") as products:
    for line in products:
        if not line.startswith("ID"): #I put the products' names and prices into a dictionary 
            product = line.split(", ")
            catalog[product[1].strip()] = product[2].strip()

shopping_cart = {}
def add_to_cart(item,amount):
    shopping_cart[item] = catalog[item] * amount # the overall price is the original price of the product times the number of times the user added it to the cart 
def remove_from_cart(item):
    shopping_cart.pop(item)
def calculate_total():
    total = 0
    for item in shopping_cart:
        total += int(shopping_cart[item]) #I calculated the sum of all of the products' prices
    return total

add_to_cart("Phone",1)
add_to_cart("Laptop",1)
add_to_cart("Headphones",1)
add_to_cart("Digital Camera",1)
add_to_cart("Smart TV",1)
add_to_cart("External Hard Drive",1)
add_to_cart("Printer",1)
add_to_cart("Laptop Stand",1)
add_to_cart("Mouse",1)
add_to_cart("Microphone",1)
add_to_cart("Bluetooth Speaker",1)
add_to_cart("Smart Watch",1)
add_to_cart("Gaming Mouse",1)
add_to_cart("Mechanical Keyboard",1)
add_to_cart("Monitor",1)

print("Cart after adding products:")
for item in shopping_cart:
    amount = int(shopping_cart[item]) // int(catalog[item]) #to show the number of times the user added an item to their cart
    print("-", item, "x" + str(amount) + ":", shopping_cart[item])

print("Total:", calculate_total())

remove_from_cart("Phone")
remove_from_cart("Smart TV")
remove_from_cart("Headphones")
remove_from_cart("External Hard Drive")
remove_from_cart("Mouse")
remove_from_cart("Mechanical Keyboard")
remove_from_cart("Smart Watch")

print("Cart after removing products:")
for item in shopping_cart:
    amount = int(shopping_cart[item]) // int(catalog[item])
    print("-", item, "x" + str(amount) + ":", shopping_cart[item])
print("Total:", calculate_total())

#task 4
def discount():
    total = calculate_total()
    if total > 1000:
        price = total * 90 // 100
        print("After 10% discount:", price)
    if "Laptop" or "Monitor" in shopping_cart:
        print("After 15% discount on specific products:")
    if "Laptop" in shopping_cart:
        total -= int(shopping_cart["Laptop"]) * 15 // 100
        print("-Laptop: Original price", shopping_cart["Laptop"] + ",", "Discounted price", int(shopping_cart["Laptop"]) * 85 // 100)
    if "Monitor" in shopping_cart:
        total -= int(shopping_cart["Monitor"]) * 15 // 100
        print("-Monitor: Original price", shopping_cart["Monitor"] + ",", "Discounted price", int(shopping_cart["Monitor"]) * 85 // 100)
    print("Final Total:", total)
    return total

discount()

#task 5
def transaction_summary(username,shopping_cart,total):
    with open("transaction_summary.txt", "w") as transaction:
        transaction.write("User: " + username + "\n")
        transaction.write("Products:\n")
        for item in shopping_cart:
            amount = int(shopping_cart[item]) // int(catalog[item]) #to calculate the number of times the user added an item to their cart
            transaction.write("- " + item + " x" + str(amount) + ": " + shopping_cart[item] + "\n")
        transaction.write("Final Total: ")
        transaction.write(str(total) + "\n")
        
    with open("transaction_summary.txt", "r") as transaction:
        for line in transaction:
            print(line)
        print("Transaction summary has been successfuly saved to the file!")

transaction_summary("defne_aydin",shopping_cart,discount())

#task 6
with open("products.txt", "r") as file:
    products = []
    for line in file:
        if line.startswith("ID"): #the first line is the headers
            headers = line.strip().split(", ")
        else:
            values = line.strip().split(", ") #I put the lines into a list to control them better
            product = {
                headers[0]: int(values[0]),
                headers[1]: values[1],
                headers[2]: int(values[2]),
                headers[3]: int(values[3])
            } #I created a dictionary of each product to make the rest of the code simpler
            products.append(product)

def write_products(filename, products):
    with open(filename, "w") as file:
        headers = "ID, Name, Price, Stock"
        file.write(headers + "\n")
        for product in products: #I wrote the updated version of all products back into the file
            file.write(str(product["ID"]) + ", " + product["Name"] + ", " + str(product["Price"]) + ", " + str(product["Stock"]) + "\n")

def adjust_product_details(products, ids_to_update, price_factor, stock_factor):
    if not ids_to_update:
        return
    for product in products:
        if product["ID"] == ids_to_update[0]:
            product["Price"] = product["Price"] * price_factor
            product["Stock"] = product["Stock"] * stock_factor
            break
    adjust_product_details(products, ids_to_update[1:], price_factor, stock_factor) #the function will run for as long as there is an id left in the list

ids_to_update = [1,4,14,21]
price_factor = float(input("Enter the price adjustment factor:"))
stock_factor = float(input("Enter the stock adjustment factor:"))

adjust_product_details(products,ids_to_update,price_factor,stock_factor)
print("Updated Products:")
for product in products:
    if product["ID"] in ids_to_update: #I displayed the products that were updated
        print(product)
write_products("products.txt",products)

#task 7
def search_by_price_range(products, min_price, max_price):
    return [product for product in products if min_price <= product["Price"] <= max_price]

def filter_by_stock(products, minimum_stock):
    return [product for product in products if product["Stock"] > minimum_stock]

def search_by_name(products, name_keyword):
    return [product for product in products if name_keyword in product["Name"]]

print("Search by Price Range (3000-6000):")
result = search_by_price_range(products,3000,6000)
for product in result:
    print(product)

print("Filter by Stock Availability (>10):")
result = filter_by_stock(products,10)
for product in result:
    print(product)

print("Search by Product Name (contains 'Mouse'):")
result = search_by_name(products, "Mouse")
for product in result:
    print(product)

  