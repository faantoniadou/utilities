#%%
import pandas as pd
import numpy as np
import random
from random import randint, randrange
import secrets
import string
import sqlite3
import time
import datetime
from datetime import date, datetime

def str_time_prop(start, end, time_format, prop):
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))



def random_date(start, end, prop):
    return str_time_prop(start, end, '%Y-%m-%d %H:%M:%S', prop)



class UserDB:
    def __init__(self, no_users):
        self.no_users = no_users
        self.loc_index = None
        self.user_db = None

    def gen_password_data(self, pwd_length):
        letters = string.ascii_letters
        digits = string.digits
        special_chars = string.punctuation
        alphabet = letters + digits + special_chars

        pwd = ''.join(secrets.choice(alphabet) for i in range(pwd_length))
        
        return pwd


    def gen_first_name_data(self):
        firstName = np.random.choice(['Adam', 'Bob', 'Charlie', 'David', 'Ethan', 'Frank', 'George', 'Harry', 'Ian', 'Jack', 'Kevin', 'Liam', 'Michael', 'Nathan', 'Aidyn', 'Raphael', 'Quentin', 'Richard', 'Sam', 'Thomas', 'Ulysses', 'Victor', 'William', 'Xavier', 'Yan', 'Zachary',
                                    'Alice', 'Bella', 'Catherine', 'Daisy', 'Phaedra', 'Fiona', 'Grace', 'Hannah', 'Luigi', 'Jessica', 'Katherine', 'Lily', 'Mia', 'Nikitas', 'Olivia', 'Penelope', 'Rachel', 'Sophia', 'Victoria', 'Wendy', 'Xenia', 'Yvonne', 'Josh',
                                    'Ava', 'Amelia', 'Charlotte', 'Emily', 'Isla', 'Kamala', 'Aria', 'Aurora', 'Evelyn', 'Genevieve', 'Harper', 'Luna', 'Maya', 'Nora', 'Riley', 'Jannik', 'Violet', 'Zoey',
                                    'Dominick', 'Otto', 'Ryker', 'Sawyer', 'Silas', 'Theodore', 'Tucker', 'Wesley', 'Weston', 'Xander', 'Auro', 'Alexander', 'Asher', 'Benjamin', 'Carter', 'Daniel', 'Elijah', 'Ayesha', 'Gabriel', 'Henry', 'James', 'Jacob', 'Jayden', 'John', 'Joseph', 
                                    'Joshua', 'Odysseus', 'Logan', 'Lucas', 'Mason', 'Yulu', 'Izzy', 'Noah', 'Oliver', 'Owen', 'Ryan', 'Samuel', 'Sebastian', 'Simon', 'Nikaros', 'Zeus', 'Aris', 'Kostas'
                                    'Angela', 'Barack', 'Boris', 'Donald', 'Emmanuel', 'Francois', 'Omiros', 'Gordon', 'Hilary', 'Jacinda', 'Jeremy', 'Joe', 'John', 'Justin', 'Kim', 'Margaret', 'Mikhail', 'Narendra', 'Nicola', 'Paul', 'Rajoy', 'Raul', 'Ricardo', 
                                    'Rohani', 'Rutte', 'Sadiq', 'Salman', 'Shinzo', 'Theresa', 'Vladimir', 'Xi', 'Yoshihide', 'Zuma'], 1)
        return firstName


    def gen_last_name_data(self):
        lastName = np.random.choice(['Miers', 'Jones', 'Smith', 'Williams', 'Brown', 'Taylor', 'Davies', 'Evans', 'Wilson', 'Thomas', 'Roberts', 'Johnson', 'Lewis', 'Walker', 'Robinson', 'Wood', 
                                    'Thompson', 'White', 'Watson', 'Jackson', 'Wright', 'Green', 'Harris', 'Cooper', 'King', 'Lee', 'Martin', 'Clarke', 'James', 'Morgan', 'Hughes', 'Edwards', 
                                    'Hill', 'Moore', 'Clark', 'Harrison', 'Scott', 'Young', 'Morris', 'Hall', 'Ward', 'Turner', 'Carter', 'Phillips', 'Mitchell', 'Patel', 'Adams', 'Campbell', 
                                    'Antoniadou','Sophocleous', 'Christodoulou', 'Levin', 'Kloecker', 'Hu', 'Zang', 'Mingxi', 'Zhang', 'Nai', 'Petheno', 'Kori', 'Edo', 'Lambert', 'Batminton', 'Xanthos', 'Pseftikos',
                                    'Koliandris', 'Exo', 'Oxi', 'Enixero', 'Kokkinou', 'Zhao', 'Bowel', 'Zantis', 'Kardashian', 'Omorfos', 'Zhu', 'Ofkeros', 'Huang', 'Earth', 'Ortiki', 'Zheng', 'Cheng', 'Malakas', 'Ikosi', 'Zhou', 'Chen',
                                    'Ashimos', 'Yang', 'Eki', 'Pitta', 'Xu', 'Mayong', 'Mars', 'Liu', 'Soler', 'Mesa', 'Wang', 'Li', 'Vlamis', 'Zhao', 'Petrou', 'Vrikkis', 'Kors', 'Wu', 'Vuitton', 'Elms', 'Styles', 'Sun',
                                    'Antoniou', 'Kamakakiwowe', 'Umukuwawo', 'Zumbupupate', 'Perez', 'Garcia', 'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Gonzalez', 'Perez', 'Garcia', 'Rodriguez',
                                    'Gaulle', 'Macron', 'Trudau', 'Merkel', 'Johnson', 'Boris', 'May', 'Trump', 'Obama', 'Clinton', 'Bush', 'Reagan', 'Carter', 'Nixon', 'Kennedy', 'Johnson', 'Eisenhower'], 1)
        return lastName



    def gen_address_data(self):
        addressNos = np.arange(80)

        addressNames = ['Olympiados', 'Pembridge', 'Hanover', 'Tottenham', 'Baker', 'Paradise', 'Palms', 'Beverly', 'Holy', 'Trinity', 'St. James', 
                        'St. James', 'Rankeillor', 'Chriseleousa', 'St. Peter', 'Princes', 'Tomorrow', 'Lochness', 'St. Andrew', 'South Bridge', 'Bread', 'St. Patrick', 'St. Joseph', 
                        'James Clerk Maxwell', 'Pollock', 'St. Philip', 'Alexander the Great', 'St. Matthew', 'Nicholson', 'Independence Day', 'St. Paul', 'Castle', 'Lord Kelvin', 'St. Mark', 'Quartermile', 
                        'Montague', 'Buccleuch', 'St. David', 'St. Patrick', 'West Bow', 'Elm', 'St. Thomas', 'Pleasance', 'Bristo', 'Chalmers']

        address = ['Street', 'Mews', 'Avenue', 'Boulevard', 'Road', 'Lane', 'Drive', 'Court', 'Place', 'Square', 'Terrace', 'Trail', 'Parkway', 'Commons', 'Villas']

        fulladdress = str(np.random.choice(addressNos)) + ' ' + np.random.choice(addressNames) + ' ' + np.random.choice(address)
        return fulladdress



    def gen_phone_data(self):
        country_code = ['+1', '+44', '+357', '+49', '+86', '+81', '+977', '+98', '+356', '+39', '+27', '+90', '+92',
                        '+91', '+976', '+60', '+379', '+34', '+212', '+972', '+30', '+51', '+1', '+52', '+370', '+375',
                        '+504', '+351', '+595', '+598', '+53', '+82', '+856', '+968', '+20', '+212', '+961', '+961', '+961']
        
        range_start = 10**(10-1)
        range_end = (10**10)-1
        phoneNo = randint(range_start, range_end)

        phone = np.random.choice(country_code) + ' ' + str(phoneNo)

        return phone



    def gen_username_data(self, firstName, lastName):
        name = firstName + lastName
        first_letter = name[0]
        three_letters_surname = name[-1][:3].rjust(3, 'x')
        number = '{:03d}'.format(random.randrange(1, 999))
        username = '{}{}{}'.format(first_letter, three_letters_surname, number)
        
        return username



    def gen_email_data(self):
        email = ['gmail', 'yahoo', 'hotmail', 'outlook', 'cablenet', 'aon', 'eduroam']
        domain = ['com', 'co.uk', 'org', 'net', 'edu', 'gov', 'mil']
        email_address = '@' + np.random.choice(email) + '.' + np.random.choice(domain)
        return email_address


    def gen_user_dummy_data(self):
        countries_list = ['United States', 'United Kingdom','United Kingdom', 'Cyprus', 'Germany', 'China', 'Japan', 'Nepal', 'Iran',
                        'Malta', 'Italy', 'South Africa', 'Turkey', 'Pakistan', 'India', 'Mongolia', 'Malaysia',
                        'Vatican City', 'Spain', 'Morocco', 'Israel', 'Greece', 'Peru', 'Canada', 'Mexico',
                        'Libya', 'Chad', 'Lesotho', 'United Arab Emirates', 'Qatar', 'Australia', 'New Zealand',
                        'Austria', 'Switzerland', 'France', 'Sweden', 'Finland', 'Norway', 'Denmark', 'Netherlands',
                        'Monaco', 'San Marino', 'Ecuador', 'Venezuela', 'Panama', 'Honduras', 'Portugal', 'Paraguay',
                        'Uruguay', 'Cuba', 'South Korea', 'Laos', 'Oman', 'Egypt', 'Algeria', 'Lebanon']

        cities_list = ['New York', 'Edinburgh', 'London', 'Nicosia', 'Berlin', 'Beijing', 'Tokyo', 'Kathmandu', 'Tehran',
                        'Valletta', 'Florence', 'Cape Town', 'Ankara', 'Islamabad', 'New Delhi', 'Ulaanbaatar', 'Kuala Lumpur',
                        'Vatican City', 'Madrid', 'Rabat', 'Jerusalem', 'Thessaloniki', 'Lima', 'Ottawa', 'Mexico City',
                        'Tripoli', 'N\'Djamena', 'Maseru', 'Abu Dhabi', 'Doha', 'Sydney', 'Wellington',
                        'Vienna', 'Bern', 'Paris', 'Stockholm', 'Helsinki', 'Oslo', 'Copenhagen', 'Amsterdam',
                        'Monaco', 'San Marino', 'Quito', 'Caracas', 'Panama City', 'Tegucigalpa', 'Lisbon', 'Asuncion',
                        'Montevideo', 'Havana', 'Seoul', 'Vientiane', 'Muscat', 'Cairo', 'Algiers', 'Beirut']
        
        self.loc_index = np.random.choice(np.arange(len(countries_list)), self.no_users)

        self.user_db = pd.DataFrame({
            'userID': np.arange(1,self.no_users+1),
            'firstName': [self.gen_first_name_data()[0] for i in range(self.no_users)],
            'lastName' : [self.gen_last_name_data()[0] for i in range(self.no_users)],
            'phoneNumber': [self.gen_phone_data() for i in range(self.no_users)], 
            'country': [countries_list[i] for i in self.loc_index],
            'city': [cities_list[i] for i in self.loc_index],
            'password': [self.gen_password_data(12) for i in range(self.no_users)],
            'address': [self.gen_address_data() for i in range(self.no_users)],
            'postcode': np.random.choice(['10001', '10002', '10003', '10004', '10005', '10006', '10007', '10008', '2064', '10010',
                                        'W1A 1AA', 'W1A 1AB', 'W1A 1AD', 'W1A 1AE', 'W1A 1AF', 'W1A 1AG', 'W1A 1AH', 'W1A 1AJ', 
                                        'G1 1AA', 'G1 1AB', 'G1 1AD', 'G1 1AE', 'G1 1AF', 'G1 1AG', 'G1 1AH', 'G1 1AJ', 'G1 1AL', 
                                        'HG1 1BB', 'HG1 1BD', 'HG1 1BE', 'HG1 1BF', 'HG1 1BG', 'HG1 1BH', 'HG1 1BJ', 'HG1 1BP'], self.no_users),
            'isAdmin' : np.zeros(self.no_users),                           
            })

        self.user_db.insert(3, 'username', [self.gen_username_data(self.user_db['firstName'][i], self.user_db['lastName'][i]) for i in range(self.no_users)])
        self.user_db.insert(4, 'email', [self.user_db['username'][i] + self.gen_email_data() for i in range(self.no_users)])
        self.user_db.head()
        return self.user_db



class CategoriesDB:
    # This class generates dummy data for the categories table in the database
    def __init__(self):
        self.categ_db = None

    def create_categories_db(self):
        data = {'categoryName': ['Books', 'Sports', 'Clothes', 'Jewelry', 'Furniture', 'Kitchen', 'Electronics', 'Other'],
                'categoryDescription': ['', '', '', '', '', '', '', '']}

        self.categ_db = pd.DataFrame(data, columns= ['categoryName', 'categoryDescription'])
       
        return self.categ_db

class ConditionsDB:
    # This class generates dummy data for the conditions table in the database
    def __init__(self):
        self.cond_db = None

    def create_conditions_db(self):
        data = {'conditionName': ['New', 'Light Defects', 'Broken', 'Other', 'Significant Defects', 'Damaged'],
                'conditionDescription': ['', '', '', '', '', '']}

        self.cond_db = pd.DataFrame(data, columns= ['conditionName', 'conditionDescription'])
       
        return self.cond_db

class AuctionDB(UserDB, CategoriesDB):
    def __init__(self, no_users, no_auctions, categ_df):
        self.auctions_db = None
        self.auctionID = None
        self.no_auctions = no_auctions
        self.item_indices = np.random.choice(np.arange(0, self.no_auctions), self.no_auctions)

        CategoriesDB.__init__(self)
        UserDB.__init__(self, no_users=no_users)

        self.categ_db = categ_df
        self.user_df = user_df



    def auction_start_date(self):        
        return random_date('2022-11-16 18:54:55', (datetime.today().strftime('%Y-%m-%d %H:%M:%S' )), random.random())
    

    def auction_end_date(self):        
        return random_date((datetime.today().strftime('%Y-%m-%d %H:%M:%S' )), '2022-11-29 18:54:55', random.random())


    def create_auctions_data(self):
        titles = ['Electric kettle', 'Pizza roller', 'Ice cream maker', 'Toaster', 'Coffee machine', 'Juicer', '3L Blender', 'Hand mixer',
                'Golf club bag', '1980s Tennis racket', 'Baseball bat', 'NBA Basketball', 'Children\'s Football', 'Volleyball net', 'Skaterboy Skateboard',
                'Antique Pearl necklace', 'Gold wedding ring', 'Seashell bracelet', 'Silver earrings', 'Gold necklace', 'My grandma\'s Amethyst ring',
                'Macbook Pro M2 256GB, 16GB RAM', 'iPhone 14 Pro Max - Red', 'Samsung Galaxy IIII with case included', 'Sony M4 Headphones', 'Bose Waterproof Speaker',
                'The Lord of the Rings', 'Harry Potter Full Series', 'The Chronicles of Narnia', 'The Hobbit', 'The Hunger Games Trilogy', 'Animal Farm', 'Twilight Saga',
                'Wooden Wardrobe', 'IKEA Bed Frame', 'Swedish Coffee table', 'German Silk Curtains', '7 Dreams Mattress', 'Pack of 7 Outdoors Plalstic Chairs',
                'Outdoor Inflatable Pool', 'Limited Edition Toblerone Chocolate', 'Countryside Bird Feeder', 'Persian Bath Soaps - many scents', 'Dry Lavender Sack', 'Monopoly Global Special Edition',
                'Burberry Womens Beige Jacket without tags', 'Levis Bootcut Womens Jeans', 'Jack Wills Grey Logo Hoodie Unisex', 'Unbraded Heeled Womens Sandals Size EU38', 'Mens Black Leather Jacket', 'Mens Black Leather Boots Size EU42']

        categories = ['Kitchen', 'Kitchen', 'Kitchen', 'Kitchen', 'Kitchen', 'Kitchen', 'Kitchen', 'Kitchen',
                    'Sports', 'Sports', 'Sports', 'Sports', 'Sports', 'Sports', 'Sports', 
                    'Jewelry', 'Jewelry', 'Jewelry', 'Jewelry', 'Jewelry', 'Jewelry', 
                    'Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics',
                    'Books', 'Books', 'Books', 'Books', 'Books', 'Books', 'Books', 
                    'Furniture', 'Furniture', 'Furniture', 'Furniture', 'Furniture', 'Furniture',  
                    'Other', 'Other', 'Other', 'Other', 'Other', 'Other',
                    'Clothes', 'Clothes', 'Clothes', 'Clothes', 'Clothes', 'Clothes']


        price_array = np.round(np.array(random.choices(np.arange(1, 10000)/100, weights=np.exp((np.arange(1, 10000)/100))[::-1], k=self.no_auctions)),2)


        self.auctions_db = pd.DataFrame({
            'auctionID' : np.arange(self.no_auctions),
            'userID': np.random.choice(self.user_df['userID'], self.no_auctions),
            'categoryName': [categories[self.item_indices[i]%len(categories)] for i in range(self.no_auctions)],
            'conditionName': np.random.choice(['New', 'Light Defects', 'Broken', 'Other', 'Significant Defects', 'Damaged'], self.no_auctions),
            'createdAt': [self.auction_start_date() for i in range(self.no_auctions)],
            'endAt': [self.auction_end_date() for i in range(self.no_auctions)],
            'startPrice': price_array,
            'reservePrice': np.round(price_array + np.round(np.random.uniform(0, 100, self.no_auctions), 2),2),
            'title': [titles[self.item_indices[i]%len(titles)] for i in range(self.no_auctions)],
            'description': ['A very good ' + titles[self.item_indices[i]%len(titles)] + '.' for i in range(self.no_auctions)],
            'imageLink': [''] * self.no_auctions,
            'views': np.random.choice(np.arange(0, 301), self.no_auctions),
            })

        isActive = np.empty(self.no_auctions)

        # deterime whether auction is active or not
        for i in range(self.no_auctions):
            if self.auctions_db['endAt'][i] > datetime.today().strftime('%Y-%m-%d %H:%M:%S' ):
                isActive[i] = 1
            else:
                isActive[i] = 0

        self.auctions_db.insert(6, 'isActive', isActive)

        return self.auctions_db



class BidsDB(AuctionDB, UserDB):
    def __init__(self, no_bids, no_auctions, no_users, user_df, categ_df):
        self.bids_db = None
        self.no_bids = no_bids
        self.user_df = user_df

        AuctionDB.__init__(self, no_users=no_users, no_auctions=no_auctions, categ_df=categ_df)
        UserDB.__init__(self, no_users=no_users)


    def create_bids_data(self, auctions_db):
        self.auctionID =  np.random.choice(auctions_db['auctionID'][1:], self.no_bids)

        self.bids_db = pd.DataFrame({
            'bidID': np.arange(1, 1+self.no_bids),
            'auctionID': self.auctionID,
            })

        userIDs = np.empty(self.no_bids)
        bidAt = []

        for i in range(self.no_bids):
            # get userIDs of the users who do not own the auction
            userIDs[i] = np.random.choice(self.user_df['userID'][self.user_df['userID'] != auctions_db['userID'][self.auctionID[i]]])
            
            # set bid time to be between auction start and end time
            bidAt.append(random_date(auctions_db['createdAt'][self.auctionID[i]], auctions_db['endAt'][self.auctionID[i]], random.random()))
            
        self.bids_db.insert(1, 'userID', userIDs)
        self.bids_db.insert(3, 'bidAt', bidAt)

        # set bid price to be between start price and reserve price
        self.bids_db.insert(3, 'bidPrice', np.round(np.random.uniform(auctions_db['startPrice'][self.auctionID], auctions_db['reservePrice'][self.auctionID], self.no_bids), 2))
        
        return self.bids_db
    

    def determine_sold_status(self, no_auctions, auctions_db):
        self.bids_db = self.create_bids_data(auctions_db)
        isSold = np.empty(no_auctions)

        # determine number of bids for each auction
        for i in range(no_auctions):
            if np.any(self.auctionID == auctions_db['auctionID'][i]):
                isSold[i] = True
            else:
                isSold[i] = False
        
        auctions_db.insert(7, 'isSold', isSold)

        return auctions_db 





if __name__ == '__main__':
    no_users = 50
    no_auctions = 200
    no_bids = 300

    user_df = UserDB(no_users).gen_user_dummy_data()
    
    categ_df = CategoriesDB().create_categories_db()
    auction_df = AuctionDB(no_users, no_auctions, categ_df).create_auctions_data()
    bids_df = BidsDB(no_bids, no_auctions, no_users, user_df, categ_df).create_bids_data(auction_df)
    conditions_df = ConditionsDB().create_conditions_db()

    BidsDB(no_bids, no_auctions, no_users, user_df, categ_df).determine_sold_status(no_auctions, auction_df)  # inserts isSold column to auction_df


    with open('dummy_data.txt', 'w') as f:
        conn = sqlite3.connect('db_cw')
        c = conn.cursor()


        c.execute('CREATE TABLE IF NOT EXISTS users (userID number, username text, email text, password text, firstName text, lastName text, phoneNumber text, country text, city text, address text, postcode text, isAdmin number)')
        user_df.to_sql('users', conn, if_exists='replace', index=False)
        conn.commit()
        c.execute('''  
        SELECT * FROM users
                ''')
        records = c.fetchall()
        
        f.write('INSERT INTO users (userID, firstName, lastName, username, email, phoneNumber, country, city, password, adresseLine, postcode, isAdmin) \nVALUES\n')
        for row in records:
            if row == records[-1]:
                f.write(str(row) +';\n\n')
            else:
                f.write(str(row) +',\n')

        
        c.execute('CREATE TABLE IF NOT EXISTS conditions (conditionName text, conditionDescription text)')
        conditions_df.to_sql('conditions', conn, if_exists='replace', index=False)
        conn.commit()
        c.execute('''
        SELECT * FROM conditions
                ''')
        records = c.fetchall()

        f.write('INSERT INTO conditions (conditionName, conditionDescription) \nVALUES\n')
        for row in records:
            if row == records[-1]:
                f.write(str(row) +';\n\n')
            else:
                f.write(str(row) +',\n')



        c.execute('CREATE TABLE IF NOT EXISTS categories (categoryID number, categoryName text)')
        categ_df.to_sql('categories', conn, if_exists='replace', index=False)
        conn.commit()
        c.execute('''
        SELECT * FROM categories
                ''')
        records = c.fetchall()
        
        f.write('INSERT INTO categories (categoryName, categoryDescription) \nVALUES\n')
        for row in records:
            if row == records[-1]:
                f.write(str(row) +';\n\n')
            else:
                f.write(str(row) +',\n')




        c.execute('CREATE TABLE IF NOT EXISTS auctions (auctionID number, userID number, categoryName text, conditionName text, createdAt text, endAt text, \
            isActive number, isSold number, startPrice number, reservePrice number, title text, description text, imageLink text, views number)')
        auction_df.to_sql('auctions', conn, if_exists='replace', index=False)
        conn.commit()
        c.execute('''
        SELECT * FROM auctions
                ''')
        records = c.fetchall()
        
        f.write('INSERT INTO auctions (auctionID, userID, categoryName, conditionName, createdAt, endAt, isActive, isSold, startPrice, reservePrice, title, description, imageLink, views) \nVALUES\n')
        for row in records:
            if row == records[-1]:
                f.write(str(row) +';\n\n')
            else:
                f.write(str(row) +',\n')
        


        c.execute('CREATE TABLE IF NOT EXISTS bids (bidID number, userID number, auctionID number, amount number, bidAt date)')
        bids_df.to_sql('bids', conn, if_exists='replace', index=False)
        conn.commit()
        c.execute('''
        SELECT * FROM bids
                ''')
        records = c.fetchall()

        f.write('INSERT INTO bids (bidID, userID, auctionID, amount, bidAt) \nVALUES\n ')
        for row in records:
            if row == records[-1]:
                f.write(str(row) +';\n\n')
            else:
                f.write(str(row) +',\n')


        f.close()

