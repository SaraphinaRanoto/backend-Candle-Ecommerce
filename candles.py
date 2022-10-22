import dbClass

class Product:
   price = 100
   def __init__(self, prod_name, prod_id, quantity, prod_color):
    self.prod_name =  prod_name
    self.prod_id = prod_id
    self.quantity = quantity
    self.prod_color = prod_color
   
    
   def getProdname(self):
    return self.prod_name + "  "+ self.prod_id  + " " + self.prod_color                    #+ " " + self.quantity gives error

   def getQuantity(self):
    return self.quantity

   def getEverything(self):
    return{
        "quantity": self.quantity,
        "prod_name": self.prod_name,
        "prod_id": self.prod_id, 
        "prod_color": self.prod_color
        }

def printProductInfo(productNum, p):
 print("Product", productNum, p.getProdname(), "are", p.getQuantity(),"in the shopping basket")
 return

pTable = dbClass.candlesTable

def insertProduct(p):
    columns = "id_num, candle_name, candle_color, quantity, price"
    values = " %d, '%s','%s', %d, %f" % ( p.prod_id, p.prod_name, p.prod_color, p.quantity, p.price)
    pTable.insert(columns, values)

#ERROR ON LINE 34 TO BE FIXED AFTER!!!!

product = []
count = 2
curr_count = 0

while True:
    prod_id = int(input("Product Number: "))
    prod_name = input("Product Name: ")
    prod_color = input("Candle Color: ")
    quantity = int(input("Quantity: "))
    price = float(input("Purchase Price:R "))
 
    temp_product = Product(prod_id, prod_name, prod_color, quantity)
    product.append(temp_product)
 
    curr_count += 1

    if(curr_count == count):
          break

for index,p in enumerate(product):
    insertProduct(p)
  




