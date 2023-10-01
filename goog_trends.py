from pytrends.request import TrendReq

mytrend = TrendReq()
search_dict = {}
search_list = []

#print(type(mytrend))
# extract United States trending seach terms
tr_search_us_df = mytrend.trending_searches(pn="united_kingdom")
# find out type of result
###print(type(tr_search_us_df))
# print the data frame
###print(tr_search_us_df)
output = tr_search_us_df.get(0)
#print(tr_search_us_df.iloc[0, 0])
#print(len(tr_search_us_df.index))
for x in range(len(tr_search_us_df.index)):
    term = tr_search_us_df.iloc[x, 0]
    # search_dict.update({x : term})
    search_list.append(term)
print(search_list)
    