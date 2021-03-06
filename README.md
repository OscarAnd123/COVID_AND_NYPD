## Has COVID-19 had any effect on the number of arrest by the NYPD?

![vis0](/nyc2.jpg)

## Overview
My focus for this project is to show if COVID-19 change the number of arrest by the NYPD. The way I'm approaching this project is to analyze the number of arrest during 2020 and comparing that to previous years. With the analyzes that I made, I will conclude if arrest increase or decrease from previous years. 

I analyzed NYPD's records of arrest throughout 2020, I looked at the number of arrest for each month, the number of arrest by race, and the number of arrest by Boroughs. 

During the George Floyd protest I have seen the NYPD arrest many protesters throughout the country and NYC. I was wondering if the number of Arrest had spiked up more than usual. My hypothesis is that the number of arrest will be like 2019 but the number of arrest will spike up during the summer. 

The dataset that I'll be using came from NYC Open data: https://data.cityofnewyork.us/Public-Safety/NYPD-Arrests-Data-Historic-/8h9b-rp9u/data in order to test my hypothesis and analyze the number of arrest made by the NYPD for previous years.



### Data
## Analyzes of 2020

![vis1](/graph2.jpg)

The number of arrest in 2020 is 140413. The first thing that I noticed was that there was big decrease of arrest during the months January, February, March, and April. The reason why there was a decrease could be because of COVID-19. COVID-19 was introduced in the beginning of the year and NYC was on lockdown. The second thing I noticed was the big spike in May this could be because the George Floyd protest were going on and many protesters were arrested during this month. Lastly, I was astonished that Arrests were increasing during the months of August, September, October, November, and December. I don't understand why Arrests increased during the fall and winter but usually arrest decrease during these months. In an article called [Seasonal Patterns in Criminal Victimization Trends](https://bjs.ojp.gov/content/pub/pdf/spcvt.pdf) they show how violent and household property crimes lower during the winter. But being arrested does not necessarily mean you were charged with a crime.

![vis2](/race_graph3.jpg)

During 2020 Black people are more likely to get arrested than any other race. The second demographic that is likely to get arrested are Hispanics. This is surprising because this disparity of arrests reminds me of the days of Stop and Frisk. Where the purpose of Stop and Frisk program was to target criminals but it targeted minorities the most and the effects are still lingering. Another reason why there is a disparity is because many communities that have many minorities are being over policed and there are laws that target minorities.

[John DeCarlo, chairman of the Department of Criminal Justice at the University of New Haven's Henry C. Lee College of Criminal Justice and Forensic Sciences, told ABC News that while he does not believe police target people for arrest based on race, he said officers often find themselves enforcing "overreaching laws" passed by legislatures that end up being biased against residents of economically disadvantaged communities.](https://abcnews.go.com/US/blacks-account-half-nyc-arrests-years-end-stop/story?id=71412485)

As of March 31, 2021, it is legal for adults 21 and older to possess up to three ounces of cannabis for personal use in New York. Adults may smoke or vape cannabis wherever smoking tobacco is allowed under the smoke-free air laws, with a few exceptions. [Before this law black people where 3 times more likely to get arrested than white people but the usage of marijuana where similar](https://www.aclu.org/news/criminal-law-reform/a-tale-of-two-countries-racially-targeted-arrests-in-the-era-of-marijuana-reform/).
If we just get rid of laws that target minorities we can change the disparity in arrest which can lead to communities trusting the policy more.


![vis3](/graph1.jpg)

Brooklyn, Manhattan, Bronx, and Queens had similar number of arrests. But the only borough that had a big difference was Staten Island. This could be because the population of Staten Island is lower that the five boroughs, so arrest are lower.


## Comparing The Number Of Arrest Of 2020 To Previous Years

![vis4](/graph4.jpg)

I was surprised that the number of arrest decreased a lot during 2020. In the beginning of this project, I thought that the number of arrest will be like 2019 but the number of arrest will spike up during the summer. There was a drastic decrease of arrest but there was also a spike during May. 

Comparing the numbers of arrest during 2020 and 2019 there is a decrease of 214617 arrest (a decrease of 60.45%). 
Comparing 2020 to 2018 there was a decrease of 106360 arrest (a decrease of 43.10%).

One interesting thing that I saw when looking at the graph was that each year had a similar increase and decrease periods. For example, in the month of May and October there is an increase of arrest and during March through April there is a decrease. 



![vis5](/graph5.jpg)

Although cases are lower during 2020 the trend of Black and Hispanics being the top two races from being arrested are still there. This shows that NYC is not doing enough to close the disparity gap of arrest. As I mentioned before many communities that have many minorities are being over policed and there are laws that target minorities.


![vis6](/graph6.jpg)

what we see in this graph is that the trend of number of arrest are similar every year. Although the number of arrest are different all the boroughs have a similar number of arrest except for Staten Island.


## Techniques

The tools I used for this project were pandas matplotlib and datetime. I used pandas in order to read the csv file and to extract data that I needed. While extracting data I also used datetime to get specific data for each month of 2020, 2019, and 2018. After extracting the data that I needed I used matplotlib in order to make bar graphs and line graphs to show the data clearly.


## Conclusion

What I learned is that COVID-19 did change the number of arrest during 2020 by a lot. When comparing that to 2019 there was a decrease of 60.45% and comparing that to 2018 there was a decrease of 43.10%. Now I'm curios to see if 2021 will have similar numbers of arrest like 2020 because COVID-19 is still prevalent or will the numbers of arrest increase because more people are getting vaccinated, and NYC is coming back to normal.


## Citation

Data Source:

https://data.cityofnewyork.us/Public-Safety/NYPD-Arrests-Data-Historic-/8h9b-rp9u/data

Information Source:

https://www.wsj.com/articles/SB10001424052702304066504576345553135009870
https://inequality.stanford.edu/sites/default/files/Crime_fact_sheet.pdf
https://bjs.ojp.gov/content/pub/pdf/spcvt.pdf
https://abcnews.go.com/US/blacks-account-half-nyc-arrests-years-end-stop/story?id=71412485
https://www.aclu.org/news/criminal-law-reform/a-tale-of-two-countries-racially-targeted-arrests-in-the-era-of-marijuana-reform/

Image Source:

https://www.nytimes.com/2019/06/05/realestate/new-york-citys-evolving-skyline.html

