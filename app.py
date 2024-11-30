

from base_class import *
from methods_api import *





class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Order

class ItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Item

class OrderItemSchema(ma.SQLAlchemyAutoSchema):
    order_id = fields.Int()
    product_id = fields.Int()
       
    product_name = fields.Method('get_product_info')

    def get_product_info(self, order_item):
        return order_item.product.name if order_item.product else None
    product_price = fields.Method('get_product_price')

    def get_product_price(self, order_item):
        return order_item.product.price if order_item.product else None

user_schema = UserSchema()
users_schema = UserSchema(many=True)
order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)
item_schema = ItemSchema()
items_schema = ItemSchema(many=True)
order_item_schema = OrderItemSchema()
order_items_schema = OrderItemSchema(many=True)



if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)