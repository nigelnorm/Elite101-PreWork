import datetime  #for hours purposes


def prices(caller):
  prices = {
    "shirts": 15,
    "sandals": 5,
    "pants": 20,
    "jackets": 40,
    "coats": 30,
    "shorts": 10,
    "shoes": 40
  }
  print("These are our prices: ")
  for key, value in prices.items():
    print(key + ": " + str(value))
  buy = input("Would you like to buy anything?(Y/N)")
  
  if buy == "Y":
    item = input("What would you like to buy: ")
    if item in prices.keys():
      print("Thanks for purchasing!")
    else:
      print("That is not an item, try again")
  else:
    print("No problem.")


def location(caller):
  location = "Nowhere, Arizona"
  print("We are located in " + location)


def products(caller):
  products = [
    "shirts", "sandals", "pants", "jackets", "coats", "shorts", "shoes"
  ]
  print("We have: " + str(products))


def hours(caller):

  if "open" in caller:
    start = 8
    end = 23
    current = datetime.datetime.now().hour
    current += 6

    if start <= current <= end:
      print("Yes we are open. Come on in!")
    else:
      print(
        "Sorry, we are unfortunately closed. On weekdays we are open from 8:00 am to 11:00 pm"
      )
  else:
    print(
      "On weekdays we are open from 8:00 am to 11:00 pm. Please come in when you can."
    )


name = input("Hello, what is you're name? ")
print("Thanks for coming to this retail store " + name +
      ". How may I help you? ")
more = True
while (more):
  
  question = input()
  if "price" in question or "buy" in question:
    prices(question)
    
  elif "locat" in question or "where" in question:
    location(question)
    
  elif "hour" in question or "open" in question:
    hours(question)
    
  elif "product" in question or "have" in question:
    products(question)
    
  more = input("Anything else you'd like to ask?(Y/N)")
  
  if "N" in more:
    more = False
  else:
    print("How else may I help you?")
print("Thank you for calling us. Have a great day!")
