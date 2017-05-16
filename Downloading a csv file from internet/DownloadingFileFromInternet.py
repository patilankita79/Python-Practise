# A program to download csv file from internet

from urllib import request

#Downloading csv file from internet
file_url = "http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=8&e=2&f=2014&g=d&a=2&b=27&c=2014&ignore=.csv"

def download_file(url):
    # Connecting to internet
    #Connction to webpage
    response = request.urlopen(url)

    #reading the data which is stored in variable file_read
    csv = response.read()

    #whatever data is read in varaible file_read, it is converted to string
    csv_string = str(csv)

    lines = csv_string.split("\\n")

    destination_url = r'stock_data.csv'

    file_read = open(destination_url, 'w')

    for line in lines:
        #Take file and write to it
        file_read.write(line +  "\n")
    file_read.close()

download_file(file_url)