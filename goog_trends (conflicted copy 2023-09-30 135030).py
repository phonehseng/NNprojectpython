from pytrends.request import TrendReq

mytrend = TrendReq()

print(type(mytrend))
# extract United States trending seach terms
tr_search_us_df = mytrend.trending_searches(pn="united_kingdom")
# find out type of result
print(type(tr_search_us_df))
# print the data frame
###print(tr_search_us_df)
output = tr_search_us_df.get(0)
print(output)

