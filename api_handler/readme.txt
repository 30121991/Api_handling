1.Run api_main.py - as the main server script 

In api_main.py  script below are the end point channels :

2. api.add_resource(filter_activities, '/filter/') for - "filter by time range (date_from+date_to is enough), channels, countries, operating systems"

   api.add_resource(group_by_activity, '/groupby/') for - "group by one or more columns: date, channel, country, operating system"

   api.add_resource(order_by_activity, '/orderby/') for - "sort by any column in ascending or descending order"

   api.add_resource(cpi_activity, '/cpi/') for - "see derived metric CPI (cost per install) which is calculated as cpi = spend / installs"

   api.add_resource(first_june_activity, '/frst_jne/') - "Show the number of impressions and clicks that occurred before the 1st of June 2017, broken down by channel and country, sorted by clicks in descending order"

   api.add_resource(may_month_install, '/may_install/') - "Show the number of installs that occurred in May of 2017 on iOS, broken down by date, sorted by date in ascending order."

   api.add_resource(revenue_first_june, '/rev_frst_jne/') - "Show revenue, earned on June 1, 2017 in US, broken down by operating system and sorted by revenue in descending order."

   api.add_resource(cpi_channel_canada, '/cpi_cal_canada/') -"Show CPI and spend for Canada (CA) broken down by channel ordered by CPI in descending order. Please think carefully which is an appropriate aggregate function for CPI."


3. In "Test" folder we have the get_requests_urilib.py file where all the rest calling functions are mentiond according . We can call each of the get calls to verify each of the end points .
   Run 'get_requests_urilib.py' to get the outputs that you wanted (Please change the function names accordingly if you want to check for different different endpoint) 

4. I always preffered working on dataframes of pandas instead of using row of rows handler of relational databases . I always convert the sql 'fetchall' results in dataframes and then do the operations .
So in pandas we can directly call a url based csv and read it into datframes .So I just skipped the portion to load the csv file in SQLite dtabase and then load it into dataframe instead of that I directly read it from csv file to dataframe .
