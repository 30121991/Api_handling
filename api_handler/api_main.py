from flask import Flask, render_template, jsonify, request,redirect

from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with

import pandas as pd

import json     

from db_handling.db_handller import db_action

db_action_obj=db_action()
 

app = Flask(__name__)
api = Api(app)


parser = reqparse.RequestParser()

parser.add_argument('date', type=str)
parser.add_argument('startdate', type=str)
parser.add_argument('enddate', type=str)
parser.add_argument('channel', type=str)
parser.add_argument('country', type=str)
parser.add_argument('os', type=str)
parser.add_argument('orderby', type=str)
parser.add_argument('order', type=str)
      
class filter_activities(Resource):

    def get(self):
        args = parser.parse_args()
        startdate = args.get('startdate')
        enddate = args.get('enddate')
        channel = args.get('channel')
        country = args.get('country')
        os = args.get('os')
        df=db_action_obj.reading_files()
        df=db_action_obj.filtering_dataset(df,startdate,enddate,channel,country,os)
        json_val = df.to_json() 
        return json_val

class group_by_activity(Resource):

    def get(self):
        argss = parser.parse_args()
        date = argss.get('date')
        channel = argss.get('channel')
        country = argss.get('country')
        os = argss.get('os')
        df=db_action_obj.reading_files()
        df=db_action_obj.group_by(df,date,channel,country,os)
        print(df.head(10))
        json_val = df.to_json() 
        return json_val
        
class order_by_activity(Resource):

    def get(self):
        argss = parser.parse_args()
        orderby = argss.get('orderby')
        print(orderby)
        order = argss.get('order')
        df=db_action_obj.reading_files()
        df=db_action_obj.order_by(df,orderby,order)
        print(df.head(10))
        json_val = df.to_json() 
        return json_val        

class cpi_activity(Resource):

    def get(self):
        df=db_action_obj.reading_files()
        df=db_action_obj.cpi_cal(df)
        json_val = df.to_json()
        return json_val
        

class first_june_activity(Resource):

    def get(self):
        df=db_action_obj.reading_files()
        df=db_action_obj.first_june(df)
        json_val = df.to_json()
        return json_val
        
class revenue_first_june(Resource):

    def get(self):
        df=db_action_obj.reading_files()
        df=db_action_obj.rev_first_june(df)
        json_val = df.to_json()
        return json_val

class may_month_install(Resource):

    def get(self):
        df=db_action_obj.reading_files()
        df=db_action_obj.may_mnth_instl(df)
        json_val = df.to_json()
        return json_val
                          
class cpi_channel_canada(Resource):

    def get(self):
        df=db_action_obj.reading_files()
        df=db_action_obj.cpi_cal_canda(df)
        json_val = df.to_json()
        return json_val
                          
                
                
api.add_resource(filter_activities, '/filter/')

api.add_resource(group_by_activity, '/groupby/')

api.add_resource(order_by_activity, '/orderby/')

api.add_resource(cpi_activity, '/cpi/')

api.add_resource(first_june_activity, '/frst_jne/')

api.add_resource(may_month_install, '/may_install/')

api.add_resource(revenue_first_june, '/rev_frst_jne/')

api.add_resource(cpi_channel_canada, '/cpi_cal_canada/')

if __name__ == '__main__':
    app.run(debug=True)        
        

