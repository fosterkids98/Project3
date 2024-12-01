#Flask_API_DB Module 3 Project


A simple api for storing User, Orders & Products in a database.


#Functions

#-User Functions

--Create User

  --Endpoint: /users

      -name
      
      -email
      
      -address

  --Method: POST
  

--Retrieve all Users

  --Endpoint: /users
  
  --Method: GET
  

--Retrieve one User

  --Endpoint: /users
  
  --Method: GET

  
--Update User info
  
  --Endpoint: /users/<int:user_id>
  
    -name
    
    -email
    
    -address
  
  --Method: PUT


--Delete a User

  --Endpoint: /users/<int:user_id>
  
  --Method: DELETE



#Order Functions

--Create Order

  --Endpoint: /orders
  
    -user_id
  
  --Method: POST


--Add a Product to an Order

  --Endpoint: /orders/<int:order_id>/add_product/<int:product_id>
  
  --Method: POST


--Remove a Product from an Order

  --Endpoint: /orders/<int:order_id>/remove_product/<int:item_id>
  
  --Method: DELETE


--Get all Orders for a User

  --Endpoint: /orders/users/<user_id>
  
  --Method: GET


--Get all Products from an Order

  --Endpoint: /orders/<order_id>/products
  
  --Method: GET



#Product Functions

--Creat Products in list format

  --Endpoint: /product_list
  
    [
    
      {
      
        "serial": serial
        
        "name": "name"
        
        "price": 00.00
        
        "description": "description"
      
      },
      
      {
      
        "serial": serial
        
        "name": "name"
        
        "price": 00.00
        
        "description": "description"
      
      }
      
      ]
  
  --Method: POST

  
--Create a Product
  
  --Endpoint: /products
  
    -serial
    
    -name
    
    -price
    
    -description
  
  --Method: POST


--Retrieve all Products

  --Endpoint: /products
  
  --Method: GET


--Retrieve one Product

  --Endpoint: /products/<int:id>
  
  --Method: GET


--Update a Product listing

  --Endpoint: /products/<int:id>
  
  --Method: PUT


--Delete a Product listing

  --Endpoint: /products/<int:id>
  
  --Method: DELETE







#EXAMPLE PRODUCTS  

for easier insertion into database use '/product_list' api method

[

  {
  
    "serial": "3001",
    
    "name": "Smartphone X200",
    
    "price": 599.99,
    
    "description": "A cutting-edge smartphone with a 6.5-inch OLED display, 128GB storage, and 5G capability."
    
  },
  
  {
  
    "serial": "7002",
    
    "name": "Wireless Headphones Pro",
    
    "price": 199.99,
    
    "description": "Noise-cancelling headphones with Bluetooth 5.0 and 30 hours of battery life."
    
  },
  
  {
  
    "serial": "2003",
    
    "name": "4K Ultra HD TV",
    
    "price": 899.99,
    
    "description": "A 55-inch 4K smart TV with HDR support and integrated streaming apps."
    
  },
  
  {
  
    "serial": "5004",
    
    "name": "Smartwatch 360",
    
    "price": 249.99,
    
    "description": "Fitness tracker and smartwatch with heart rate monitoring, GPS, and sleep tracking."
    
  },
  
  {
  
    "serial": "3005",
    
    "name": "Laptop Pro 15",
    
    "price": 1299.99,
    
    "description": "A high-performance laptop with a 15-inch Retina display, Intel i7 processor, and 16GB RAM."
    
  },
  
  {
  
    "serial": "9006",
    
    "name": "Electric Kettle X",
    
    "price": 39.99,
    
    "description": "1.7L electric kettle with fast boiling, auto shut-off, and stainless steel design."
    
  },

  {
  
    "serial": "1007",
    
    "name": "Cordless Vacuum Cleaner",
    
    "price": 159.99,
    
    "description": "Powerful cordless vacuum with multiple attachments and a HEPA filter for home cleaning."
  },
  
  {
  
    "serial": "6008",
    
    "name": "Portable Power Bank 10000mAh",
    
    "price": 29.99,
    
    "description": "Compact and powerful 10000mAh power bank for charging devices on the go."
  },
  
  {
  
    "serial": "5009",
    
    "name": "Bluetooth Smart Scale",
    
    "price": 49.99,
    
    "description": "Digital smart scale with Bluetooth connectivity to sync your weight data with your phone."
  },
  
  {
  
    "serial": "4010",
    
    "name": "Gaming Mouse RX500",
    
    "price": 59.99,
    
    "description": "Ergonomic gaming mouse with customizable RGB lighting, 8000 DPI sensor, and programmable buttons."
  }
  
]
