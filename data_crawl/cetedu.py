import requests
from bs4 import BeautifulSoup
api_ajax = "https://www.cet.edu.vn/wp-admin/admin-ajax.php"
headers = {
    "accept": "text/html, */*; q=0.01",
    "accept-language": "en-US,en;q=0.9,vi;q=0.8",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "sec-ch-ua": "\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"Google Chrome\";v=\"122\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-requested-with": "XMLHttpRequest"
}
body = ("action=get_related_post_for_pages_new"
        "&offset_lt=9"
        "&limit_lt=9"
        "&category=35&page={}"
        "&col_class=4"
        "&hide_desc=0&hide_image=0&limit_chars=100&nofollow=&image_size=large&orderby=date&order=DESC&exclude=")


def _crawl(category_id):
    for i in range(0, 100):
        r = requests.post(api_ajax, headers=headers,
                          data="action=get_related_post_for_pages_new"f"&offset_lt={i * 9}""&limit_lt=9"f"&category={category_id}&page={i}""&col_class=4""&hide_desc=0&hide_image=0&limit_chars=10000&nofollow=&image_size=large&orderby=date&order=DESC&exclude=")
        if r.text == '        ':
            break
        else:
            # print(r.text)
            html = BeautifulSoup(r.text, "html.parser")
            articles = html.find_all('article', class_="box-item")
            for article in articles:
                image = article.find('img')['src']
                title = article.find('img')['alt']
                article_url = article.find('a')['href']
                print(f"{title}\t{image}\t{article_url}")


if __name__ == '__main__':
    xao_id = 35
    print('xao_id')
    _crawl(xao_id)
    chien_id = 39
    print('chien_id')
    _crawl(chien_id)
    lau_id = 37
    print('lau_id')
    _crawl(lau_id)
    kho_id = 38
    print('kho_id')
    _crawl(kho_id)
    bun_id = 40
    print('bun_id')
    _crawl(bun_id)
    mut_id = 42
    print('mut_id')
    _crawl(mut_id)
    xoi_id = 43
    print('xoi_id')
    _crawl(xoi_id)
    anvat_id = 41
    print('anvat_id')
    _crawl(anvat_id)
    canh_id = 46
    print('canh_id')
    _crawl(canh_id)
    chao_id = 45
    print('chao_id')
    _crawl(chao_id)
    nuong_id = 44
    print('nuong_id')
    _crawl(nuong_id)
    hap_id = 60
    print('hap_id')
    _crawl(hap_id)
    goi_id = 59
    print('goid')
    _crawl(goi_id)
    sup_id = 398
    print('sup_id')
    _crawl(sup_id)
    che_id = 47
    print('che_id')
    _crawl(che_id)
