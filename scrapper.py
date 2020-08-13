from bs4 import BeautifulSoup
import faster_than_requests as req
import csv
count = 0
list_url = {}
names = {}
values = {}
lines = ""


def input_url(index):
    url = input("Enter URL: ")
    list_url[index] = url
    matter = req.get2str(url)
    return matter


def take_value():
    global lines
    for i in range(1, count+1):
        lines = input_url(i)
        lines_list = list(lines.split("\n"))
        for rotate in range(len(lines_list)):
            if '''id="priceblock_dealprice"''' in lines_list[rotate]:
                line_value = lines_list[rotate]
            elif '''id="priceblock_ourprice"''' in lines_list[rotate]:
                line_value = lines_list[rotate]
            elif '''id="productTitle"''' in lines_list[rotate]:
                line_name = lines_list[rotate+9]
        soup = BeautifulSoup(line_value, 'html.parser')
        price = soup.get_text()
        price = price[2:]
        price = price.replace(",", "")
        price = float(price)
        line_name = line_name[24::]
        soup = BeautifulSoup(line_name, 'html.parser')
        names[i] = soup.get_text()
        values[i] = price


def make_list(index):
    return_list = [str(index), names[index], values[index], list_url[index]]
    return(return_list)


def save_details_csv():
    with open("Details.csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for i in range(1, count+1):
            get_list = make_list(i)
            writer.writerow(get_list)
    csvfile.close()


# Take Input
count = int(input("Enter Number of Entry: "))
take_value()
save_details_csv()
