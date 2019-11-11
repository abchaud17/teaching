import xlwings as xw

def hello_xlwings():
    wb = xw.Book.caller()
    wb.sheets[0].range("A1").value = "Hello xlwings!"

@xw.func
def double_sum(x, y):
    """Returns twice the sum of the two arguments"""
    return 2 * (x + y)

@xw.func
def hello(name):
    return "hello {0}".format(name)

def get_figure(ticker, api_key):
    import matplotlib.pyplot as plt
    import quandl

    # Fetch market data from Quandl
    quandl.ApiConfig.api_key = api_key
    df = quandl.get(ticker, start_date="2000-01-01")

    scale = 1.0

    # Plot using Matplotlib
    fig = plt.figure(dpi=90, figsize=(scale * 3.0, scale * 2.0))
    df.plot(ax=plt.gca())

    return fig, df

def grab_plot():
    # Create a reference to the calling Excel Workbook
    sht = xw.Book.caller().sheets[0]

    # Get the ticker and the API key from Excel
    ticker = sht.range('B2').value
    api_key = sht.range('B50').value

    sht1 = xw.Book.caller().sheets[1]

    # Get the figure and show it in Excel
    fig, df = get_figure(ticker, api_key)
    pic = sht1.pictures.add(fig, name='quandl_fig', update=True)

    # Print raw data
    xw.Book.caller().sheets[1].range("J1").value = df

if __name__ == '__main__':
    xw.serve()
