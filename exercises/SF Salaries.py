# Import Pandas as pd
import pandas as pd

# Read Salaries.csv as a dataframe called sal

sal = pd.read_csv('Salaries.csv')
sal

'''
Id	EmployeeName	JobTitle	BasePay	OvertimePay	OtherPay	Benefits	TotalPay	TotalPayBenefits	Year	Notes	Agency	Status
0	1	NATHANIEL FORD	GENERAL MANAGER-METROPOLITAN TRANSIT AUTHORITY	167411.18	0.00	400184.25	NaN	567595.43	567595.43	2011	NaN	San Francisco	NaN
1	2	GARY JIMENEZ	CAPTAIN III (POLICE DEPARTMENT)	155966.02	245131.88	137811.38	NaN	538909.28	538909.28	2011	NaN	San Francisco	NaN
2	3	ALBERT PARDINI	CAPTAIN III (POLICE DEPARTMENT)	212739.13	106088.18	16452.60	NaN	335279.91	335279.91	2011	NaN	San Francisco	NaN
3	4	CHRISTOPHER CHONG	WIRE ROPE CABLE MAINTENANCE MECHANIC	77916.00	56120.71	198306.90	NaN	332343.61	332343.61	2011	NaN	San Francisco	NaN
4	5	PATRICK GARDNER	DEPUTY CHIEF OF DEPARTMENT,(FIRE DEPARTMENT)	134401.60	9737.00	182234.59	NaN	326373.19	326373.19	2011	NaN	San Francisco	NaN
...	...	...	...	...	...	...	...	...	...	...	...	...	...
148649	148650	Roy I Tillery	Custodian	0.00	0.00	0.00	0.0	0.00	0.00	2014	NaN	San Francisco	NaN
148650	148651	Not provided	Not provided	NaN	NaN	NaN	NaN	0.00	0.00	2014	NaN	San Francisco	NaN
148651	148652	Not provided	Not provided	NaN	NaN	NaN	NaN	0.00	0.00	2014	NaN	San Francisco	NaN
148652	148653	Not provided	Not provided	NaN	NaN	NaN	NaN	0.00	0.00	2014	NaN	San Francisco	NaN
148653	148654	Joe Lopez	Counselor, Log Cabin Ranch	0.00	0.00	-618.13	0.0	-618.13	-618.13	2014	NaN	San Francisco	NaN
148654 rows × 13 columns
'''

# Check the head of the DataFrame

sal.head()

'''
Id	EmployeeName	JobTitle	BasePay	OvertimePay	OtherPay	Benefits	TotalPay	TotalPayBenefits	Year	Notes	Agency	Status
0	1	NATHANIEL FORD	GENERAL MANAGER-METROPOLITAN TRANSIT AUTHORITY	167411.18	0.00	400184.25	NaN	567595.43	567595.43	2011	NaN	San Francisco	NaN
1	2	GARY JIMENEZ	CAPTAIN III (POLICE DEPARTMENT)	155966.02	245131.88	137811.38	NaN	538909.28	538909.28	2011	NaN	San Francisco	NaN
2	3	ALBERT PARDINI	CAPTAIN III (POLICE DEPARTMENT)	212739.13	106088.18	16452.60	NaN	335279.91	335279.91	2011	NaN	San Francisco	NaN
3	4	CHRISTOPHER CHONG	WIRE ROPE CABLE MAINTENANCE MECHANIC	77916.00	56120.71	198306.90	NaN	332343.61	332343.61	2011	NaN	San Francisco	NaN
4	5	PATRICK GARDNER	DEPUTY CHIEF OF DEPARTMENT,(FIRE DEPARTMENT)	134401.60	9737.00	182234.59	NaN	326373.19	326373.19	2011	NaN	San Francisco	NaN
'''

# Use the .info() method to find out how many entries there are

sal.info()

'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 148654 entries, 0 to 148653
Data columns (total 13 columns):
 #   Column            Non-Null Count   Dtype  
---  ------            --------------   -----  
 0   Id                148654 non-null  int64  
 1   EmployeeName      148654 non-null  object 
 2   JobTitle          148654 non-null  object 
 3   BasePay           148045 non-null  float64
 4   OvertimePay       148650 non-null  float64
 5   OtherPay          148650 non-null  float64
 6   Benefits          112491 non-null  float64
 7   TotalPay          148654 non-null  float64
 8   TotalPayBenefits  148654 non-null  float64
 9   Year              148654 non-null  int64  
 10  Notes             0 non-null       float64
 11  Agency            148654 non-null  object 
 12  Status            0 non-null       float64
dtypes: float64(8), int64(2), object(3)
memory usage: 14.7+ MB

'''

# what is the average base pay?

BasePayMean = sal['BasePay'].mean()
BasePayMean

# What is the highest amount of OvertimePay in the dataset

OverTimePayMax = sal['OvertimePay'].max()
OverTimePayMax

# What is the job title of JOSEPH DRISCOLL ? 
# Note: Use all caps, otherwise you may get an answer that doesn't match up (there is also a lowercase Joseph Driscoll)

sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle']

# How much does JOSEPH DRISCOLL make (including benefits)?

sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits']

# What is the name of highest paid person (including benefits)?

sal[sal['TotalPayBenefits']==sal['TotalPayBenefits'].max()]['EmployeeName']

# What is the name of lowest paid person (including benefits)? Do you notice something strange about how much he or she is paid?

sal[sal['TotalPayBenefits']==sal['TotalPayBenefits'].min()]['EmployeeName']

# What was the average (mean) BasePay of all employees per year? (2011-2014) ?

sal.groupby('Year').agg(['mean'])['BasePay']

# How many unique job titles are there?

sal['JobTitle'].nunique()

# What are the top 5 most common jobs?

sal['JobTitle'].value_counts().head(5)

# How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?)

sum(sal[sal['Year'] == 2013]['JobTitle'].value_counts() == 1)

# How many people have the word Chief in their job title? (This is pretty tricky)

def chief(title):
    if 'chief' in title.lower():
        return True
    else:
        return False
        
sum(sal['JobTitle'].apply(lambda x:chief(x)))




