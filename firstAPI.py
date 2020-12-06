'''
Api Usage >>>

'/products'                                 => Get All Products
'/add/(product name,type,price,quantity)'   => Add New Product
'/delete/(id)'                              => Delete A Product by id
'/product/(id)'                             => Get A Product by id

NOTE --> product id's start at 0

'''

# <---------------- script start --------------------->

from flask import Flask
from flask_restful import Resource,Api

# app init
app = Flask(__name__)

app.config['SECRET_KEY'] = 'SECRET'
api = Api(app)

index = 0

# initial product inventory
products = []


# <--------------- product classes -------------------->

# GET ALL PRODUCTS
class Product(Resource):

    def get(self):
        return {'products' : products} 


# EDIT PRODUCTS
class EditProduct(Resource):

    # add new product #
    def post(self,name,typ,price,qty):

        global index

        product =  {
            'id':index,
            'name':name,
            'type':typ,
            'price':price,
            'qty':qty
        }
        products.append(product)
        index +=1

        return {"Product added" : product}

    # remove product by id #
    def delete(self,id):

        for index,product in enumerate(products):
            if product['id'] == id:
                prod  = products.pop(index)
                return {"Product removed" : prod}

        return {"Product" : None},404

    # get product by id #
    def get(self,id):

        for product in products:
            if product['id'] == id:
                return {"Product" : product}
        
        return {"Product" : None},404


# <--------------- adding resources  ------------------->

# view all products
api.add_resource(Product,'/products')

# edit products
api.add_resource(EditProduct,'/add/<string:name>/<string:typ>/<string:price>/<string:qty>','/delete/<int:id>','/product/<int:id>')



# <--------------------- run app ----------------------->
if __name__ == '__main__':
    app.run(debug=True)