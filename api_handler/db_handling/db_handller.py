import pandas as pd

class db_action:
    def __init__(self):
        self.file_link="https://gist.githubusercontent.com/kotik/3baa5f53997cce85cc0336cb1256ba8b/raw/3c2a590b9fb3e9c415a99e56df3ddad5812b292f/dataset.csv"
        
        
    def reading_files(self):
        df = pd.read_csv(self.file_link)
        df['date']= pd.to_datetime(df['date'])
        return df 

    def filtering_dataset(self,df,startdate,enddate,channel,country,os):
        if startdate:
            df = df.loc[((df['date'] > startdate) & (df['date'] <= enddate))]
        print(df.head(5))    
        if channel:
            df.loc[df['channel'] == channel]
        if country:
            df.loc[df['country'] == country]
        if os:
            df.loc[df['os'] == os]    
            
        df['date']=df['date'].dt.strftime('%Y-%m-%d')
        return df 
        
    def group_by(self,df,date,channel,country,os):
        key_list=[]
        if date:
           key_list.append(date)
        if channel:
            key_list.append(channel)
        if country:
            key_list.append(country)
        if os:
            key_list.append(os)
            
        df = df.groupby(key_list,as_index=False).mean()
        
        df['date']=df['date'].dt.strftime('%Y-%m-%d')
        return df 

    def order_by(self,df,orderby,order):
        if order == "ascending":
            df.sort_values(by=[orderby], ascending=True,inplace=True)
        else:
            df.sort_values(by=[orderby], ascending=False,inplace=True)        
        df['date']=df['date'].dt.strftime('%Y-%m-%d')    
        return df
        
    def cpi_cal(self,df):
        cpi_lst=[]
        for i,row in df.iterrows():
            spend=float(row['spend'])
            installs=int(row['installs'])
            cpi=spend/installs
            cpi_lst.append(cpi)
        df["cpi"] = cpi_lst
        print("###")
        print(df.columns)   
        print("##")       
        df['date']=df['date'].dt.strftime('%Y-%m-%d')    
        return df        

    def first_june(self,df):
       df = df.loc[(df['date'] < '2017-06-01')] 
       grouped_multiple  = df.groupby(['channel', 'country']).agg({'impressions': 'sum', 'clicks': 'sum'})
       grouped_multiple.columns = ['impressions', 'clicks']
       grouped_multiple = grouped_multiple.reset_index()
       grouped_multiple.sort_values(by=['clicks'], ascending=False,inplace=True)
       print("###")
       print(grouped_multiple)
       return grouped_multiple
       
    def rev_first_june(self,df):
       df = df.loc[((df['date'] == '2017-06-01') & (df['country'] <= 'US'))] 
       grouped_multiple  = df.groupby(['os']).agg({'revenue': 'sum'})
       grouped_multiple.columns = ['revenue']
       grouped_multiple = grouped_multiple.reset_index()
       grouped_multiple.sort_values(by=['revenue'], ascending=False,inplace=True)
       print("####")
       print(grouped_multiple)
       return grouped_multiple
       
    def may_mnth_instl(self,df):
       df = df.loc[((df['date'] >= '2017-05-01') & (df['date'] <= '2017-05-31'))] 
       grouped_multiple  = df.groupby(['date','os']).agg({'installs': 'sum'})
       grouped_multiple.columns = ['installs']
       grouped_multiple = grouped_multiple.reset_index()
       grouped_multiple.sort_values(by=['date'], ascending=True,inplace=True)
       print("####")
       print(grouped_multiple)
       grouped_multiple['date']=grouped_multiple['date'].dt.strftime('%Y-%m-%d')
       return grouped_multiple       
       
       
    def cpi_cal_canda(self,df):
        cpi_lst=[]
        for i,row in df.iterrows():
            spend=float(row['spend'])
            installs=int(row['installs'])
            cpi=spend/installs
            cpi_lst.append(cpi)
        df["cpi"] = cpi_lst
        print("###")
        df.loc[df['country'] == 'CA']  
        grouped_multiple  = df.groupby(['channel']).agg({'cpi': 'mean'})
        grouped_multiple.columns = ['cpi']
        grouped_multiple = grouped_multiple.reset_index()
        grouped_multiple.sort_values(by=['cpi'], ascending=False,inplace=True)
        print("#####")
        print(grouped_multiple)
        return grouped_multiple  