import json
from sys import argv

from requests_html import HTMLSession


def main(url):
    session = HTMLSession()
    #
    # response = session.get("https://kaspi.kz/shop/p/lego-mir-jurskogo-perioda-ps4-rus-10700136/")
    response = session.get(url)

    response.html.render()

    # content = response.html.html

    # print(content)

    session.close()

    first_place_seller_xpath = '/html/body/div[1]/div[3]/div/div[3]/div/div/div[1]/div/div/div/table/tbody/tr[1]/td[1]/a'
    first_place_seller_price_xpath = '/html/body/div[1]/div[3]/div/div[3]/div/div/div[1]/div/div/div/table/tbody/tr[1]/td[4]/div'

    second_place_seller_xpath = '/html/body/div[1]/div[3]/div/div[3]/div/div/div[1]/div/div/div/table/tbody/tr[2]/td[1]/a'
    second_place_seller_price_xpath = '/html/body/div[1]/div[3]/div/div[3]/div/div/div[1]/div/div/div/table/tbody/tr[2]/td[4]/div'

    third_place_seller_xpath = '/html/body/div[1]/div[3]/div/div[3]/div/div/div[1]/div/div/div/table/tbody/tr[3]/td[1]/a'
    third_place_seller_price_xpath = '/html/body/div[1]/div[3]/div/div[3]/div/div/div[1]/div/div/div/table/tbody/tr[3]/td[4]/div'

    first_place_seller = response.html.xpath(first_place_seller_xpath, first=True)
    first_place_seller_price = response.html.xpath(first_place_seller_price_xpath, first=True)

    second_place_seller = response.html.xpath(second_place_seller_xpath, first=True)
    second_place_seller_price = response.html.xpath(second_place_seller_price_xpath, first=True)

    third_place_seller = response.html.xpath(third_place_seller_xpath, first=True)
    third_place_seller_price = response.html.xpath(third_place_seller_price_xpath, first=True)

    data = []

    if first_place_seller_price:
        first_place_seller_price = int(first_place_seller_price.text[:-2].replace("\xa0", ""))
        data.append({
            "name": first_place_seller.text,
            "price": first_place_seller_price
        })
    else:
        data.append({
            "name": "",
            "price": 0
        })

    if second_place_seller_price:
        second_place_seller_price = int(second_place_seller_price.text[:-2].replace("\xa0", ""))
        data.append({
            "name": second_place_seller.text,
            "price": second_place_seller_price
        })
    else:
        data.append({
            "name": "",
            "price": 0
        })

    if third_place_seller_price:
        third_place_seller_price = int(third_place_seller_price.text[:-2].replace("\xa0", ""))
        data.append({
            "name": third_place_seller.text,
            "price": third_place_seller_price
        })
    else:
        data.append({
            "name": "",
            "price": 0
        })

    json_data = json.dumps(data, indent=4)

    print(json_data)

    # if first_place_seller:
    #     print("{ \"name\": \"" + first_place_seller.text + "\", \"price\": \"" + first_place_seller_price.text[:-1] + "\"}")
    # else:
    #     print("No elements found")


if __name__ == '__main__':
    script, first = argv
    main(first)
