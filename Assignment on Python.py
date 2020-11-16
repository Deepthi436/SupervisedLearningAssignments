#!/usr/bin/env python
# coding: utf-8

# In[72]:


#Dictionary
#In the weekend , I purchased 250g of apple, 500g of sugar, 2.5 kg of rice, 2.5 litres of milk and finally 1 dozen of egg.
#1.Can you help me frame the above purchase in the form of dictionary with commodities as keys to it.
Commodities = {"apple":0.25,"sugar":0.5,"rice":2.5,"milk":2.5,"egg":1}
print(Commodities)

#2.I forgot to mention another item, 1kg of atta packet. Can you also add it ?
Commodities.update({"atta":1})
print(Commodities)

#3.Instead of 2kg of rice, I bought only 1kg of rice. Can you change the corresponding value ?
Commodities["rice"] = 1
print(Commodities)

#4.Can you list out all these items using a loop.-to get quantities
for commodities in Commodities:
    print(Commodities[commodities])

#4.Can you list out all these items using a loop.-to get items
for commodities in Commodities:
    print(commodities)

#However, the cost of 1 kg apple is Rs.220, 1 kg of sugar is Rs.43, 1 Kg of rice is Rs. 45, 1 litre of milk is Rs.30 and 1 dozen of egg is Rs. 60.
#Create another dictionary for pricing.

Prices = {"apple":220,"sugar":43,"rice":45,"milk":30, "egg":60}

Price_of_each_commodity =  {commodity : price * Prices[commodity] for commodity, price in Commodities.items() if commodity in Prices}

print(Price_of_each_commodity)

only_prices_of_each_commodity = Price_of_each_commodity.values()
Total_price = sum(only_prices_of_each_commodity)
print("THE TOTAL BILL IS",Total_price)


# In[53]:


#Assignment on List
AI_companies = ['Amazon','Facebook','HiSilicon','Google','Apple','Microsoft','SenseTime']

# Sort the list in ascending order
AI_companies.sort()
print(AI_companies)

#Add multiple companies at once 'Nvidia', 'OpenAI' , 'Qualcomm' and 'Reliance' to the list
AI_companies.extend(['Nvidia','OpenAI','Qualcomm','Reliance'])
print(AI_companies)

#Lower the list using List comprehension
AI_companies_lower = [company.lower() for company in AI_companies]
print(AI_companies_lower)

#Elimiate 'Reliance' from the list
Reliance_removed = AI_companies.remove('Reliance')
print(AI_companies)


#Extract 'Facebook', 'Google' and 'Microsoft' using a single command
Extracted = [AI_companies[2],AI_companies[3],AI_companies[5]]
print(Extracted)


# In[69]:


#Assignment on Tuple
#(a)Consider the above standard price problem statement and place the prices in the form of the tuple.
Prices=(220,43,45,30,60)

#(b)Find out the min and max price among them.
print(min(Prices))
print(max(Prices))

#(c)Also, convert the above "AI_companies" list to a tuple.
AI_companies = ('Amazon','Facebook','HiSilicon','Google','Apple','Microsoft','SenseTime')

#Combine two above tuples to a single tuple.
Combined = Prices + AI_companies
print(Combined)

#(e)Compare the length of two tuples.
if len(Prices)>len(AI_companies):
    print("length of Prices is greater than AI_companies")
else:
    print("length of Prices is less than AI_companies")




# In[83]:


#Assignment on Strings

Text = " I am very keen in building up my career in Data Science, but not sure from where to start. If I search the web it throws me thousands of articles, few are relevant others make me confused, again I come around to the same page. Supervised has provided me a good platform to remove all such qualms which were wrangling in my mind"
#Consider the above text as a string, figure out the average length of the string.
print(len(Text))

#Lower the text in the string.
print(Text.lower())

#Try to get the clean text removing the punctuation from the string.---need to do

#Extract word "Data Science" from the string.
import re
word_to_extract = 'Data Science'
re.findall(word_to_extract,Text)




# In[ ]:




