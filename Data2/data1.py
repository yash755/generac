import requests
import json
from bs4 import BeautifulSoup
import csv

file = open('code.txt', 'r')

for f in file:
    code = f
    code = code.replace('\n', '')

    try:

        print (code)

        url = "https://www.generac.com/GeneracCorporate/Webservices/DealerLocatorWebService.asmx/SearchDealerLocator"

        payload = "{'searchOptions':{'State':'','City':'','PostalCode':" + str(code) + ",'Category':'3',\"CountryCode\":\"\",\"Radius\":\"200\",\"IsUSASelected\":true,\"IsCANSelected\":false,\"IsINTSelected\":false}}"
        headers = {
            'sec-ch-ua': "\"Chromium\";v=\"88\", \"Google Chrome\";v=\"88\", \";Not A Brand\";v=\"99\"",
            'accept': "application/json, text/javascript, */*; q=0.01",
            'x-requested-with': "XMLHttpRequest",
            'sec-ch-ua-mobile': "?0",
            'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36",
            'content-type': "application/json; charset=UTF-8",
            'sec-fetch-site': "same-origin",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'cache-control': "no-cache",
            'postman-token': "dcc43ea0-8113-a025-ebd6-358a95a772ad"
        }

        response = requests.request("POST", url, data=payload, headers=headers)

        data = json.loads(response.text)
        data1 = json.loads(data['d'])

        dealers = data1['DealerObjectList']

        if len(dealers) >= 1:
            for dealer in dealers:

                DealerID = ''
                DealerName = ''
                DealerAddress1 = ''
                DealerAddress2 = ''
                DealerCity = ''
                DealerState = ''
                DealerZip = ''
                DealerCountry = ''
                DealerWebSite = ''
                DealerPhone = ''
                DealerService = ''

                try:
                    DealerID = dealer['DealerID']

                except:
                    print ("E")


                try:
                    DealerName = dealer['DealerName']
                except:
                    print ("E")

                try:
                    DealerAddress1 = dealer['DealerAddress1']
                except:
                    print ("E")
                try:
                    DealerAddress2 = dealer['DealerAddress2']
                except:
                    print ("E")

                try:
                    DealerCity = dealer['DealerCity']
                except:
                    print ("E")
                try:
                    DealerState = dealer['DealerState']
                except:
                    print ("E")
                try:
                    DealerZip = dealer['DealerZip']
                except:
                    print ("E")
                try:
                    DealerCountry = dealer['DealerCountry']
                except:
                    print ("E")
                try:

                    DealerWebSite = dealer['DealerWebSite']
                    html = BeautifulSoup(DealerWebSite, 'html.parser')

                    a_tag = html.find('a')
                    DealerWebSite = a_tag.text.strip()

                    print (DealerWebSite)

                except:
                    print ("E")
                try:
                    DealerPhone = dealer['DealerPhone']
                except:
                    print ("E")

                    # print (DealerWebSite)

                try:
                    services = dealer['DealerServices']
                    service_tag = ''
                    for service in services:
                        try:
                            service_tag = service_tag + service['ServiceName'] + ','
                        except:
                            print ("E")

                    DealerService = service_tag

                except:
                    print ("E")

                arr = []

                temp = []

                temp.append(code)
                temp.append('Industrial/Commercial Sales & Service')
                temp.append(DealerID)
                temp.append(DealerName)
                temp.append(DealerAddress1)
                temp.append(DealerAddress2)
                temp.append(DealerCity)

                temp.append(DealerState)
                temp.append(DealerZip)
                temp.append(DealerCountry)
                temp.append(DealerWebSite)

                temp.append(DealerPhone)
                temp.append(DealerService)

                arr.append(temp)

                print (temp)

                with open('cat2.csv', 'a+') as csvfile:
                    csvwriter = csv.writer(csvfile)
                    csvwriter.writerows(arr)

        else:
            print ("Not Found")

    except:
        print ("Error")

        f1 = open('errors.txt','a+')
        f1.write(code)
        f1.write('\n')
        f1.close()
