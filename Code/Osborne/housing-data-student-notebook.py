#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pip install geopandas


# # A notebook for the Data Ethics Coruse
# 
# Assembled by John Wallin with the help of Claude 3.5, GPT-4o

# ## Housing Discrimination and Algorithmic Bias: A Data Ethics Project
# 
# ## Background and Context
# 
# ### Historical Housing Discrimination
# Racial covenants were legal clauses in property deeds that prohibited sale or occupancy by non-white people. These discriminatory practices, along with redlining and other systematic forms of housing discrimination, shaped the demographic and economic patterns we see in our cities today. While racial covenants were made illegal by the Fair Housing Act of 1968, their effects continue to influence modern housing patterns, property values, and wealth distribution.
# 
# The Mapping Prejudice Project at the University of Minnesota has documented over 30,000 racial covenants in Hennepin County. These covenants, implemented between 1910 and 1955, created lasting patterns of segregation and economic disparity that persist in modern data.
# 
# ### Modern Mortgage Lending
# Today, most mortgage lending decisions involve algorithmic systems that assess credit risk and determine loan approval. While these systems don't explicitly consider race, they may perpetuate historical biases through:
# - Property valuations influenced by historical segregation
# - Neighborhood characteristics shaped by past discrimination
# - Economic factors that reflect generational wealth disparities
# 
# ## Project Overview
# 
# This project examines the relationship between historical housing discrimination and modern lending patterns, focusing on two distinct types of bias:
# 
# 1. **Data Bias**: How historical discrimination is embedded in modern data
#    - Property values in areas with/without historical covenants
#    - Neighborhood demographic and economic characteristics
#    - Patterns of generational wealth and investment
# 
# 2. **Algorithmic Bias**: How modern lending systems might perpetuate discrimination
#    - Mortgage approval rates and terms
#    - Risk assessment criteria
#    - The use of potentially biased proxy variables
# 
# ## Data Sources
# 
# ### Primary Dataset (Provided)
# You will receive a preprocessed dataset combining:
# - Covenant density by census tract
# - Property values
# - Modern mortgage lending data
# - Census demographic information
# 
# ### Original Data Sources (For Reference and Extension Work)
# 1. **Mapping Prejudice Project**
#    - URL: https://mappingprejudice.umn.edu/
#    - Contains: Historical covenant data for Hennepin County
#    - Format: GIS data showing covenant locations and details
# 
# 2. **Census TIGER/LINE Files**
#    - URL: https://www.census.gov/cgi-bin/geo/shapefiles/index.php?year=2024&layergroup=Census+Tracts
#    - Contains: Census tract boundaries
#    - Format: Geographic shapefiles
# 
# 3. **HMDA Data Browser**
#    - URL: https://ffiec.cfpb.gov/data-browser/data/2023?category=states&items=MN
#    - Contains: Modern mortgage lending data
#    - Format: CSV files with lending information
# 
# ## Project Components
# 
# ### 1. Initial Analysis (50%)
# Using the provided dataset:
# - Analyze relationships between covenant density and property values
# - Examine modern mortgage approval patterns
# - Identify potential proxy variables for historical discrimination
# - Compare lending patterns in historically covenanted vs. non-covenanted areas
# 
# ### 2. Bias Investigation (30%)
# Clearly distinguish between and analyze:
# - **Data Bias**: Document how historical discrimination appears in modern data
#   - Property value disparities
#   - Neighborhood characteristics
#   - Economic indicators
# - **Algorithmic Bias**: Examine how lending algorithms might perpetuate discrimination
#   - Approval rate patterns
#   - Loan term differences
#   - Risk assessment criteria
# 
# ### 3. Ramsey County Extension (20%)
# Extend the analysis to Ramsey County:
# 1. Gather data from the provided sources
# 2. Adapt the analysis methods from Hennepin County
# 3. Compare patterns between counties
# 4. Document challenges and limitations
# 
# ## Deliverables
# 
# ### GitHub Repository
# - Analysis code and documentation
# - Data processing scripts
# - Meeting summaries (AI-assisted)
# - Visualization code
# - README explaining repository organization
# 
# ### Final Report (5 pages)
# 1. Introduction and Historical Context
# 2. Methodology
# 3. Findings
#    - Data bias analysis
#    - Algorithmic bias analysis
#    - County comparison
# 4. Discussion
#    - Implications for modern lending
#    - Proposed mitigation strategies
# 5. Limitations and Future Work
# 
# ### Presentation (15 minutes)
# - Historical context
# - Methodology overview
# - Key findings
# - Visualizations
# - Recommendations
# 
# ## Technical Resources
# - You will receive access to:
#   - Preprocessed dataset for Hennepin County
#   - Python notebook showing data preparation steps
#   - Sample visualization code
# 
# ## Evaluation
# Grading will follow the provided rubrics, with special emphasis on:
# - Clear distinction between data and algorithmic bias
# - Quality of technical analysis
# - Depth of historical understanding
# - Effectiveness of communication
# - Success in Ramsey County extension
# 
# ## Tips for Success
# - Start with the provided dataset to understand basic patterns
# - Document all assumptions and methodological choices
# - Clearly separate findings related to data bias vs. algorithmic bias
# - Consider ethical implications throughout your analysis
# - Plan the Ramsey County extension early - data collection takes time
# 
# 
# # Housing Discrimination and Algorithmic Bias: A Data Ethics Project
# 
# [Previous sections remain the same through "Technical Resources"]
# 
# ## Project Steps
# 
# ### Step 1: Set Up Project Infrastructure
# 
# 1. **Create the GitHub Repository**
#    - One group member creates a repository named `DATA6550-Housing-Bias`
#    - Required directory structure:
#      ```
#      databias_report.docx
#      readme.md
#      Code/
#        Lastname1/
#        Lastname2/
#        Lastname3/
#        Lastname4/
#      Data/
#        hennepin_analysis.csv
#        [Additional datasets]
#      Collaboration/
#        WeekA.docx
#        WeekB.docx
#      Analysis/
#        [Graphics and intermediate results]
#      ```
#    - Share repository access with all group members
#    - Add the instructor as a collaborator
# 
# 2. **Set Up Shared Document**
#    - Create shared Word document in OneDrive named `databias_report.docx`
#    - Enable "Track Changes" under the Review tab
#    - Share with all team members and instructor
#    - Add link to document in D2L Dropbox
# 
# ### Step 2: Create Group Communication Plan
# 
# 1. Choose a communication platform (D2L forums, Teams, Zoom, etc.)
# 2. Invite all group members and instructor to the platform
# 3. Establish regular check-in schedule
# 4. Document communication protocols in repository README
# 
# ### Step 3: Initial Data Exploration
# 
# 1. Download and examine the provided Hennepin County dataset
# 2. Review documentation of data sources:
#    - Mapping Prejudice Project
#    - Census TIGER/LINE files
#    - HMDA Data Browser
# 3. Document initial observations in shared report
# 
# ### Step 4: Divide and Execute Tasks
# 
# 1. Assign specific analysis responsibilities:
#    - Historical context research
#    - Data bias analysis
#    - Algorithmic bias investigation
#    - Visualization development
# 2. Each member must contribute their own code to their personal directory
# 3. Regular code reviews and integration discussions
# 
# ### Step 5: Document Discussions
# 
# 1. After each group meeting, create AI-generated summary including:
#    - Key decisions and insights
#    - Task assignments and deadlines
#    - Challenges and solutions
# 2. Save summaries as WeekA.docx and WeekB.docx in Collaboration folder
# 
# ### Step 6: Conduct Primary Analysis
# 
# 1. Analyze Hennepin County data:
#    - Property value patterns
#    - Lending disparities
#    - Demographic correlations
# 2. Document methodology and findings
# 3. Create visualizations
# 4. Regular repository updates
# 
# ### Step 7: Ramsey County Extension
# 
# 1. Collect required datasets
# 2. Apply analysis methodology
# 3. Compare results with Hennepin County
# 4. Document challenges and limitations
# 
# ### Step 8: Complete Final Report
# 
# 1. Compile findings in shared Word document
# 2. Include sections on:
#    - Historical context
#    - Methodology
#    - Results
#    - Comparative analysis
#    - Recommendations
# 3. Ensure all members contribute with tracked changes
# 
# ### Step 9: Submit Deliverables
# 
# 1. **GitHub Repository**
#    - Complete code base
#    - Documentation
#    - Analysis results
#    - Meeting summaries
# 
# 2. **D2L Group Dropbox**
#    - Final report PDF
#    - Collaboration summaries
#    - Repository URL
#    - Presentation slides
# 
# 3. **Individual Dropbox**
#    - Personal contribution summary
#    - Lessons learned
#    - Reflection on findings
# 
# ### Step 10: Present Findings
# 
# 1. Prepare 15-minute presentation
# 2. Include:
#    - Historical context
#    - Methodology overview
#    - Key findings
#    - Visualizations
#    - Recommendations
# 3. Be prepared for Q&A
# 
# [Previous sections on Evaluation remain the same]
# 
# ## Important Notes
# 
# - Submit only one repository URL and report per group
# - Maintain regular commits to show consistent progress
# - Document all data sources and methodological decisions
# - Clearly distinguish between data bias and algorithmic bias findings
# - Start Ramsey County data collection early
# - Use course forums or office hours for technical support
# 
# 
# 

# In[ ]:





# ### In this block we filter the Minnesota tract data from the Census database
# 
# [https://www.census.gov/cgi-bin/geo/shapefiles/index.php?year=2024&layergroup=Census+Tracts](https://www.census.gov/cgi-bin/geo/shapefiles/index.php?year=2024&layergroup=Census+Tracts)
# 
# The county code is hard coded in this block, so you will need to change it for other counties.

# In[2]:


import geopandas as gpd
import pandas as pd
import numpy as np
from shapely.geometry import Point
import matplotlib.pyplot as plt
import seaborn as sns


# Read the full state file
mn_tracts = gpd.read_file('tl_2024_27_tract.zip')

# Filter for Hennepin County (FIPS code 053)
hennepin_tracts = mn_tracts[mn_tracts['COUNTYFP'] == '053']

# Save just Hennepin County if you want
hennepin_tracts.to_file('hennepin_tracts.shp')


# In[4]:





# ### Mortgage data from 2023
# 
# We now reading the mortgage data for Minnesota in 2023.
# 
# [https://ffiec.cfpb.gov/data-browser/data/2023?category=states&items=MN](https://ffiec.cfpb.gov/data-browser/data/2023?category=states&items=MN)
# 
# Data is available back to 2018.

# In[3]:


mortgage_data = pd.read_csv('state_MN.csv')
mheaders = mortgage_data.columns
mheaders


# In[4]:


# data set size
mortgage_data.shape


# ### We will filter the loans to only be mortgages.
# 
# [https://ffiec.cfpb.gov/documentation/publications/loan-level-datasets/lar-data-fields](https://ffiec.cfpb.gov/documentation/publications/loan-level-datasets/lar-data-fields)
# 
# This is loan_purpose == 1

# In[5]:


# filter by loan_purpose = 1 (home purchase)
mortgage_data = mortgage_data[mortgage_data['loan_purpose'] == 1]


# In[6]:


covenent = pd.read_csv('Hennepin_County_Racial_Covenants_Table.csv')
cheaders = covenent.columns
cheaders


# ### We need to make our data sets a bit more manageable before merging

# In[7]:


covenant_slim = covenent[['FID', 'Racial_Res', 'Date_Deed', 'X', 'Y']]


# In[8]:


mortgage_slim = mortgage_data[[
    'activity_year',
    'census_tract',
    'derived_race',
    'action_taken',
    'loan_amount',
    'property_value',
    'income',
    'interest_rate',
    'tract_minority_population_percent',
    'tract_to_msa_income_percentage',
    'denial_reason-1'
]]


# ### Merge the two data sets
# 
# Merging the two datasets is tricky because this is geographic data.  One data set uses Lat and Long.  The other is set up to use census data tracts.  To put this together, we need to convert Lat and Long into UTM coordinates and determine what is inside the tract boundary.

# In[9]:


# Convert covenant data to GeoDataFrame with correct initial CRS
geometry = [Point(xy) for xy in zip(covenant_slim['X'], covenant_slim['Y'])]
covenant_gdf = gpd.GeoDataFrame(covenant_slim, geometry=geometry)
covenant_gdf.set_crs(epsg=4326, inplace=True)  # WGS84 decimal degrees

print("Original covenant points:", len(covenant_gdf))

# Transform to match the tracts CRS (UTM Zone 15N)
covenant_gdf = covenant_gdf.to_crs(epsg=26915)

# Quick check of transformed coordinates
print("\nTransformed coordinate ranges:")
print("X range:", covenant_gdf.geometry.x.min(), "to", covenant_gdf.geometry.x.max())
print("Y range:", covenant_gdf.geometry.y.min(), "to", covenant_gdf.geometry.y.max())

# Verify these points fall within tract bounds
tract_bounds = hennepin_tracts.total_bounds
print("\nTract bounds:")
print("X range:", tract_bounds[0], "to", tract_bounds[2])
print("Y range:", tract_bounds[1], "to", tract_bounds[3])

# Perform spatial join with transformed coordinates
covenants_with_tracts = gpd.sjoin(covenant_gdf, hennepin_tracts, how='left', predicate='within')

# See how many points matched to tracts
print("\nPoints that matched to tracts:", len(covenants_with_tracts))
print("Points with null tract assignments:", covenants_with_tracts['TRACTCE'].isna().sum())

# Count covenants per tract
covenants_per_tract = covenants_with_tracts.dropna(subset=['TRACTCE']).groupby('TRACTCE').size().reset_index(name='covenant_count')

print("\nTract Summary:")
print("Number of tracts with covenants:", len(covenants_per_tract))
if len(covenants_per_tract) > 0:
    print("\nCovenant counts per tract:")
    print(covenants_per_tract['covenant_count'].describe())


# In[10]:


def format_census_tract(value):
    try:
        # First convert to string to handle any type
        tract_str = str(value)
        # Remove any decimal points and trailing zeros
        tract_str = tract_str.split('.')[0]
        return tract_str
    except Exception as e:
        print(f"Error processing value: {value}, Type: {type(value)}")
        raise e

# Create a clean copy and try the conversion
mortgage_clean = mortgage_slim.copy()
mortgage_clean['census_tract'] = mortgage_clean['census_tract'].astype(str)
mortgage_clean['census_tract'] = mortgage_clean['census_tract'].apply(format_census_tract)

# Let's see what we got
print("\nAfter cleaning:")
print(mortgage_clean['census_tract'].head())


# In[11]:


# Clean mortgage data - first ensure we have strings
mortgage_clean = mortgage_slim.copy()
mortgage_clean['census_tract'] = mortgage_clean['census_tract'].astype(str)
mortgage_clean['census_tract'] = mortgage_clean['census_tract'].str.replace('.0', '')

# Clean mortgage data - first ensure we have strings
mortgage_clean = mortgage_slim.copy()
mortgage_clean['census_tract'] = mortgage_clean['census_tract'].astype(str)
mortgage_clean['census_tract'] = mortgage_clean['census_tract'].str.replace('.0', '')



# First format the covenant census tract IDs
covenants_with_tracts['census_tract'] = (
    covenants_with_tracts['STATEFP'] + 
    covenants_with_tracts['COUNTYFP'] + 
    covenants_with_tracts['TRACTCE']
)

# Create the per-tract counts
covenants_per_tract = covenants_with_tracts.groupby('census_tract').size().reset_index(name='covenant_count')

# Clean the mortgage data
mortgage_clean = mortgage_slim.copy()
mortgage_clean['census_tract'] = mortgage_clean['census_tract'].astype(str).str.replace('.0', '')

# Verify the formats match
print("Mortgage data examples:")
print(mortgage_clean['census_tract'].head())
print("\nCovenant data examples:")
print(covenants_per_tract['census_tract'].head())






# Merge the datasets
combined_data = mortgage_clean.merge(
    covenants_per_tract,
    on='census_tract',
    how='left'
)

# Fill NaN covenant counts with 0
combined_data['covenant_count'] = combined_data['covenant_count'].fillna(0)

# Basic Analysis
print("\nMerge Results:")
print("Total mortgage applications:", len(combined_data))
print("Applications in tracts with covenants:", (combined_data['covenant_count'] > 0).sum())
print("Unique tracts with covenants:", combined_data[combined_data['covenant_count'] > 0]['census_tract'].nunique())

# Calculate approval rates
combined_data['was_approved'] = combined_data['action_taken'].isin([1, 2])
covenant_areas = combined_data['covenant_count'] > 0

print("\nApproval Rates:")
print("Tracts with no covenants:", 
      combined_data[~covenant_areas]['was_approved'].mean())
print("Tracts with covenants:", 
      combined_data[covenant_areas]['was_approved'].mean())


# In[12]:


combined_data.columns

