############################################################################
#
#   ShodanSearch.py
#   © 2021 ABDULKADİR GÜNGÖR All Rights Reserved
#   Contact email address: abdulkadir_gungor@outlook.com
#
#	Developper:	Abdulkadir GÜNGÖR (abdulkadir_gungor@outlook.com)
#	Date:	04/2021
#	All Rights Reserved (Tüm Hakları Saklıdır)
#
############################################################################
from SearchData import SearchData
from NetworkData import NetworkData
import shodan, socket, os

# Ekranı Temizlemek için
def screenClear():
    print("\r\n") # Konsol dışı kullanımda ekranı temizlemek için
    # clear screen
    # ********************
    # Windows
    if os.name=='nt':
        os.system('cls')
    # Linux or MAC
    elif os.name=='posix':
        os.system('clear')
    # ********************
    print("")

#
def showBanner():
    print()
    print('\t#####################################################')
    print('\t#/*************************************************\#')
    print('\t#**||~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~||**#')
    print('\t#**||                                           ||**#')
    print('\t#**||            Shodan Search V1.1             ||**#')
    print('\t#**||                04/2021                    ||**#')
    print('\t#**||                                           ||**#')
    print('\t#**||       Developer: Abdulkadir GÜNGÖR        ||**#')
    print('\t#**||       (abdulkadir_gungor@outlook.com)     ||**#')
    print('\t#**||                                           ||**#')
    print('\t#**||~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~||**#')
    print('\t#\*************************************************/#')
    print('\t#####################################################')
    print()
    print()

#
def showMenu():
    print('\t       MENU')
    print('\t--------------------------------')
    print('\t1) Scan Ip/Hostname')
    print('\t2) Scan Network')
    print()
    print()
    print('\t(Exit) <<e>>')

# Shodan Api Key
def check_api_key():
    try:
        with open("Shodan_Api_Key.txt","r") as rfile:
            key = rfile.read()
            api_key = key.strip()
            result = True
    except:
        api_key = ''
        result = False
    #
    return result, api_key
#


def search_ip_or_hostname(SHODAN_API_KEY):
    try:
        print()
        print('\t{:^40}'.format('#' * 40))
        print('\t{:^40}'.format('SHODAN IP/HOSTNAME SEARCH'))
        print('\t{:^40}'.format('#' * 40))
        print()
        print()
        print('\t(Input Example) <Input> : www.google.com')
        print('\t(Input Example) <Input> : 8.8.8.8')
        print()
        tmp_input = input('\t<Input> : ')
        print()
        print()
        target_ip = socket.gethostbyname(tmp_input.strip())
        api = shodan.Shodan(SHODAN_API_KEY)
        host = api.host(target_ip)
        data = SearchData()
        #
        for key in host:
            if key == 'ip_str':
                data.ip = host[key]
            elif key == 'ports':
                data.ports = host[key]
            elif key == 'os':
                data.os = host[key]
            elif key == 'last_update':
                data.last_update = host[key]
            elif key == 'vulns':
                data.vulns = host[key]
            elif key == 'country_name':
                data.country_name = host[key]
            elif key == 'city':
                data.city = host[key]
            elif key == 'org':
                data.organization = host[key]
            elif key == 'data':
                data.data = host[key]
        #
        print('\t{:^40}'.format('SUMMARY'))
        print('\t{}'.format('-' * 40))
        print("\tIp              :", data.ip)
        print("\tCity            :", data.city)
        print("\tCountry         :", data.country_name)
        print("\tOrganization    :", data.organization)
        print("\tLast Update     :", data.last_update)
        print("\tOs              :", data.os)
        print("\tPorts           :", data.ports)
        print("\tVulnerabilities :", data.vulns)
        print('\t{}'.format('-' * 40))
        print()
        print()
        print('\t{:^40}'.format('DETAIL(S)'))
        print('\t{}'.format('-' * 40))
        for item in data.data:
            print()
            print("\tPort                 :", item['port'])
            try:
                print("\tProtocol             :", item['transport'])
            except:
                print("\tProtocol             : - ")
            try:
                print("\tProgram              :", item['product'])
            except:
                print("\tProgram              :  - ")
            try:
                print("\tVulnerability(ies)   :", item['vulns'])
            except:
                print("\tVulnerability(ies)   :  - ")
            # print("\tAll Data  :", item)
        #
        print('\t{}'.format('-' * 40))
        print()
        print()
        input("\t(Back) <Enter> :")
        #
    except:
        print("\tAn error occurred!")
        print()
        print()
        input("\t(Back) <Enter> :")

#
def search_network(SHODAN_API_KEY):
    try:
        print()
        print('\t{:^40}'.format('#' * 40))
        print('\t{:^40}'.format('SHODAN NETWORK SEARCH'))
        print('\t{:^40}'.format('#' * 40))
        print()
        print()
        print('\t(Input Example) <Input> : 8.8.8.0/24 ')
        print()
        tmp_input = input('\t <Input> : ')
        print()
        print()
        api     = shodan.Shodan(SHODAN_API_KEY)
        search_tmp = f"net:{tmp_input.strip()}"
        network = api.search( search_tmp, minify=False)
        #
        print('\t{:^40}'.format('RESULT(S)'))
        print('\t{}'.format('-' * 40))
        print('\tNetwork      : {}'.format(tmp_input.strip()))
        print('\tTotal Result : {}'.format(network['total']))
        print()
        print()
        #
        results = []
        for tmp in network['matches']:
            data = NetworkData()
            #
            try:
                data.ip = tmp['ip_str']
            except:
                data.ip = '-'
            #
            try:
                data.port = tmp['port']
            except:
                data.port = '-'
            #
            try:
                data.os = tmp['os']
            except:
                data.os = '-'
            #
            try:
                data.vulns = tmp['vulns']
            except:
                data.vulns = '-'
            #
            try:
                data.organization = tmp['org']
            except:
                data.organization = '-'
            #
            try:
                data.data = tmp['data']
            except:
                data.data = '-'
            #
            results.append(data)
        #
        if len(results) > 0:
            txt_tmp = f"{len(results)} IP(s) are shown"
            print('\t{:^40}'.format(txt_tmp))
            print('\t{}'.format('-' * 40))
            for tmp in results:
                print('\t{}:{}'.format(tmp.ip, tmp.port))
            print()
            print()
            for tmp in results:
                print('\t{:^40}'.format('DETAILS'))
                print('\t{}'.format('-' * 40))
                print("\tIp              :", tmp.ip)
                print("\tOrganization    :", tmp.organization)
                print("\tOs              :", tmp.os)
                print("\tPort            :", tmp.port)
                print("\tVulnerabilities :", tmp.vulns)
                print('\t{}'.format('-' * 40))
                print()
        print()
        print()
        input("\t(Back) <Enter> :")
    except:
        print("\tAn error occurred!")
        print()
        print()
        input("\t(Back) <Enter> :")

#
if __name__ == '__main__':
    res, SHODAN_API_KEY = check_api_key()
    if res:
        while True:
            screenClear()
            showBanner()
            showMenu()
            tmp = input('\t(Selection) : ')
            if tmp.strip().lower() == 'e' :
                exit(0)
            elif tmp.strip().isdigit():
                slc = int(tmp.strip())
                if  slc == 1:
                    screenClear()
                    search_ip_or_hostname(SHODAN_API_KEY)
                elif slc == 2:
                    screenClear()
                    search_network(SHODAN_API_KEY)
    else:
        screenClear()
        showBanner()
        print('\t"Shodan_Api_Key.txt" not found.')
        print()
        print()
        input("\t(Exit) <Enter> :")
        exit(0)