import mysql.connector
import requests

if __name__ == "__main__":
    db_manager


class db_manager():
    __db = ""
    __cursor = ""

    def __init__(self, host, user, passwd, url):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.url = url
        self.__db = mysql.connector.connect(
            host=self.host, user=self.user, passwd=self.passwd)
        self.__cursor = self.__db.cursor()

    def __del__(self):
        self.__db.close()

    def get_all_data(self):
        response = requests.get(self.url)
        return response.json()

    def save_all_data(self, data):
        self.__cursor.execute("CREATE DATABASE IF NOT EXISTS coronavirus;")
        self.__cursor.execute("USE coronavirus;")
        self.__cursor.execute(
            "CREATE TABLE IF NOT EXISTS CORON (id INT AUTO_INCREMENT PRIMARY KEY, Country VARCHAR(255), CountryCode VARCHAR(255), Slug VARCHAR(255), NewConfirmed INT(10), TotalConfirmed INT(10),NewDeaths INT(10),TotalDeaths INT(10), NewRecovered INT(10),TotalRecovered INT(10), Date VARCHAR(255))")

        for item in data["Countries"]:
            Country = item["Country"]
            CountryCode = item["CountryCode"]
            Slug = item["Slug"]
            NewConfirmed = item["NewConfirmed"]
            TotalConfirmed = item["TotalConfirmed"]
            NewDeaths = item["NewDeaths"]
            TotalDeaths = item["TotalDeaths"]
            NewRecovered = item["NewRecovered"]
            TotalRecovered = item["TotalRecovered"]
            Date = item["Date"]
            self.__cursor = self.__db.cursor()
            sql = "INSERT INTO CORON (Country,CountryCode,Slug,NewConfirmed,TotalConfirmed,NewDeaths,TotalDeaths,NewRecovered,TotalRecovered,Date ) " \
                "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (Country, CountryCode, Slug, NewConfirmed, TotalConfirmed,
                   NewDeaths, TotalDeaths, NewRecovered, TotalRecovered, Date)
            self.__cursor.execute(sql, val)
            self.__db.commit()
            print(self.__cursor.rowcount, "Coron added")

    def show_add_data(self):
        self.__cursor.execute("USE coronavirus;")
        self.__cursor.execute(
            "SELECT * FROM CORON ORDER BY TotalConfirmed DESC")
        coron = self.__cursor.fetchall()
        conf_all = 0
        recov_all = 0
        for item in coron:
            print("[Країна]", item[2],
                  "\n[Кількість нових захворювать за добу]", item[3], "\n[Всього захворівших]",
                  item[4],
                  "\n[Кількість померлих за добу]", item[5], "\n[Всього померлих] ", item[6],
                  "\n[Вилікуваних за добу]", item[7], "\n[Всього вилікуваних]", item[8], "\n[Дата]", item[9])
            conf_all += item[4]
            recov_all += item[8]
            print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
        print("Загальна кількість хворих  ➤", conf_all,
              "\nЗагальна кількість вилікуваних ➤", recov_all)

    def show_country(self, countr, countrycode):
        self.__cursor.execute("USE coronavirus;")
        self.__cursor.execute(
            "SELECT * FROM CORON WHERE Country = '" + countr + "' OR CountryCode = '"+countrycode+"'")
        coron = self.__cursor.fetchall()
        return coron

    def update_stat(self):
        self.__cursor.execute("USE coronavirus;")
        sql = ("DELETE FROM CORON")
        self.__cursor.execute(sql)
        self.__db.commit()
