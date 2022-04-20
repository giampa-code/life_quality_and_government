# Government and Life Quality.

## 1. Introduction

If there is something that has always worried me about my country Argentina (among many things) it was corruption and lack of justice. From day-to-day injustices to major corruption scandals in the news, the common denominator always seemed to be that nothing ever happens and things stay the same.

This is why I began to investigate, I searched databases from various sources and analyzed them to see if I could reach a conclusion and see how corrupt we are as a country (because we all do corruption) and how much that affects our lives.

## 2. Sources

### 2.1 World Bank Data.

The first reliable data base that I found were the World Development and  Worldwide Governance Indicators of [*The World Bank*](https://databank.worldbank.org/home).

From the Development DB I obtained the GDP per capita of 2019 of 265 countries.

From the Governance DB I calculated the mean over the years of each feature for each country (214 countries and 25 years aprox.) and combined the all variables into one **Government Quality** feature per country componened by:

- **Control of Corruption**: captures perceptions of the extent to which public power is exercised for private gain, including both petty and grand forms of corruption, as well as "capture" of the state by elites and private interests.
  
- **Government Effectiveness**: captures perceptions of the quality of public services, the quality of the civil service and the degree of its independence from political pressures, the quality of policy formulation and implementation, and the credibility of the government's commitment to such policies.

- **Political Stability and Absence of Violence/Terrorism**: measures perceptions of the likelihood of political instability and/or politically-motivated violence, including terrorism.

- **Rule of Law**: captures perceptions of the extent to which agents have confidence in and abide by the rules of society, and in particular the quality of contract enforcement, property rights, the police, and the courts, as well as the likelihood of crime and violence.

- **Regulatory Quality**: captures perceptions of the ability of the government to formulate and implement sound policies and regulations that permit and promote private sector development.

- **Voice and Accountability**: captures perceptions of the extent to which a country's citizens are able to participate in selecting their government, as well as freedom of expression, freedom of association, and a free media.

### 2.2 United Nations Development Programme

The 2019 Human Development Report was used from the UN.
This dataset has in total 189 countries and takes into account three main factors: health (life expectancy at birth), education (mean years of schooling) and GDP.

### 2.3 Numbeo

The 2022 Quality of Life Index by Country was used from Numbeo, slef-described as "the world’s largest cost of living database".
This dataset has information from 89 countries, with missing values mainly from Africa and Central America.
The Quality of Life index is an estimation of overall quality of life by using an empirical formula which takes into account: 
- purchasing power index 
- pollution index
- house price to income ratio
- cost of living index
- safety index
- health care index
- traffic commute time index
- climate index

## 3 Analysis and results

### 3.1 Rankings

Top 10 ranking plus Argentina plus the mean and median were made, listed from most interesting to least interesting, according to my opinion.

#### 3.1.1 Top 10 Government Quality

This graphic is clear, we not only have a low score, but we are also below the mean and the median.

![Top 10 Government Quality](https://github.com/giampa14/life_quality_and_government/blob/master/reports/figures/TOP10_GQ.png)

#### 3.1.2 Top 10 Property Price to Anual Income Ratio

AKA how many years a mean family should work to buy a mean apartment. The higher this value is, the worse.
What calls my attention the most is how Argentina shares the podium with Asian countries, which have a different reality in terms of space and population.

![Top 10 Property Price to Anual Income Ratio](https://github.com/giampa14/life_quality_and_government/blob/master/reports/figures/TOP10_PPAI.png)

#### 3.1.3 Top 10 Unsafe Countries

Being in the top of a not so nice index.

![Top 10 Life Quality Index](https://github.com/giampa14/life_quality_and_government/blob/master/reports/figures/TOP10_USC.png)

#### 3.1.4 Top 10 Life Quality Index

The same as the Government Quality ranking. Latter it will be showed that it is a linear relationship between the LQI and the GQI.

![Top 10 Life Quality Index](https://github.com/giampa14/life_quality_and_government/blob/master/reports/figures/TOP10_LQI.png)


#### 3.1.5 Top 10 Human Development Index

Despite out "bad quality of life", we have most of our basic needs covered, unlike many countries in Africa.

![Top 10 Human Development Index](https://github.com/giampa14/life_quality_and_government/blob/master/reports/figures/TOP10_HDI.png)

#### 3.1.6 Top 10 GDP

Not good, but above the median.

![Top 10 GDP](https://github.com/giampa14/life_quality_and_government/blob/master/reports/figures/TOP10_GDP.png)

### 3.2 Government and Life Quality

This is the most important outcome of the whole analysis, that is why it shares title with the document.

The results show that there is a high correlation between the quality of government of a country and the quality of life and wealth of its inhabitants.

![Government and Life Quality](https://github.com/giampa14/life_quality_and_government/blob/master/reports/figures/QLI_GQ.png)

### 3.3 Government Quality and Human Development

It is shown that the HDI grows logarithmically with respect to the Government Quality.
The same conclusions of the HDI ranking applies here. 

![Government and Life Quality](https://github.com/giampa14/life_quality_and_government/blob/master/reports/figures/HDI_GQ.png)

## 4 Conclusions and personal opinion

The results were surprisingly clear: 1) the quality of life (and GDP/capita) of the inhabitants of a country is totally related to the quality of its government and 2) that we are halfway down the table.

And it may be my opinion that the quality of life is a consequence and not a cause of the poor quality of government, but there is a reality that cannot be denied: having a good government is the responsibility of the citizens.

That is why I believe that we should not only work and fulfill our duties, but also exercise our citizen role: vote with conscience, participate in politics, demand that our politicians to fulfill their obligations and penalize (and then remember) acts of corruption.
