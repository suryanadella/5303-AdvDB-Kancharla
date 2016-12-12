

Added sandeep kollipara. Press backspace to remove.

Skip to content
Using Gmail with screen readers
Search



Your message has been sent.
Gmail
COMPOSE
Labels
Inbox (11,540)
Starred
Important
Sent Mail
Drafts (32)
Circles
[Imap]/Sent (1)
[Imap]/Trash (26)
citi demat
demat
Junk E-mail
Personal
Travel
More 
Hangouts

 
 
 
  More 
1 of 13,558  
 
Expand all Print all In new window
(no subject)
Inbox
x  
Trash
x 

kiran reddy		2:17 PM (1 hour ago)
db.yelp.user.aggregate([{"$group":{"_id":"$name","average":{"$avg":{"$size":"...

sandeep kollipara
Attachments3:17 PM (4 minutes ago)

to me 

Attachments area

kiran reddy <kiran.kancharla92@gmail.com>
3:20 PM (0 minutes ago)

to sandeep 
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

print "\n\n Difficult queries "

	
Click here to Reply or Forward
1 deleted message in this conversation. View message or delete forever.
3.9 GB (26%) of 15 GB used
Manage
Terms - Privacy
Last account activity: 0 minutes ago
Details
sandeep kollipara's profile photo
sandeep kollipara
Add to circles

Show details

from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
from flask_restful import reqparse
from flask import jsonify
from flask_cors import CORS, cross_origin

#from pymongo import MongoClient
import pymongo
from bson import Binary, Code
from bson.json_util import dumps
from bson.objectid import ObjectId

import datetime

import json
import urllib


import timeit

app = FlaskAPI(__name__)
CORS(app)

client = pymongo.MongoClient('localhost', 27017)
db = client['advdbms_kollipara']
businessdb = db['yelp.business']
review = db['yelp.review']
userdb = db['yelp.user']
tip = db['yelp.tip']

parser = reqparse.RequestParser()

"""=================================================================================="""
"""=================================================================================="""
"""=================================================================================="""


@cross_origin() # allow all origins all methods.
@app.route("/", methods=['GET'])
def index():
    """Print available functions."""
    func_list = {}
    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static':
            func_list[rule.rule] = app.view_functions[rule.endpoint].__doc__
    return func_list

   
"""1================================================================================="""

@app.route("/zip/<args>", methods=['GET'])
def zip(args):
    """hello"""
    args = myParseArgs(args)    
    args['zips']=args['zips']
    ziplist=args['zips'].split(",")
    zip1=ziplist[0]
    zip2=ziplist[1]
        
    data = []
    result = businessdb.find({'$or': [{'full_address':{'$regex': '.*'+zip1}},{'full_address':{'$regex': '.*'+zip2}}]},{"full_address":1,"_id":0})
    if 'start' in args.keys():
        args['start'] = int(args['start'])
    if 'limit' in args.keys():
        args['limit'] = int(args['limit'])

    data = [] 
    if 'start' in args.keys() and 'limit' in args.keys():
        result = businessdb.find({'$or': [{'full_address':{'$regex': '.*'+zip1}},{'full_address':{'$regex': '.*'+zip2}}]},{"full_address":1,"_id":0}).skip(args['start']).limit(args['limit'])
    elif 'start' in args.keys():
        result = businessdb.find({'$or': [{'full_address':{'$regex': '.*'+zip1}},{'full_address':{'$regex': '.*'+zip2}}]},{"full_address":1,"_id":0}).skip(args['start'])
    elif 'limit' in args.keys():
        result = businessdb.find({'$or': [{'full_address':{'$regex': '.*'+zip1}},{'full_address':{'$regex': '.*'+zip2}}]},{"full_address":1,"_id":0}).limit(args['limit'])
    else:
        result = businessdb.find({'$or': [{'full_address':{'$regex': '.*'+zip1}},{'full_address':{'$regex': '.*'+zip2}}]},{"full_address":1,"_id":0}).limit(50)
    for r in result:
        data.append(r)
        
    return {"All restaurants in the given zip codes":data}

"""2================================================================================="""
@app.route("/city/<args>", methods=['GET'])
def city(args):

    args = myParseArgs(args)
    city = args['city']
    data=[]
    
    if 'start' in args.keys():
        args['start'] = int(args['start'])
    if 'limit' in args.keys():
        args['limit'] = int(args['limit'])

    data = []
    
    
    if 'start' in args.keys() and 'limit' in args.keys():
        result = businessdb.find({'full_address':{'$regex': city}},{"full_address":1,"_id":0}).skip(args['start']).limit(args['limit'])
    elif 'start' in args.keys():
        result = businessdb.find({'full_address':{'$regex': city}},{"full_address":1,"_id":0}).skip(args['start'])
    elif 'limit' in args.keys():
        result = businessdb.find({'full_address':{'$regex': city}},{"full_address":1,"_id":0}).limit(args['limit'])
    else:
        result = businessdb.find({'full_address':{'$regex': city}},{"full_address":1,"_id":0}).limit(50)
    for r in result:
        data.append(r)
        
    return {"data":data}
"""3================================================================================="""

@app.route("/closest/<args>", methods=['GET'])
def closest(args):
    args = myParseArgs(args)
    if 'lat' in args.keys():
        lat=float(args['lat'])

    if 'lon' in args.keys():
        lon=float(args['lon'])
        
    if 'start' in args.keys():
        args['start'] = int(args['start'])
    if 'limit' in args.keys():
        args['limit'] = int(args['limit'])

    data = []
    
    
    if 'start' in args.keys() and 'limit' in args.keys():
        result = businessdb.find({'loc': {'$geoWithin': { '$center': [ [ lon,lat] , .004 ] }}},{"_id":0,"name":1}).skip(args['start']).limit(args['limit'])
    elif 'start' in args.keys():
        result = businessdb.find({'loc': {'$geoWithin': { '$center': [ [ lon,lat] , .004 ] }}},{"_id":0,"name":1}).skip(args['start'])
    elif 'limit' in args.keys():
        result = businessdb.find({'loc': {'$geoWithin': { '$center': [ [ lon,lat] , .004 ] }}},{"_id":0,"name":1}).limit(args['limit'])
    else:
        result = businessdb.find({'loc': {'$geoWithin': { '$center': [ [ lon,lat] , .004 ] }}},{"_id":0,"name":1}).limit(50)
        
    for r in result:
        data.append(r)
        
    return {"Restaurants with in 5 miles":data}  
    
"""4================================================================================="""
@app.route("/reviews/<args>", methods=['GET'])
def reviews(args):
    
    args = myParseArgs(args) 
    data=[]
    id = args['id']
    if 'start' in args.keys():
        args['start'] = int(args['start'])
    if 'limit' in args.keys():
        args['limit'] = int(args['limit'])

    if 'start' in args.keys() and 'limit' in args.keys():
        result = review.find({'business_id' : id},{'_id':0}).skip(args['start']).limit(args['limit'])
    elif 'start' in args.keys():
        result = review.find({'business_id' : id},{'_id':0}).skip(args['start'])
    elif 'limit' in args.keys():
        result = review.find({'business_id' : id},{'_id':0}).limit(args['limit'])
    else:
        result = review.find({'business_id' : id},{'_id':0}).limit(50)

    for r in result:
        data.append(r)
    return {"All reviews for restaurant X":data}
       
"""5================================================================================="""
@app.route("/stars/<args>", methods=['GET'])
def stars(args):
    args = myParseArgs(args)
    id = args['id']
    num_stars=int(args['num_stars'])
    data=[]
    if 'start' in args.keys():
        args['start'] = int(args['start'])
    if 'limit' in args.keys():
        args['limit'] = int(args['limit'])

    if 'start' in args.keys() and 'limit' in args.keys():
        result = review.find({'business_id' : id, 'stars':num_stars},{"_id":0}).skip(args['start']).limit(args['limit'])
    elif 'start' in args.keys():
        result = review.find({'business_id' : id, 'stars':num_stars},{"_id":0}).skip(args['start'])
    elif 'limit' in args.keys():
        result = review.find({'business_id' : id, 'stars':num_stars},{"_id":0}).limit(args['limit'])
    else:
        result = review.find({'business_id' : id, 'stars':num_stars},{"_id":0}).limit(50)
    for r in result:
        data.append(r)
    return {"All the reviews for restaurant X that are 5 stars":data}

"""6================================================================================="""
@app.route("/yelping/<args>", methods=['GET'])
def yelping(args):
    args = myParseArgs(args)
    min_years = int(args['min_years'])
    this_year=2016
    req_year= this_year - min_years
    this_month=12
    k=str(req_year) + "-" + str(this_month)
    data=[]
    if 'start' in args.keys():
        args['start'] = int(args['start'])
    if 'limit' in args.keys():
        args['limit'] = int(args['limit'])

    if 'start' in args.keys() and 'limit' in args.keys():
        result = userdb.find({'yelping_since' : { '$gt' : k}},{"_id":0}).skip(args['start']).limit(args['limit'])
    elif 'start' in args.keys():
        result = userdb.find({'yelping_since' : { '$gt' : k}},{"_id":0}).skip(args['start'])
    elif 'limit' in args.keys():
        result = userdb.find({'yelping_since' : { '$gt' : k}},{"_id":0}).limit(args['limit'])
    else:
        result = userdb.find({'yelping_since' : { '$gt' : k}},{"_id":0}).limit(50)
    for r in result:
        data.append(r)
    return {" All the users that are yelping since X years":data}
       
"""7================================================================================="""
@app.route("/most_likes/<args>", methods=['GET'])
def most_likes(args):
    data =[]
    args = myParseArgs(args)
    if 'start' in args.keys():
        args['start'] = int(args['start'])
    if 'limit' in args.keys():
        args['limit'] = int(args['limit'])

    if 'start' in args.keys() and 'limit' in args.keys():
        result = tip.find({},{ "_id" : 0, "business_id":1,"likes":1}).sort([('likes' , -1)]).skip(args['start']).limit(args['limit'])
    elif 'start' in args.keys():
        result = tip.find({},{ "_id" : 0,"business_id":1, "likes":1}).sort([('likes' , -1)]).skip(args['start'])
    elif 'limit' in args.keys():
        result = tip.find({},{ "_id" : 0,"business_id":1, "likes":1}).sort([('likes' , -1)]).limit(args['limit'])
    else:
        result = tip.find({},{ "_id" : 0,"business_id":1, "likes":1}).sort([('likes' , -1)]).limit(50)
    for r in result:
        data.append(r)
    return {"Business that has most likes":data}
   
"""8================================================================================="""
@app.route("/review_count/", methods=['GET'])
def review_count():
    data=[]
    result=userdb.aggregate([{'$group': {'_id':0, 'avgReviewCountForUsers': {'$avg':'$review_count'} } }])
    for r in result:
        data.append(r['avgReviewCountForUsers'])
    return {"average review count":data}
"""9================================================================================="""
@app.route("/elite/<args>", methods=['GET'])
def elite(args):
    args = myParseArgs(args)
    data=[]
    if 'start' in args.keys():
        args['start'] = int(args['start'])
    if 'limit' in args.keys():
        args['limit'] = int(args['limit'])

    if 'start' in args.keys() and 'limit' in args.keys():
        result = userdb.find({'elite':{'$ne':[]}},{"_id":0,"user_id":1,"name":1,"elite":1}).skip(args['start']).limit(args['limit'])
    elif 'start' in args.keys():
        result = userdb.find({'elite':{'$ne':[]}},{"_id":0,"user_id":1,"name":1,"elite":1}).skip(args['start'])
    elif 'limit' in args.keys():
        result = userdb.find({'elite':{'$ne':[]}},{"_id":0,"user_id":1,"name":1,"elite":1}).limit(args['limit'])
    else:
        result = userdb.find({'elite':{'$ne':[]}},{"_id":0,"user_id":1,"name":1,"elite":1}).limit(50)
    for r in result:
        data.append(r)
    return {"All elite users":data}
"""10================================================================================="""
@app.route("/longest_elite/<args>", methods=['GET'])
def longest_elite(args):
    args = myParseArgs(args)
    data=[]
    if 'start' in args.keys():
        args['start'] = int(args['start'])
    if 'limit' in args.keys():
        args['limit'] = int(args['limit'])

    if 'start' in args.keys() and 'limit' in args.keys():
        result = userdb.find({'elite':{'$ne':[]}},{"_id":0,"user_id":1,"name":1,"elite":1}).skip(args['start']).limit(args['limit'])
    elif 'start' in args.keys():
        result = userdb.find({'elite':{'$ne':[]}},{"_id":0,"user_id":1,"name":1,"elite":1}).skip(args['start'])
    elif 'limit' in args.keys():
        result = userdb.find({'elite':{'$ne':[]}},{"_id":0,"user_id":1,"name":1,"elite":1}).limit(args['limit'])
    else:
        result = userdb.find({'elite':{'$ne':[]}},{"_id":0,"user_id":1,"name":1,"elite":1}).limit(50)
    for r in result:
        data.append(r)
    return {"All elite users":data}
"""11================================================================================="""
@app.route("/avg_elite/", methods=['GET'])
def avg_elite():
    data=[]
    result= userdb.aggregate([{"$group":{"_id":"$name","average":{"$avg":{"$size":"$elite"}}}},{ "$limit" : 1 }])
    for r in result:
        data.append(r)
    return {"All elite users":data}
"""=================================================================================="""
@app.route("/user/<args>", methods=['GET'])
def user(args):

    args = myParseArgs(args)
    
    if 'skip' in args.keys():
        args['skip'] = int(args['skip'])
    if 'limit' in args.keys():
        args['limit'] = int(args['limit'])

    data = []
    
    #.skip(1).limit(1)
    
    if 'skip' in args.keys() and 'limit' in args.keys():
        result = userdb.find({},{'_id':0}).skip(args['skip']).limit(args['limit'])
    elif 'skip' in args.keys():
        result = userdb.find({},{'_id':0}).skip(args['skip'])
    elif 'limit' in args.keys():
        result = userdb.find({},{'_id':0}).limit(args['limit'])
    else:
        result = userdb.find({},{'_id':0}).limit(10)  

    for row in result:
        data.append(row)


    return {"data":data}
    


@app.route("/business/<args>", methods=['GET'])
def business(args):

    args = myParseArgs(args)
    
    data = []
    
    result = businessdb.find({},{'_id':0}).limit(100)
    
    for row in result:
        data.append(row)
    

    return {"data":data}
"""=================================================================================="""
def snap_time(time,snap_val):
    time = int(time)
    m = time % snap_val
    if m < (snap_val // 2):
        time -= m
    else:
        time += (snap_val - m)
        
    if (time + 40) % 100 == 0:
        time += 40
        
    return int(time)

"""=================================================================================="""
def myParseArgs(pairs=None):
    """Parses a url for key value pairs. Not very RESTful.
    Splits on ":"'s first, then "=" signs.
    
    Args:
        pairs: string of key value pairs
        
    Example:
    
        curl -X GET http://cs.mwsu.edu:5000/images/
        
    Returns:
        json object with all images
    """
    
    if not pairs:
        return {}
    
    argsList = pairs.split(":")
    argsDict = {}

    for arg in argsList:
        key,val = arg.split("=")
        argsDict[key]=str(val)
        
    return argsDict
    

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)
api.py
Open with Google Docs
Displaying api.py.
