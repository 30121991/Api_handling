from urllib import *
import urllib.request 
import urllib.parse 

def  get_filter():   
    url = "http://127.0.0.1:5000/filter/" 
    params = {'startdate': '2017-05-17', 'enddate': '2017-05-19'}
    query_string = urllib.parse.urlencode( params ) 
    url = url + "?" + query_string 
    return url 
 
def  get_groupby():   
    url = "http://127.0.0.1:5000/groupby/" 
    params = {'date':'date','channel':'channel','country':'country','os':'os'}
    query_string = urllib.parse.urlencode( params ) 
    url = url + "?" + query_string 
    return url
    
def  get_orderby():   
    url = "http://127.0.0.1:5000/orderby/" 
    params = {'orderby':'revenue','order':'ascending'}
    query_string = urllib.parse.urlencode( params ) 
    url = url + "?" + query_string 
    return url

def  get_cpi():   
    url = "http://127.0.0.1:5000/cpi/" 
    return url

def  get_frst():   
    url = "http://127.0.0.1:5000/frst_jne/" 
    return url

def  get_rev_frst_jne():   
    url = "http://127.0.0.1:5000/rev_frst_jne/" 
    return url


def  may_install():   
    url = "http://127.0.0.1:5000/may_install/" 
    return url

def  cpi_cal_canada():   
    url = "http://127.0.0.1:5000/cpi_cal_canada/" 
    return url    

url= may_install()

with urllib.request.urlopen( url ) as response: 
    response_text = response.read() 
    print( response_text ) 
    
    