import datetime
import logging

class Product:
    def __init__(self, name, location, quantity, expiration_date):
        self.name = name
        self.location = location
        self.quantity = quantity
        self.expiration_date = expiration_date
        
    def __repr__(self):
        return f'{self.name} ({self.quantity}) - expires {self.expiration_date}'

class Fridge:
    def __init__(self):
        self.products = []
        self.logger = logging.getLogger(__name__)
        
    def add_product(self, product):
        self.products.append(product)
        self.logger.info(f'{product.name} added to the fridge')
            
    def remove_product(self, product):
        self.products.remove(product)
        self.logger.info(f'{product.name} removed from the fridge')
            
    def list_products(self):
        for product in self.products:
            print(product)
            
    def list_expired_products(self):
        now = datetime.datetime.now()
        for product in self.products:
            if product.expiration_date < now:
                print(product)
                self.logger.info(f'{product.name} expired and listed')

    def list_expiring_soon_products(self):
        now = datetime.datetime.now()
        for product in self.products:
            if product.expiration_date < now + datetime.timedelta(days=1):
                print(product)
                self.logger.info(f'{product.name} expiring soon and listed')

def add_product(fridge):
    name = input('Enter product name: ')
    location = input('Enter product location: ')
    try:
        quantity = int(input('Enter product quantity: '))
    except ValueError:
        print('Error: quantity must be a number')
        return
    try:
        expiration_date = datetime.datetime.strptime(input('Enter product expiration date (YYYY-MM-DD): '), '%Y-%m-%d')
    except ValueError:
        print('Error: invalid date format')
        return
    product = Product(name, location, quantity, expiration_date)
    fridge.add_product(product)
    print(f'{product.name} added to the fridge')

def remove_product(fridge):
    name = input('Enter product name: ')
    for product in fridge.products:
        if product.name == name:
            fridge.remove_product(product)
            print(f'{product.name} removed from the fridge')
            return
    print(f'Error: product {name} not found')

def list_products(fridge):
    fridge.list_products()

def list_expired_products(fridge):
    fridge.list_expired_products()

def list_expiring_soon_products(fridge):
    fridge.list_expiring_soon_products()





def main():
    logger = logging.getLogger(__name__) 
    logging.basicConfig(level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')
    handler = logging.FileHandler('fridge.log')
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
                    
    fridge = Fridge()
    while True:
        action = input('---FRIDGE--- \n1.add \n2.remove \n3.list \n4.expired \n5.expiring \n6.close:\n ')
        if action == '1':
            add_product(fridge)
        elif action == '2':
            remove_product(fridge)
        elif action == '3':
            list_products(fridge)
        elif action == '4':
            list_expired_products(fridge)
        elif action == '5':
            list_expiring_soon_products(fridge)
        elif action == '6':
            break

if __name__ == '__main__':
     main()