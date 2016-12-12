
import os 
import json 
import re 
import operator
from pymongo import MongoClient
from bson import Binary, Code
from bson.son import SON 
DATABASENAME = 'kiranreddy92' 
client = MongoClient('localhost', 27017) 
db = client[DATABASENAME] 
X = 89122 
Y = 89117
if raw_input("Run find 5 star reviews?: ") == 'y':
    search_zip_codes = {'full_address':{'$regex': "89122" + "|" + "89117"}} 
    result = db.yelp.business.find(search_zip_codes).count()
    print(result)
print"\n"

if raw_input("find all the restaurents in city X?: ") == 'y':
    X = str(raw_input("Enter name of the city: ")) 
    search_city = {'city':{'$regex':X,'$options':'-i'}} 
    result=db.yelp.business.find(search_city).count()
    print(result) 
print"\n"
    
if raw_input("Find the restaurants within 5 miles of lat , lon:") == 'y': 
    restuarants = {"loc":{ "$geoWithin":{ "$center":[ [ -80.839186,35.226504] , .004 ] } }}
    result=db.yelp.business.find(restuarants).count()
    print(result)
print"\n"
    
if raw_input("Find all the reviews for restaurant X:") == 'y':
    review = raw_input("Enter business id for the review: ") 
    review_count={'business_id':review} 
    result=db.yelp.review.find(review_count).count() 
    print(result) 
print"\n"


    
if raw_input("Find all the reviews for restaurant X that are 5 stars :") == 'y':    
	review = raw_input("Enter business id for the review: ") 
	result=db.yelp.review.find({"business_id":review ,"stars":5}).count() 
	print(result)
print"\n"


	
if raw_input("Find all the users that have been 'yelping' for over 5 years :") == 'y': 
   yelp={"yelping_since" : { "$gt" : "2011-07"}}
   result = db.yelp.user.find(yelp).limit(20)
   for i in result:
        print(i)
print"\n"

   
if raw_input("Find the business that has the tip with the most likes :") == 'y': 
   result = db.yelp.tip.find().sort('likes',-1).limit(1)
   for i in result:
        print(i)
print"\n"


if raw_input("Find the average review_count for users :") == 'y': 
   result = db.yelp.user.aggregate([{"$group": {"_id":0, 'avg_review_count': {"$avg":"$review_count"} } }])
   for i in result:
   		print(i)
print"\n"
   
if raw_input("Find all the users that are considered elite :") == 'y': 
   result = db.yelp.user.find({"elite":{"$ne":[]}},{"_id":0,"user_id":1,"name":1,"elite":1}).count()
   print(result)
print"\n"
  
if raw_input("Find the longest elite user :") == 'y': 
   result = db.yelp.user.aggregate( [{ "$unwind" : "$elite" },{ "$group" : { "_id" : "$_id", "duration" : { "$sum" : 1 }} },{ "$sort" : { "duration" : -1 } },{ "$limit" : 1 }] )
   for i in result:
        print(i)
print"\n"
   
if raw_input("Find Of elite users, whats the average number of years someone is elite :") == 'y': 
   result = db.yelp.user.aggregate([{"$group":{"_id":0,"average":{"$avg":{"$size":"$elite"}}}},{ "$limit" : 1 }])
   for i in result:
        print(i)








   
	
