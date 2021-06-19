### Numbers chapter 1 : the census ###
# 1 The Lord spoke to Moses in the wilderness of Sinai, in the tent of meeting, on the first day of the second month, in the second year after they had come out of the land of Egypt, saying, 
# 2 “Take a census of all the congregation of the people of Israel, 
			# by clans, 
					# by fathers' houses, according to the number of names, 
							# every male, head by head. 
# 3 From twenty years old and upward, 
		# all in Israel who are able to go to war, you and Aaron shall list them, company by company.

# Assuming:
# df is the dataset with all the population of israel 

# Query:

### STATA
by tribe: count if age >=20 & male ==1 & able_war ==1

#### R

df2 <- subset(df, age >=20 & male ==1 & able_war ==1)
df2 %>% group_by(tribes) %>% tally()


##Python : 
import pandas as pd
import numpy as np

df2 = df[(df.age >= 20) & (df.male ==True) & (df.able_war ==True)] # create subset
print(df2['tribes'].value_counts()) #could use sum() in the place of count()