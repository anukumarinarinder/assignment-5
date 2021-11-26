# Defining a class for Shirts
class Shirts:
    def __init__(self):
        pass
    
    # Function for getting input from user
    def getUserChoice(self):
        typeOfShirt = 0
        colorOfShirt = 0
        quantityOfShirt = 0
        print("Please choose a type of T-shirt: \n1.Polo T-shirt \n2.Round Neck T-shirt")
        typeOfShirt = int(input(typeOfShirt))
        print("Please choose color of T-shirt: \n1.Blue\n2.Green\n3.Red")
        colorOfShirt = int(input(colorOfShirt))
        print("Please enter quantity of T-shirts")
        quantityOfShirt = int(input(quantityOfShirt))
        return typeOfShirt, colorOfShirt, quantityOfShirt

# Defining a class for Pants
class Pants:
    def __init__(self):
        pass 
    
    # Function for getting input from user
    def getUserChoice(self):
        typeOfPants = 0
        colorOfPants = 0
        quantityOfPants = 0
        print("Please choose a type of Pants: \n1.Cargo Pants \n2.Jeans")
        typeOfPants = int(input(typeOfPants))
        print("Please choose color of Pants: \n1.Beige\n2.Black\n3.Blue")
        colorOfPants = int(input(colorOfPants))
        print("Please enter quantity of Pants")
        quantityOfPants = int(input(quantityOfPants))
        return typeOfPants, colorOfPants, quantityOfPants

# Defining class Calculate for Total Price and Discount
class Calculate:
  def __init__(self):
    pass

  priceOfshirt = 9.99
  shirtAttributes = ()
  shirtObject = Shirts()
  shirtAttributes = shirtObject.getUserChoice()
  priceOfPants = 12
  pantsAttributes = ()
  pantsObject = Pants()
  pantsAttributes = pantsObject.getUserChoice()

  def calcDiscount(self):
    totalPriceshirt = 0
    # Calculating total price of shirts
    finalPriceshirt = self.shirtAttributes[2] * self.priceOfshirt
    totalPriceshirt = self.shirtAttributes[2] * self.priceOfshirt
    # Calculating total price of pants
    totalPricePants = 0
    finalPricePants = self.pantsAttributes[2] * self.priceOfPants
    totalPricePants = self.pantsAttributes[2] * self.priceOfPants
    
    studentOrSenCitz = ""
    # Boolean variables to check for different discounts
    self.boolStudentOrSenCitz = False
    self.boolQuantityDiscount = False
    
    # Asking for Student or Senior Citizen
    print("Are you a Student or a Senior Citizen? \nPress Y if yes\nPress N for No")
    studentOrSenCitz = input()

    if studentOrSenCitz == "Y" or studentOrSenCitz == "y":
      finalPriceshirt = totalPriceshirt - (totalPriceshirt*0.1)
      finalPricePants = totalPricePants - (totalPricePants*0.1)
      self.boolStudentOrSenCitz = True 
    else:
      pass

    # Checking for Quantity Discount
    if self.pantsAttributes[2] > 3:
      finalPricePants = finalPricePants - (totalPricePants*0.15)
      self.boolQuantityDiscount = True
    
    
    if self.shirtAttributes[2] > 3:
      finalPriceshirt = finalPriceshirt - (totalPriceshirt*0.15)
      self.boolQuantityDiscount = True

    return finalPriceshirt, finalPricePants

  # FUnction for calculating total price
  def calcTotal(self):
    pricelist = self.calcDiscount()
    total = pricelist[0] + pricelist[1] 
    total = total + (total*0.13)
    return total

  # Function for providing Summary
  def summary(self):
    shirtcolor = ""
    shirttype = ""
    pantscolor = ""
    pantstype = ""

    if self.shirtAttributes[0] == 1:
      shirttype = "Polo T-shirt"
    elif self.shirtAttributes[0] == 2:
      shirttype = "Round Neck T-shirt"

    if self.shirtAttributes[1] == 1:
      shirtcolor = "Blue"
    elif self.shirtAttributes[1] == 2:
      shirtcolor = "Green"
    elif self.shirtAttributes[1] == 3:
      shirtcolor = "Red"

    if self.pantsAttributes[0] == 1:
      pantstype = "Cargo Pants"
    elif self.pantsAttributes[0] == 2:
      pantstype = "Jeans"

    if self.pantsAttributes[1] == 1:
      pantscolor = "Beige"
    elif self.pantsAttributes[1] == 2:
      pantscolor = "Black"
    elif self.pantsAttributes[1] == 3:
      pantscolor = "Blue"
    
    
    cost = self.calcTotal()
    # Printing Summary
    print("\n")
    print("------------------------------------------","\n" ,self.shirtAttributes[2], " ", shirtcolor, " ",shirttype,"\n", self.pantsAttributes[2], " ", pantscolor, " ", pantstype)
    if self.boolStudentOrSenCitz:
      print("Student/Senior Citizen Discount: 10%")
    if self.boolQuantityDiscount:
      print("Quantity Discount: 15%")
    print("Total cost: $", cost)
    print("------------------------------------------")
  

objectCalculate = Calculate()
objectCalculate.summary()

