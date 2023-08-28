import scrapy
from scrapy.utils.response import open_in_browser
from urllib.parse import urlencode
import re

class DentalscraperSpider(scrapy.Spider):
    name = "dentalscraper"
    allowed_domains = ["www.dentalcity.com"]
    start_urls = [
        "https://www.dentalcity.com/category/2/shop-category"
        # "https://www.dentalcity.com/",
        # "https://www.dentalcity.com/category/1120/anesthetics"
        # "https://www.dentalcity.com/category/1155/injectable"
    ]

    def parse(self, response):
        links = response.css(".categoriesdesc, .col-md-3, .col-xs-6").css("a::attr(href)").extract()

        cookies = {
            '.ASPXANONYMOUS': 'xVIn-vsM2gEkAAAAODhiODFiNWMtOTBjNy00MGVmLWFjNmUtNTQ5MDcxMmJhYzgxQcvz9xRM8kZgymXjUxUNSyY3LR81',
            'hopperopened': '0',
            '_gcl_au': '1.1.895782735.1692946354',
            '_gid': 'GA1.2.1520967086.1692946360',
            'ln_or': 'eyI0NTg2MDE4IjoiZCJ9',
            '_fbp': 'fb.1.1692946361738.671841227',
            '_hjFirstSeen': '1',
            '_hjIncludedInSessionSample_1518909': '1',
            '_hjSession_1518909': 'eyJpZCI6IjYwYTMyODczLTJjOTktNDJiNC04YTU2LTYyM2ZjZDM0MWI4OSIsImNyZWF0ZWQiOjE2OTI5NDYzNjE5NzcsImluU2FtcGxlIjp0cnVlfQ==',
            '_hjAbsoluteSessionInProgress': '0',
            '_hjSessionUser_1518909': 'eyJpZCI6Ijg2YTllNzA3LWE2OGYtNTI3OS04MmE2LThiMThhZTFjYTVhNSIsImNyZWF0ZWQiOjE2OTI5NDYzNjE5MDEsImV4aXN0aW5nIjp0cnVlfQ==',
            'Ignify_Nav': 'PDCacheKey_1%3DPRODUCT-LISTING-SESSION-KEY%5EPDPrevNextReffer_1%3Dhttps%3A//www.dentalcity.com/category/692/dci-international%5ECurrentPDReferrer_1%3Dhttps%3A//www.dentalcity.com/category/692/dci-international%5E',
            'WebStore_SessionId': '2tf4udmikefw4isyftaj3dmj',
            'userdata': 'f8bdb4a4-37a9-40d1-ad98-c71e983fb6df',
            '_gat_UA-58893840-1': '1',
            'hoppersession': 'WebStore_SessionId=2tf4udmikefw4isyftaj3dmj',
            'signuppopup': 'EmailSignUp_shown=1&WebStore_SessionId=2tf4udmikefw4isyftaj3dmj',
            '_uetsid': 'fb7d5a10431311ee85fa1b244fe68bb4',
            '_uetvid': 'fb7dcf70431311ee95ba559414e9f307',
            '_ga': 'GA1.2.71703478.1692946360',
            '_ga_ZHCQ4Y1LQW': 'GS1.1.1692946359.1.1.1692946731.16.0.0',
        }

        headers = {
            'authority': 'www.dentalcity.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9,pt;q=0.8',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': '.ASPXANONYMOUS=xVIn-vsM2gEkAAAAODhiODFiNWMtOTBjNy00MGVmLWFjNmUtNTQ5MDcxMmJhYzgxQcvz9xRM8kZgymXjUxUNSyY3LR81; hopperopened=0; _gcl_au=1.1.895782735.1692946354; _gid=GA1.2.1520967086.1692946360; ln_or=eyI0NTg2MDE4IjoiZCJ9; _fbp=fb.1.1692946361738.671841227; _hjFirstSeen=1; _hjIncludedInSessionSample_1518909=1; _hjSession_1518909=eyJpZCI6IjYwYTMyODczLTJjOTktNDJiNC04YTU2LTYyM2ZjZDM0MWI4OSIsImNyZWF0ZWQiOjE2OTI5NDYzNjE5NzcsImluU2FtcGxlIjp0cnVlfQ==; _hjAbsoluteSessionInProgress=0; _hjSessionUser_1518909=eyJpZCI6Ijg2YTllNzA3LWE2OGYtNTI3OS04MmE2LThiMThhZTFjYTVhNSIsImNyZWF0ZWQiOjE2OTI5NDYzNjE5MDEsImV4aXN0aW5nIjp0cnVlfQ==; Ignify_Nav=PDCacheKey_1%3DPRODUCT-LISTING-SESSION-KEY%5EPDPrevNextReffer_1%3Dhttps%3A//www.dentalcity.com/category/692/dci-international%5ECurrentPDReferrer_1%3Dhttps%3A//www.dentalcity.com/category/692/dci-international%5E; WebStore_SessionId=2tf4udmikefw4isyftaj3dmj; userdata=f8bdb4a4-37a9-40d1-ad98-c71e983fb6df; _gat_UA-58893840-1=1; hoppersession=WebStore_SessionId=2tf4udmikefw4isyftaj3dmj; signuppopup=EmailSignUp_shown=1&WebStore_SessionId=2tf4udmikefw4isyftaj3dmj; _uetsid=fb7d5a10431311ee85fa1b244fe68bb4; _uetvid=fb7dcf70431311ee95ba559414e9f307; _ga=GA1.2.71703478.1692946360; _ga_ZHCQ4Y1LQW=GS1.1.1692946359.1.1.1692946731.16.0.0',
            'origin': 'https://www.dentalcity.com',
            'referer': 'https://www.dentalcity.com/category/', # concatenate ID/category-name
            'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        data = {
            'param1': '', # id of category
            'param2': 'html_subcategorylist',
            'param3': '150X177',
            'param6': '',
            'param7': '?custid=&amp;custclsid=2',
        }

        ajax_url = [
            "https://www.dentalcity.com/widgets-category/gethtml_subcategoryproductlist"
        ]

        for i in links:
            scrapy.Request(i)

            id = re.findall(r'\d+', i)[0]
            title = re.findall(r"\d/([^/]+)$", i)[0]

            headers['referer'] = "https://www.dentalcity.com/category/" + id + "/" + title
            data['param1'] = id
            new_data = urlencode(data)
            

            for url in ajax_url:
                print(f"opening {url}")
                yield scrapy.FormRequest(
                    url,
                    headers=headers,
                    cookies=cookies,
                    body=new_data,
                    method="POST",
                    callback=self.parse_category
                )

            break

    def parse_category(self, response):
        cookies = {
            '.ASPXANONYMOUS': 'xVIn-vsM2gEkAAAAODhiODFiNWMtOTBjNy00MGVmLWFjNmUtNTQ5MDcxMmJhYzgxQcvz9xRM8kZgymXjUxUNSyY3LR81',
            'hoppersession': 'WebStore_SessionId=bfelmjqorrdb45mq10ookxuq',
            'hopperopened': '0',
            'Ignify_Nav': 'PDCacheKey_1%3DNull%5EPDPrevNextReffer_1%3Dhttps%3A//www.dentalcity.com/category/1120/anesthetics%5ECurrentPDReferrer_1%3Dhttps%3A//www.dentalcity.com/category/1120/anesthetics%5E',
            'WebStore_SessionId': 'zoihxbtqnwxk4byym4hwsqgu',
            'userdata': '336c7933-bf99-428d-ad58-a5fdbbd6268f',
            'signuppopup': 'EmailSignUp_shown=1&WebStore_SessionId=zoihxbtqnwxk4byym4hwsqgu',
        }

        headers = {
            'authority': 'www.dentalcity.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9,pt;q=0.8',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': '.ASPXANONYMOUS=xVIn-vsM2gEkAAAAODhiODFiNWMtOTBjNy00MGVmLWFjNmUtNTQ5MDcxMmJhYzgxQcvz9xRM8kZgymXjUxUNSyY3LR81; hoppersession=WebStore_SessionId=bfelmjqorrdb45mq10ookxuq; hopperopened=0; Ignify_Nav=PDCacheKey_1%3DNull%5EPDPrevNextReffer_1%3Dhttps%3A//www.dentalcity.com/category/1120/anesthetics%5ECurrentPDReferrer_1%3Dhttps%3A//www.dentalcity.com/category/1120/anesthetics%5E; WebStore_SessionId=zoihxbtqnwxk4byym4hwsqgu; userdata=336c7933-bf99-428d-ad58-a5fdbbd6268f; signuppopup=EmailSignUp_shown=1&WebStore_SessionId=zoihxbtqnwxk4byym4hwsqgu',
            'origin': 'https://www.dentalcity.com',
            'referer': '',
            'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        params = {
            'newarrivaldays': '30',
        }

        formData = {
            'source': 'NarrowSrchData',
            'filter': '',
            'cid': '',
            'type': '',
            'search': '',
            'keywordoption': '',
            'fltrdesc': '',
            'hdnCategoryId': '',
            'catalogfiltersquerystring': '',
            'hdnSelectedVal': '',
            'hdnFromPrice': '',
            'hdnPageNumber': '1',
            'hdnToPrice': '',
            'hdnCurrentProductIds': '',
            'hdnFilter': '',
            'hdndiscountid': '',
            'hdnDisplayType': 'grid',
            'hdnSortType': 'SELLERRECOMMENDATION',
            'hdnSortTypeClicked': 'false',
            'hdnProdPerPage': '',
            'searchKeyWordwithinFilter': '',
            'txtSearch': '',
            'txtNarrowSearch': '',
            'hdnSeeMore': '',
            'min_slider_price': '',
            'max_slider_price': '',
        }

        data = response.css(".category-count a::attr(href)").extract()
        for i in data:
            print(f"opening {i}")
            id = re.findall(r'\d+', i)[0]
            url = f"https://www.dentalcity.com/widgets-category/gethtml_productlist/{id}/html_productlist/300X210?newarrivaldays=30"

            title = re.findall(r"\d/([^/]+)$", i)[0]

            formData['filter'] = id
            formData['hdnCategoryId'] = id
            formData['hdnFilter'] = id

            headers['referer'] = 'https://www.dentalcity.com/category/' + id + "/" + title 

            yield scrapy.FormRequest(url,
                                     headers=headers,
                                     cookies=cookies,
                                     formdata=formData,
                                     method="POST",
                                     callback=self.parse_products)

    def parse_products(self, response):
        open_in_browser(response)
        data = response.css(".prodimage a::attr(href)").extract()
        for i in data:
            yield scrapy.Request(i, callback=self.fetch_information)
            break
    def fetch_information(self, response):
        name = response.css(".desktopproductname::text").extract()[0]
        # sku = response.css("#skucode::text").extract()[0]
        # price = response.css(".yourpricecontainer span").css("::text").extract()[0]

        print(name)
