'''
Created on 26-Jun-2017

@author: BALASUBRAMANIAM
'''
import requests

url="http://www.webservicex.net/globalweather.asmx?WSDL"
head={'content-type': 'text/xml'}
body="""<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <GetCitiesByCountry xmlns="http://www.webserviceX.NET">
      <CountryName>India</CountryName>
    </GetCitiesByCountry>
  </soap:Body>
</soap:Envelope> """

result=requests.post(url,data=body,headers=head)
print(result.content)



