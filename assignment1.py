import pandas as pd
import numpy as np

if __name__=="__main__":
    #Load dataset using Pandas
    df=pd.read_csv("Sheet1.csv")
    print("----------------------------------------------------------------------")


    #Perform data exploration (head, info, describe)
    print(df.head())
    print("----------------------------------------------------------------------")

    print(df.info())
    print("----------------------------------------------------------------------")

    print(df.describe())
    print("----------------------------------------------------------------------")

   # Handle missing values
    print(df.isnull())
    print("----------------------------------------------------------------------")
    print(df.isna())
    print("----------------------------------------------------------------------")

    sales_data=np.loadtxt("Sheet1.csv",delimiter=',',usecols=1,skiprows=1)

    #Use NumPy to compute mean, median, std of Sales
    sales_mean=np.mean(sales_data)
    print(f"sales mean:{sales_mean}")
    print("----------------------------------------------------------------------")

    sales_median=np.median(sales_data)
    print(f"Sales median:{sales_median}")
    print("----------------------------------------------------------------------")

    sales_std=np.std(sales_data)
    print(f"Standard deviation:{sales_std}")
    print("----------------------------------------------------------------------")

    #Create Profit_Per_Unit column
    df["Profit_per_unit"]=df["Profit"]/df["Quantity"]
    print(df)
    print("----------------------------------------------------------------------")

    #Filter Sales > 250
    print(df["Sales"]>250)
    print("----------------------------------------------------------------------")

    #Group by Region (total Sales, avg Profit)
    print(df.groupby("Region").agg({"Sales":["sum"],"Profit":["mean"]}))
    print("----------------------------------------------------------------------")

    #Create pivot table (Region vs Category)
    pivot = pd.pivot_table(df, values='Sales', index='Region', columns='Category', aggfunc='sum')
    print(pivot)
    print("----------------------------------------------------------------------")
    
    #Sort by Profit descending
    df_sort=df.sort_values(by="Profit",ascending=False)
    print(df_sort)
    print("----------------------------------------------------------------------")


    #Classify Sales (High/Medium/Low)
    conditions = [(df['Sales'] >= 300),(df['Sales'] >= 150) & (df['Sales'] < 300),(df['Sales'] < 150)]
    choices = ['High', 'Medium', 'Low']
    df['Sales_Class'] = np.select(conditions, choices, default='Unknown')
    print(df)
    print("----------------------------------------------------------------------")

    #Find top-performing region
    df_top=df.groupby("Region").agg({"Profit":"sum"})
    df_top=df_top.sort_values(by="Profit",ascending=False)
    print(f"The top-performing region is {df_top.index[0]}:{df_top.iloc[0]['Profit']}")
    print("----------------------------------------------------------------------")

    #Business Insights
    #The North performs the best in terms of profit and East is the lowest in terms of Profit
    #There is no sales for clothing in East and West Region
    #West performs the best for Electronics sales and there is no sale for East
    #Regarding Furniture sales only East region performed compared to the rest
