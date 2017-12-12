
# this is the only function in this program, def cheese_and_crackers()
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# here it pass number directly to the function 
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# here we use the above script to pass new value or numbers by calling new variables
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# calling the function and adding number inside the fuction
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# Input: asking numbers from users and passed to function cheese_and_crackers()
print ('Enter how many cheese: ')
cheese = str(input())
print ('Enter how many crackers: ')
crackers = str(input())
cheese_and_crackers(cheese, crackers)