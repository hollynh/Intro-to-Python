#   Calculating the cost of a book order

#   User inputs how many books and cost of each book
numBooks = int(input("Please enter the number of books to order:"))
priceOfBook = float(input("Please enter the price of the book:"))

#   Tax and shipping is calculated
tax = (priceOfBook * numBooks) * .075
shipping = numBooks * 2

#   Total cost is the books+tax+shipping
orderSum = (numBooks * priceOfBook) + tax + shipping

#   Tells customer the total cost
print("The final cost of your order is:", orderSum)
