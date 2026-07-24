import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# functions

def closing(data,ticker):
    return data["Close", ticker]

def avgclosingprice(data,ticker):
    return data["Close", ticker].mean()

def highestclosingprice(data,ticker):
    return data["Close", ticker].max()

def lowestclosingprice(data,ticker):
    return data["Close", ticker].min()

    # calculate biggest single-day loss/gain & daily differences

def calculatedailydifferences(data,ticker):
    dailyDiff = data["Close",ticker].diff()
    dailyDiff.name = "Daily Returns" 
    dailyDiff = dailyDiff.fillna(0)
     
    return dailyDiff.min(), dailyDiff.max() # biggest single day loss, gain


    # calculate daily returns as a percentage
def calculatedailyreturns(data,ticker):
    return (data["Close",ticker] - data["Close",ticker].shift(1)) / data["Close",ticker].shift(1)

    # market volatility
def calculatevolatility(data,ticker):
    return ((data["Close",ticker] - data["Close",ticker].shift(1)) / data["Close",ticker].shift(1)).std()

    # rolling averages + total return over period
def onedayavgs(data,ticker):

    return data["Close",ticker].rolling(window=1).mean(), data["Close", ticker] / data["Close", ticker].shift(1) - 1    

def sevendayavgs(data,ticker):
    return data["Close",ticker].rolling(window=5).mean(), data["Close", ticker] / data["Close", ticker].shift(5) - 1

def onemonthavgs(data,ticker):
    return data["Close",ticker].rolling(window=21).mean(), data["Close", ticker] / data["Close", ticker].shift(21) - 1

def threemonthavgs(data,ticker):
    return data["Close",ticker].rolling(window=63).mean(), data["Close", ticker] / data["Close", ticker].shift(63) - 1

def sixmonthavgs(data,ticker):
    return data["Close",ticker].rolling(window=126).mean(), data["Close", ticker] / data["Close", ticker].shift(126) - 1

def yearlyavgs(data,ticker): 
    return data["Close",ticker].rolling(window=252).mean(), data["Close", ticker] / data["Close", ticker].shift(252) - 1

def graph(data,ticker):

    close = closing(data,ticker)

    sns.lineplot(x=data.index,y=close)

    plt.show()
    return

def displaycalculations(data,ticker):
    print("Average Closing Price: " + str(avgclosingprice(data,ticker)))
    print("Highest Closing Price: " + str(highestclosingprice(data,ticker)))
    print("Lowest Closing Price: " + str(lowestclosingprice(data,ticker)))
    print("Market Volatility: " + str(calculatevolatility(data,ticker)))

    x = True

    while x == True:
        print("Choose below to view rolling averages + return: ")
        print("Enter 0 for 1 day")
        print("Enter 1 for 7 day")
        print("Enter 2 for 1 month")
        print("Enter 3 for 3 month")
        print("Enter 4 for 6 month")
        print("Enter 5 for 1 year")
        print("Enter 6 to go return to menu")

        try:
            cond = int(input("Enter your input here: \n"))
        except ValueError:
            print("Please enter a valid input!")
            continue

        if cond == 0:
            oda, odr = onedayavgs(data,ticker)
            print("One day Average: " + str(oda.iloc[-1]))
            print("One day Return: " + str(odr.iloc[-1]) + "%")
        elif cond == 1:
            sda, sdr = sevendayavgs(data,ticker)
            print("Seven day Average: " + str(sda.iloc[-1]))
            print("Seven day Return: " + str(sdr.iloc[-1]) + "%")
        elif cond == 2:
            oma, omr = onemonthavgs(data,ticker)
            print("One month Average: " + str(oma.iloc[-1]))
            print("One month Return: " + str(omr.iloc[-1]) + "%")
        elif cond == 3:
            tma, tmr = threemonthavgs(data,ticker)
            print("Three month Average: " + str(tma.iloc[-1]))            
            print("Three month Return: " + str(tmr.iloc[-1]) + "%")        
        elif cond == 4:
            sma, smr = sixmonthavgs(data,ticker)
            print("Six month Average: " + str(sma.iloc[-1]))
            print("Six month Return: " + str(smr.iloc[-1]) + "%")
        elif cond == 5:
            ya, yr = yearlyavgs(data,ticker)
            print("Yearly Average: " + str(ya.iloc[-1]))
            print("Yearly Return: " + str(yr.iloc[-1]) + "%")
        elif cond == 6:
            x = False
        else: 
            print("Please enter a valid input! (0-5)")
            continue


# load tool

load = True
while load == True:
    print("\nYfinance stock visualization tool")
    print("----------------------------------")
    print("----------------------------------")
    print("Enter 'E' to exit")
    print("----------------------------------\n")

    start = str(input("Input a start date: \n"))

    if start == "E":
        load = False
        continue

    end = str(input("Input a end date: \n"))   

    if end == "E":
        load = False
        continue

    ticker = str(input("Input a ticker: \n"))

    if ticker == "E":
        load = False
        continue

    # load yfinance data to a df
    try:
        data = yf.download(ticker, start = start,end = end) 
    except Exception as error:
        print("Invalid format please try again")
        continue

    if data.empty:
        print("No data found for this ticker")
        continue
    
    x = True

    while x == True:
        print("\n----------------------------------")
        print("----------------------------------")
        print("nter 0 to display calculations")
        print("Enter 1 to display graph")
        print("Enter 2 to view another stock\n")


        try:
            cond = int(input("Enter your input here: \n"))
        except ValueError:
            print("Please enter a valid input!")
            continue

        if cond == 0:
            displaycalculations(data,ticker)
        elif cond == 1:
            graph(data,ticker)
        elif cond == 2: 
            x = False
        else: 
            print("Please enter a valid input! (0-2)")




    



    





