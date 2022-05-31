from bs4 import BeautifulSoup
import requests
try:
    # <div class=" margin-b1__09f24__vaLrm border-color--default__09f24__NPAKY"><h1 class="css-dyjx0f">Shankar Ninan &amp; Co.</h1></div>
    
    source = requests.get('https://www.yelp.com/biz/berd-and-klauss-new-york-4')
    # source = requests.get('https://www.yelp.com/search?find_desc=immigration+lawyers&find_loc=New+York%2C+NY')
    source.raise_for_status()

    soup = BeautifulSoup(source.text, 'html.parser')
    # print(soup)
    # names = soup.find('p', class_= "css-1p9ibgf").find_all('a', class_="css-1um3nx", target="_blank", rel="noopener", role="link")
    websites = soup.find_all('a',class_="css-1um3nx", target="_blank", rel="noopener", role="link")#.a.text.strip('[<a class="css-1um3nx" href="/biz_redir?url=http%3A%2F%2Fwww.berdklauss.com&amp;cachebuster=1653817207&amp;website_link_type=website&amp;src_bizid=REpKhayZ9fvOmTxfUYgAtw&amp;s=b7a33df2eebdff6880bd4c68ac70e7eaccea51426d833563755fa6098e6119fc" rel="noopener nofollow" role="link" target="_blank"></a>]')#.find_all('a',class_="css-1um3nx", target="_blank", rel="noopener", role="link")
    print(websites)

   

except Exception as e:
  print(e)

#   # <p class=" css-1p9ibgf" data-font-weight="semibold"><a href="/biz_redir?url
