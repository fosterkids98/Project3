from app import *
from base_class import *


"""=============  user Methods  ==============="""

#CREATE USER
@app.route('/users', methods=['POST'])
def create_user():
    try:
        user_data = user_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    unique_email = user_data.get('email')
    existing_user = db.session.query(User).filter_by(email=unique_email).first()
    
    if existing_user:
        return jsonify({"message": "User already exists under this email"}), 400
    
    new_user = User(name=user_data['name'], email=user_data['email'], address=user_data['address'])
    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user), 200

#RETRIEVE ALL USERS
@app.route('/users', methods=['GET'])
def get_users():
    
    users = db.session.query(User).all()

    return users_schema.jsonify(users), 200

#RETRIEVE ONE USER
@app.route('/users/<int:id>', methods=['GET'])
def get_user(user_id):
    user = db.session.get(User, user_id)
    if not user:
        return jsonify({"message": f"No user under user id# {user_id} found"}), 400
    return user_schema.jsonify(user), 200

#UPDATE USER
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user= db.session.get(User, user_id)
    
    if not user:
        return jsonify({"message": "invalid user id"}), 400
    
    try:
        user_data = user_schema.load(request.json)
    except ValidationError as e:
        return jsonify({e.messages}), 400
    
    user.name = user_data['name']
    user.email = user_data['email']
    user.address = user_data['address']
    db.session.commit()
    return user_schema.jsonify(user), 200

#DELETE USER
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(user_id):
    user = db.session.get(User, user_id)

    if not user:
        return jsonify({"message": "invalid user id"}), 400
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": f"successfuly deleted user {user_id}"}), 200


"""=================  Order Methods  ================"""
#CREATE ORDER   
@app.route('/orders', methods=['POST'])
def create_order():
    order_data = request.get_json() 

   
    order_user_id = order_data.get('user_id') 
    

    
    user = db.session.get(User,order_user_id)
    if not user:
        return jsonify({'error': 'user not found'}), 404
    
    new_order = Order(user_id=order_user_id)
    
    db.session.add(new_order)
    db.session.commit()

    return jsonify({'message': 'Order created successfully', 'order_id': new_order.id}), 200

#ADD PRODUCT TO AN ORDER
@app.route('/orders/<int:order_id>/add_product/<int:product_id>', methods=['POST'])
def add_item_to_order(order_id, product_id):
    order = db.session.get(Order, order_id)
    
    if not order:
        return jsonify({"message": "Invalid order id"}), 400
    
    product = db.session.query(Item).filter_by(id=product_id).first()
    
    if not product:
        return jsonify({"message": "Product not found"}), 400
    existing_order_item = db.session.query(OrderItem).filter_by(order_id=order_id, item_id=product_id).first()
    if existing_order_item:
        return jsonify({"message": f"Product {product_id} already exists in this order."}), 400
    
    order_item = OrderItem(order_id=order_id, item_id=product_id)
    db.session.add(order_item)
    db.session.commit()
    
    return jsonify({"message": f"Product #{product_id} added to order {order_id}"}), 200

#DELETE PRODUCT FROM ORDER
@app.route('/orders/<int:order_id>/remove_product/<int:item_id>', methods=['DELETE'])
def delete_item_from_order(order_id,item_id):
    order = db.session.get(Order, order_id)
    
    if not order:
        return jsonify({"message": "Invalid order ID"}), 400
    
    order_item = db.session.query(OrderItem).filter_by(order_id=order_id, item_id=item_id).first()
    
    if not order_item:
        return jsonify({"message": "Item not found in this order"}), 400
    db.session.delete(order_item)
    db.session.commit()
    
    return jsonify({"message": f"Item #{item_id} removed from order {order_id}"}), 200

#GET A USERS ORDERS 
@app.route('/orders/users/<user_id>', methods=['GET'])
def get_user_orders(user_id):
    user = db.session.get(User, user_id)
    orders = user.orders
    if not user:
        return jsonify({'error': 'user not found'}), 400
    
    return orders_schema.jsonify(orders)

#GET ALL ITEMS FOR AN ORDER
@app.route('/orders/<order_id>/products', methods=['GET'])
def get_ordered_items(order_id):
    order = db.session.get(Order, order_id)
    if not order:
        return jsonify({'error': 'No such order exists'}),400

    ordered_items = db.session.query(OrderItem).filter_by(order_id=order.id).all()
    
    if not ordered_items:
        return jsonify({'error': 'No items found for this order'}), 400
    
    return order_items_schema.jsonify(ordered_items)
"""===============  Item Methods  ==============="""

#CREATE A PRODUCT
@app.route('/products', methods=['POST'])
def create_item():
    try:
        item_data = item_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    new_item = Item(name=item_data['name'], serial=item_data['serial'],
                    price=item_data['price'],description=item_data['description'])
    db.session.add(new_item)
    db.session.commit()

    return item_schema.jsonify(new_item), 200

#RETRIEVE ALL PRODUCTS
@app.route('/products', methods=['GET'])
def get_items():
    query = select(Item)
    items = db.session.execute(query).scalars().all()

    return items_schema.jsonify(items), 200

#RETRIEVE ONE PRODUCT
@app.route('/products/<int:id>', methods=['GET'])
def get_item(item_id):
    item = db.session.get(Item, item_id)
    if not item:
        return jsonify({"message": "Item not found"}), 400
    return item_schema.jsonify(item), 200

#UPDATE PRODUCTS
@app.route('/products/<int:id>', methods=['PUT'])
def update_item(item_id):
    item = db.session.get(Item, item_id)
    
    if not item:
        return jsonify({"message": "invalid user id"}), 400
    
    try:
        item_data = item_schema.load(request.json)
    except ValidationError as e:
        return jsonify({e.messages}), 400
    
    item.name = item_data['name']
    item.description = item_data['description']
    item.price = item_data['price']

    db.session.commit()
    return item_schema.jsonify(item), 200

#DELETE ITEM
@app.route('/products/<int:id>', methods=['DELETE'])
def delete_item(item_id):
    item = db.session.get(Item, item_id)

    if not item:
        return jsonify({"message": "invalid item id"}), 400
    db.session.delete(item)
    db.session.commit()
    return jsonify({"message": f"successfuly deleted item# {item_id}"}), 200