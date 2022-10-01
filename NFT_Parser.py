import requests
import json
import sqlite3
import time
import threading
import telebot
from threading import Thread
from algoliasearch .search_client import SearchClient
lock = threading .Lock()
db = sqlite3 .connect('nft.db', check_same_thread=False)
cursor = db .cursor()
cursor .execute('''CREATE TABLE IF NOT EXISTS users(
                                address TEXT NOT NULL,
                                twitter TEXT NOT NULL,
                                instagram TEXT NOT NULL,
                                balance INTEGER NOT NULL);''')
db .commit()
bot = telebot .TeleBot(
    "")
threads_c = 10
count = 0


def operation_with_wallet(OO0O000O0O00O0000, OO00OOOOO00OO00O0, O0O0OO000O00OOO0O, O0OO0OO00O00OOO00="", O00OO000OOO000OOO=""):
    if OO00OOOOO00OO00O0 == "foundation.app":
        OO00O00OOOOOOOO00 = find_wallet(OO0O000O0O00O0000)
        if OO00O00OOOOOOOO00 > 500:
            time .sleep(0.3)
            OOO0O00OOOO0OOOO0 = requests .get(
                f"https://foundation.app/_next/data/uIQ1qW7MC1YvY4ri9mQQp/{OO0O000O0O00O0000}.json").json()
            OO00OO0OOOO00OOO0 = ""
            OO00OOOO00000O0OO = ""
            if len(OOO0O00OOOO0OOOO0["pageProps"]["user"]["twitSocialVerifs"]) > 0:

                OO00OO0OOOO00OOO0 = OOO0O00OOOO0OOOO0["pageProps"]["user"]["twitSocialVerifs"][0]["username"]

            if len(OOO0O00OOOO0OOOO0["pageProps"]["user"]["instaSocialVerifs"]) > 0:

                OO00OOOO00000O0OO = OOO0O00OOOO0OOOO0["pageProps"]["user"]["instaSocialVerifs"][0]["username"]
            if OO00OO0OOOO00OOO0 != "" or OO00OOOO00000O0OO != "":
                cursor .execute("INSERT INTO users VALUES (?,?,?,?)", (OO0O000O0O00O0000,
                                OO00OO0OOOO00OOO0, OO00OOOO00000O0OO, OO00O00OOOOOOOO00))
                db .commit()
                bot .send_message(
                    O0O0OO000O00OOO0O, f"{OO0O000O0O00O0000}\nTwitter: {OO00OO0OOOO00OOO0}\nInstagram: {OO00OOOO00000O0OO}\n{OO00O00OOOOOOOO00}$ || {OO00OOOOO00OO00O0}")
    if OO00OOOOO00OO00O0 == "knownorigin.io":
        OOOOOO00OOO0O0O0O = SearchClient .create(
            '2K2S1EIZGJ', '6b346083c2c567a5674676d9b253710b')
        OO00O000OO0OOOOO0 = OOOOOO00OOO0O0O0O .init_index(
            'user-profile-index')
        OO0OO00OO00OO00OO = OO00O000OO0OOOOO0 .search(
            OO0O000O0O00O0000)
        OO00O00OOOOOOOO00 = find_wallet(OO0O000O0O00O0000)
        if OO00O00OOOOOOOO00 > 500:
            OO00OO0OOOO00OOO0 = ""
            OO00OOOO00000O0OO = ""
            try:
                if "twitter" in OO0OO00OO00OO00OO["hits"][0]:

                    OO00OO0OOOO00OOO0 = OO0OO00OO00OO00OO["hits"][0]["twitter"]
            except:
                pass
            try:
                if "instagram" in OO0OO00OO00OO00OO["hits"][0]:

                    OO00OOOO00000O0OO = OO0OO00OO00OO00OO["hits"][0]["instagram"]
            except:
                pass
            if OO00OO0OOOO00OOO0 != "" or OO00OOOO00000O0OO != "":
                cursor .execute("INSERT INTO users VALUES (?,?,?,?)", (OO0O000O0O00O0000,
                                OO00OO0OOOO00OOO0, OO00OOOO00000O0OO, OO00O00OOOOOOOO00))
                db .commit()
                bot .send_message(
                    O0O0OO000O00OOO0O, f"{OO0O000O0O00O0000}\nTwitter: {OO00OO0OOOO00OOO0}\nInstagram: {OO00OOOO00000O0OO}\n{OO00O00OOOOOOOO00}$ || {OO00OOOOO00OO00O0}")
    if OO00OOOOO00OO00O0 == "async.art":
        if O0OO0OO00O00OOO00 == None:
            O0OO0OO00O00OOO00 = ""
        if O00OO000OOO000OOO == None:
            O00OO000OOO000OOO = ""
        if O0OO0OO00O00OOO00 != "" or O00OO000OOO000OOO != "":
            OO00O00OOOOOOOO00 = find_wallet(OO0O000O0O00O0000)
            if OO00O00OOOOOOOO00 > 500:
                cursor .execute("INSERT INTO users VALUES (?,?,?,?)", (OO0O000O0O00O0000,
                                O0OO0OO00O00OOO00, O00OO000OOO000OOO, OO00O00OOOOOOOO00))
                db .commit()
                bot .send_message(
                    O0O0OO000O00OOO0O, f"{OO0O000O0O00O0000}\nTwitter: {O0OO0OO00O00OOO00}\nInstagram: {O00OO000OOO000OOO}\n{OO00O00OOOOOOOO00}$ || {OO00OOOOO00OO00O0}")


def parse_wallets(O000O0OO0O0O00O0O, O0OO0000OO0OO0OO0):
    if O000O0OO0O0O00O0O == "foundation.app":
        O00OOO0O0O00OO0O0 = SearchClient .create(
            'JR5LTVZCSE', '1ae2d43a2816a05df9d1e053907048bc')
        O0OOOO00O0OOO0O00 = O00OOO0O0O00OO0O0 .init_index(
            'users_sort_total_vol_desc')
        O000OO000OO0OOO00 = O0OOOO00O0OOO0O00 .search("", {'page': 0, 'hitsPerPage': 1000, 'filters': 'numMinted > 2 AND numSold > 2 AND numBought > 2', 'attributesToRetrieve': [
                                                      'publicKey', 'socialVerification'], })
        for OOOOOOO0OOO000O0O in O000OO000OO0OOO00['hits']:
            while True:
                if threading .active_count() < 10:
                    time .sleep(0.2)
                    OO0O0O0OO00O00000 = Thread(target=operation_with_wallet, args=(
                        OOOOOOO0OOO000O0O['publicKey'], "foundation.app", O0OO0000OO0OO0OO0))
                    OO0O0O0OO00O00000 .start()
                    break
    elif O000O0OO0O0O00O0O == "knownorigin.io":
        O00OOOO000000OO0O = {"Origin": "https://knownorigin.io"}
        OOO0O000O00O0O000 = {'query': """query GetAddresses {
                        collectors(
                            first: 1000
                            orderBy: totalPurchaseEthSpent
                            orderDirection: desc
                        ) {
                            address
                            totalPurchaseEthSpent
                        }
                        artists(first: 1000, orderBy: supply, orderDirection: desc) {
                            address, supply
                        }
                    }"""}
        O000OO000OO0OOO00 = requests .post(
            "https://api.thegraph.com/subgraphs/name/knownorigin/known-origin", json=OOO0O000O00O0O000).json()["data"]
        OOOOOOO0OOO0O0OOO = []
        for OOOOOOO0OOO000O0O in O000OO000OO0OOO00["artists"]:
            OOOOOOO0OOO0O0OOO .append(OOOOOOO0OOO000O0O["address"])
        for OOOOOOO0OOO000O0O in O000OO000OO0OOO00["collectors"]:
            OOOOOOO0OOO0O0OOO .append(OOOOOOO0OOO000O0O["address"])
        for OOOOOOO0OOO000O0O in OOOOOOO0OOO0O0OOO:
            while True:
                if threading .active_count() < 10:
                    time .sleep(0.2)
                    OO0O0O0OO00O00000 = Thread(target=operation_with_wallet, args=(
                        OOOOOOO0OOO000O0O, "knownorigin.io", O0OO0000OO0OO0OO0))
                    OO0O0O0OO00O00000 .start()
                    break
    elif O000O0OO0O0O00O0O == "async.art":
        O000OO000OO0OOO00 = requests .get(
            "https://async-api.com/arts?artType=visual&count=1000&page=1&sortBy=creationDate&sortDirection=-1").json()["market"]
        for OOOOOOO0OOO000O0O in O000OO000OO0OOO00:
            if (OOOOOOO0OOO000O0O["owner"]["twitter"] != "" or OOOOOOO0OOO000O0O["owner"]["instagram"] != "") or (OOOOOOO0OOO000O0O["owner"]["twitter"] != None or OOOOOOO0OOO000O0O["owner"]["instagram"] != None):
                while True:
                    if threading .active_count() < 10:
                        time .sleep(0.2)
                        OO0O0O0OO00O00000 = Thread(target=operation_with_wallet, args=(
                            OOOOOOO0OOO000O0O["owner"]["address"], "async.art", O0OO0000OO0OO0OO0, OOOOOOO0OOO000O0O["owner"]["twitter"], OOOOOOO0OOO000O0O["owner"]["instagram"]))
                        OO0O0O0OO00O00000 .start()
                        break
    elif O000O0OO0O0O00O0O == "rarible.com":
        O00OOOO000000OO0O = {'content-type': 'application/json'}

        OOO0O000O00O0O000 = '{"size":1000,"filter":{"verifiedOnly":true,"sort":"LATEST","statuses":["AUCTION","FIXED_PRICE","OPEN_FOR_OFFERS"],"currency":"0x0000000000000000000000000000000000000000","hideItemsSupply":"HIDE_LAZY_SUPPLY","nsfw":false,"creatorAddresses":[]}}'
        O000OO000OO0OOO00 = requests .post("https://rarible.com/marketplace/search/v1/items",
                                           data=OOO0O000O00O0O000, headers=O00OOOO000000OO0O).json()
        print(O000OO000OO0OOO00[0])


def find_wallet(OO00000000OOOO00O):
    O00OO00000O00O000 = 0
    OOO0OOO000OOO00OO = requests .get(
        f"https://api.debank.com/user/addr?addr={OO00000000OOOO00O}").json()
    if OOO0OOO000OOO00OO["error_code"] == 1:
        return False

    for O000O00OOOO0O0OOO in OOO0OOO000OOO00OO["data"]["used_chains"]:
        try:
            time .sleep(0.1)
            OO00000000O00O0O0 = requests .get(
                f"https://api.debank.com/token/balance_list?user_addr={OO00000000OOOO00O}&is_all=false&chain={O000O00OOOO0O0OOO}").json()
            for OO0O0000OOO00OO00 in OO00000000O00O0O0["data"]:
                try:
                    O00OO00000O00O000 += round((OO0O0000OOO00OO00["balance"]*(
                        10 ** -18))*OO0O0000OOO00OO00["price"])
                except:
                    pass
        except:
            time .sleep(0.1)
            OO00000000O00O0O0 = requests .get(
                f"https://api.debank.com/token/balance_list?user_addr={OO00000000OOOO00O}&is_all=false&chain={O000O00OOOO0O0OOO}").text
            O00O0OO00OOO00O0O = open("1.html", "w")
            O00O0OO00OOO00O0O .write(OO00000000O00O0O0)
            O00O0OO00OOO00O0O .close
    return O00OO00000O00O000


@bot .message_handler(commands=['start', 'help'])
def send_welcome(OOO000OOOO0O00O00):
    bot .reply_to(OOO000OOOO0O00O00, "Hello")


@bot .message_handler(func=lambda OO00OOOO0OO000OOO: True)
def echo_all(O000OO000O0OOO000):
    if O000OO000O0OOO000 .text .lower() == "начать":
        OO0OOOO0OO0OOOO00 = time .time()
        parse_wallets("foundation.app",
                      O000OO000O0OOO000 .chat .id)
        parse_wallets("knownorigin.io",
                      O000OO000O0OOO000 .chat .id)
        parse_wallets("async.art", O000OO000O0OOO000 .chat .id)
        cursor .execute(
            "delete from users where rowid not in (select min(rowid) from users group by address)")
        db .commit()
        O00O0000O0O00OO0O = open("addresses.txt", "w")
        cursor .execute("SELECT * FROM users")
        OOO0O0000OOO0OOOO = cursor .fetchall()
        cursor .execute("SELECT COUNT() FROM users")
        OO00O0OO0000O0O00 = cursor .fetchone()
        for OO000OOOO00O0OO0O in OOO0O0000OOO0OOOO:
            O00O0000O0O00OO0O .write(
                f"{OO000OOOO00O0OO0O[0]} || {OO000OOOO00O0OO0O[1]} || {OO000OOOO00O0OO0O[2]} || {OO000OOOO00O0OO0O[3]}\n")
        O00O0000O0O00OO0O .close()
        bot .send_document(O000OO000O0OOO000 .chat .id,
                           document=open("addresses.txt", "rb"))
        print("--- %s seconds ---" %
              (time .time()-OO0OOOO0OO0OOOO00))
        bot .reply_to(
            O000OO000O0OOO000, f"Загрузка закончена: {time.time() - OO0OOOO0OO0OOOO00}")


bot .infinity_polling()
