import psycopg2

class DBFacade:
    def __init__(self):
        self.DB_CONNECTION = psycopg2.connect(
            dbname='belarus',
            user='vladislav',
            host='localhost',
            password='postgres',
            port=5432
        )
        self.DB_CURSOR = self.DB_CONNECTION.cursor()
        self.__create_tables()

    def __create_tables(self):
        create_tables_query = """
                        CREATE TABLE IF NOT EXISTS city (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(200) UNIQUE,
                        region VARCHAR(200),
                        population INT,
                        area NUMERIC(8, 2)
                        ); 
        
                        CREATE TABLE IF NOT EXISTS attraction (
                         id SERIAL PRIMARY KEY,
                         city_id INT, 
                         name VARCHAR(200),
                         type VARCHAR(200),
                         FOREIGN KEY (city_id) REFERENCES city(id)
                         );  
                         
                        CREATE TABLE IF NOT EXISTS route (
                         id SERIAL PRIMARY KEY,
                         city_from_id INT,
                         city_to_id INT, 
                         transport_type VARCHAR(200),
                         schedule VARCHAR(200),
                         FOREIGN KEY (city_from_id) REFERENCES city(id),
                         FOREIGN KEY (city_to_id) REFERENCES city(id)
                         );                 
        """

        self.DB_CURSOR.execute(create_tables_query)
        self.DB_CONNECTION.commit()

    def add_city(self):
            self.DB_CURSOR.execute("SELECT COUNT(*) FROM city;")
            count = self.DB_CURSOR.fetchone()[0]

            if count == 115:
                print("All citys has a table")
                return
            elif count == 0:
                city_information = [
            ('Барановичи', 'Брестская', 171400, 50.22),
            ('Барань', 'Витебская', 10200, 12.22),
            ('Белоозерск', 'Брестская', 11000, 5.84),
            ('Белыничи', 'Могилевская', 9700, 139),
            ('Береза', 'Брестская', 28400, 30.40),
            ('Березино', 'Минская', 11400, 40.32),
            ('Березовка', 'Гродненская', 9500, 6.7),
            ('Бобруйск', 'Могилевская', 207400, 139.6),
            ('Борисов', 'Минская', 135700, 60.2),
            ('Браслав', 'Витебская', 9400, 12.9),
            ('Брест', 'Брестская', 344500, 170.90),
            ('Буда-Кошелево', 'Гомельская', 8600, 7.0),
            ('Быхов', 'Могилевская', 16400, 6.9),
            ('Василевичи', 'Гомельская', 3200, 2.5),
            ('Верхнедвинск', 'Витебская', 6900, 16.8),
            ('Ветка', 'Гомельская', 8600, 4.7),
            ('Вилейка', 'Минская', 26600, 15.40),
            ('Витебск', 'Витебская', 358400, 150.98),
            ('Волковыск', 'Гродненская', 41500, 22.30),
            ('Воложин', 'Минская', 10000, 40.4),
            ('Высокое', 'Брестская', 4900, 4.8),
            ('Ганцевичи', 'Брестская', 13400, 15.8),
            ('Глубокое', 'Витебская', 17700, 4.6),
            ('Гомель', 'Гомельская', 501100, 170.2),
            ('Горки', 'Могилевская', 29000, 8.5),
            ('Городок', 'Витебская', 11500, 12.7),
            ('Гродно', 'Гродненская', 361100, 142.11),
            ('Давид-Городок', 'Брестская', 5700, 11.18),
            ('Дзержинск', 'Минская', 29800, 20.89),
            ('Дисна', 'Витебская', 1400, 2.2),
            ('Добруш', 'Гомельская', 18100, 18.87),
            ('Докшицы', 'Витебская', 6700, 7.90),
            ('Дрогичин', 'Брестская', 14800, 15.56),
            ('Дубровно', 'Витебская', 6900, 4.89),
            ('Дятлово', 'Гродненская', 7800, 3.6),
            ('Ельск', 'Гомельская', 8700, 15.57),
            ('Жабинка', 'Брестская', 14400, 20.87),
            ('Житковичи', 'Гомельская', 16000, 33.59),
            ('Жлобин', 'Гомельская', 76800, 40.20),
            ('Жодино', 'Минская', 63700, 30.90),
            ('Заславль', 'Минская', 17400, 19.90),
            ('Иваново', 'Брестская', 16200, 10.00),
            ('Ивацевичи', 'Брестская', 22400, 16.00),
            ('Ивье', 'Гродненская', 7100, 39.76),
            ('Калинковичи', 'Гомельская', 526000, 29.8),
            ('Каменец', 'Брестская', 8300, 10.00),
            ('Кировск', 'Могилевская', 7900, 4.6),
            ('Клецк', 'Минская', 11200, 3.9),
            ('Климовичи', 'Могилевская', 15000, 14.9),
            ('Кличев', 'Могилевская', 7300, 18.2),
            ('Кобрин', 'Брестская', 52600, 29.9),
            ('Копыль', 'Минская', 10000, 12.5),
            ('Коссово', 'Брестская', 1900, 4.2),
            ('Костюковичи', 'Могилевская', 14900, 20.01),
            ('Кричев', 'Могилевская', 23300, 23.03),
            ('Круглое', 'Могилевская', 7200, 23.89),
            ('Крупки', 'Минская', 8400, 30.12),
            ('Лепель', 'Витебская', 17100, 15.54),
            ('Лида', 'Гродненская', 103900, 29.23),
            ('Логойск', 'Минская', 15600, 9.84),
            ('Лунинец', 'Брестская', 23600, 7.65),
            ('Любань', 'Минская', 11300, 5.6),
            ('Ляховичи', 'Брестская', 10600, 18.76),
            ('Малорита', 'Брестская', 12700, 4.5),
            ('Марьина Горка', 'Минская', 20100, 19.04),
            ('Микашевичи', 'Брестская', 12200, 12.23),
            ('Минск', 'Минская', 1992900, 348.8),
            ('Миоры', 'Витебская', 7800, 12.89),
            ('Могилев', 'Могилевская', 353100, 140.2),
            ('Мозырь', 'Гомельская', 105200, 34.32),
            ('Молодечно', 'Минская', 89100, 27.9),
            ('Мстиславль', 'Могилевская', 10000, 8.23),
            ('Мядель', 'Минская', 7000, 13.87),
            ('Наровля', 'Гомельская', 8400, 4.98),
            ('Несвиж', 'Минская', 16000, 3.87),
            ('Новогрудок', 'Гродненская', 27900, 22.65),
            ('Новолукомль', 'Витебская', 11800, 20.14),
            ('Новополоцк', 'Витебская', 95700, 28.56),
            ('Орша', 'Витебская', 102800, 28.30),
            ('Осиповичи', 'Могилевская', 29100, 15.15),
            ('Островец', 'Гродненская', 15100, 30.34),
            ('Ошмяны', 'Гродненская', 16800, 16.17),
            ('Петриков', 'Гомельская', 10400, 29.55),
            ('Пинск', 'Брестская', 124300, 30.46),
            ('Полоцк', 'Витебская', 79600, 30.12),
            ('Поставы', 'Витебская', 18600, 19.09),
            ('Пружаны', 'Брестская', 18824, 20.32),
            ('Речица', 'Гомельская', 65200, 19.43),
            ('Рогачев', 'Гомельская', 31800, 27.30),
            ('Светлогорск', 'Гомельская', 62600, 33.23),
            ('Свислочь', 'Гродненская', 6000, 3.9),
            ('Сенно', 'Витебская', 7100, 11.83),
            ('Скидель', 'Гродненская', 9700, 11.76),
            ('Славгород', 'Могилевская', 7800, 20.49),
            ('Слоним', 'Гродненская', 48900, 23.20),
            ('Слуцк', 'Минская', 60100, 13.19),
            ('Смолевичи', 'Минская', 22700, 23.40),
            ('Сморгонь', 'Гродненская', 35400, 22.90),
            ('Солигорск', 'Минская', 97800, 40.13),
            ('Старые Дороги', 'Минская', 10900, 20.17),
            ('Столбцы', 'Минская', 17700, 19.90),
            ('Столин', 'Брестская', 13800, 139),
            ('Толочин', 'Витебская', 9700, 9.7),
            ('Туров', 'Гомельская', 2800, 4.3),
            ('Узда', 'Минская', 10600, 14.9),
            ('Фаниполь', 'Минская', 18300, 12.7),
            ('Хойники', 'Гомельская', 13200, 11.77),
            ('Чаусы', 'Могилевская', 9800, 9.84),
            ('Чашники', 'Витебская', 7700, 5.81),
            ('Червень', 'Минская', 10500, 14.11),
            ('Чериков', 'Могилевская', 7800, 15.17),
            ('Чечерск', 'Гомельская', 8900, 14.12),
            ('Шклов', 'Могилевская', 14900, 22.34),
            ('Щучин', 'Гродненская', 15400, 20.00),
            ('Мосты', 'Гродненская', 14400, 14.84)

        ]

                add_city_information = """
                INSERT INTO city (name, region, population, area)
        VALUES (%s, %s, %s, %s);
        """

                self.DB_CURSOR.executemany(add_city_information, city_information)
                self.DB_CONNECTION.commit()
                print("Cityes add in table")
            else:
                print(f"В таблице уже есть все города")


    def show_all_city(self):
        city_query = """
        SELECT id, name, region, population, area FROM city;
        """

        self.DB_CURSOR.execute(city_query)
        result = self.DB_CURSOR.fetchall()
        print("Вся информация о городах: ")

        for cit in result:
            print(f"Город --- {cit[1]}; id города: {cit[0]}; Область: {cit[2]}; население: {cit[3]} тыс. человек; площадь: {cit[4]} км. кв.")

    def show_all_city_in_region(self):
        region = input("Enter name region: ")
        city_region = """
        SELECT id, name, region, population, area FROM city WHERE region = %s
        """
        self.DB_CURSOR.execute(city_region, (region,))
        result = self.DB_CURSOR.fetchall()

        for reg in result:
            print(f"Город --- {reg[1]}; id города: {reg[0]}; Область: {reg[2]}; население: {reg[3]} тыс. человек; площадь: {reg[4]} км. кв.")

    def the_biggest_cities(self):
        count_cities = int(input("Enter count the biggest cities: "))
        query = """
        SELECT id, name, region, population, area FROM city 
        ORDER BY population DESC
        LIMIT %s;
        """

        self.DB_CURSOR.execute(query, (count_cities,))
        result = self.DB_CURSOR.fetchall()

        print(f"\n {count_cities} the biggest cities in Belarus:\n")


        for cit in result:
            print(f"Город --- {cit[1]}; id города: {cit[0]}; Область: {cit[2]}; население: {cit[3]} тыс. человек; площадь: {cit[4]} км. кв.")


    def the_biggest_cities_by_population(self):
        count_cities = int(input("Enter count cities: "))
        query = """
        SELECT id, name, region, population, area FROM city 
        ORDER BY population DESC
        LIMIT %s;
        """

        self.DB_CURSOR.execute(query, (count_cities,))
        result = self.DB_CURSOR.fetchall()

        print(f"\n {count_cities} the biggest cities by population in Belarus:\n")


        for cit in result:
            print(f"Город --- {cit[1]}; id города: {cit[0]}; Область: {cit[2]}; население: {cit[3]} тыс. человек; площадь: {cit[4]} км. кв.")

    def information_city_name(self):
        city_name = input("Enter city name: ")
        query = """SELECT id, name, region, population, area FROM city
        WHERE name ILIKE %s
        """
        self.DB_CURSOR.execute(query, (city_name,))
        result = self.DB_CURSOR.fetchone()
        print(f"Город --- {result[1]}; id города: {result[0]}; Область: {result[2]}; население: {result[3]} тыс. человек; площадь: {result[4]} км. кв.")

    def add_attraction(self):
        att_city_id = input("Enter id your city: ")
        att_name = input("Enter name your attraction: ")
        att_type = input("Enter type your attraction: ")

        add_attraction_query = """
                        INSERT INTO attraction (city_id, name, type) VALUES (%s, %s, %s);
                        
        """
        self.DB_CURSOR.execute(add_attraction_query, (att_city_id, att_name, att_type))
        self.DB_CONNECTION.commit()

    def show_all_attraction_city(self):
        city_name = input("Enter name city: ")
        query = """
            SELECT city.name, attraction.name, attraction.type FROM city 
            JOIN attraction ON city.id = attraction.city_id
            WHERE city.name = %s;
            """
        self.DB_CURSOR.execute(query, (city_name, ))
        result = self.DB_CURSOR.fetchall()

        print(f"Attraction for {city_name}:\n")

        for reg in result:
            print(f"Город --- {reg[0]}; достопримечательность: {reg[1]}; тип: {reg[2]}")


    def add_route(self):
        route_city_from_id = input("Enter city A id: ")
        route_city_to_id = input("Enter city B id: ")
        route_transport_type = input("Enter type transport: ")
        schedule = input("Enter schedule your transport")

        add_route_query = """
                INSERT INTO route (city_from_id, city_to_id, transport_type, schedule) VALUES (%s, %s, %s, %s);

            """
        self.DB_CURSOR.execute(add_route_query, (route_city_from_id, route_city_to_id, route_transport_type, schedule))
        self.DB_CONNECTION.commit()

    def show_road_between_cityes(self):
        city_id_one = input("Enter id city A : ")
        city_id_two = input("Enter id city B: ")

        query = """
                    SELECT c_from.name AS city_from, c_to.name AS city_to, route.transport_type, route.schedule FROM route 
                    JOIN city c_from ON c_from.id = route.city_from_id
                    JOIN city c_to ON c_to.id = route.city_to_id
                    WHERE (route.city_from_id = %s AND route.city_to_id = %s)
                        OR (route.city_from_id = %s AND route.city_to_id = %s);
                    """
        self.DB_CURSOR.execute(query, (city_id_one, city_id_two, city_id_two, city_id_one))
        routes = self.DB_CURSOR.fetchall()


        for route in routes:
            print(f"Между городами --- {route[0]} и {route[1]}; ходит транспорт: {route[2]}, c расписанием: {route[3]}")


db_facade = DBFacade()

while True:
    menu = ("\n"
            "1 - show all cityes \n"
            "2 - show_all_city_in_region\n"
            "3 - the biggest cityes\n"
            "4 - the biggest cities by population\n"
            "5 - information about one city\n"
            "6 - add attraction\n"
            "7 - show all attraction in city\n"
            "8 - add route\n"
            "9 - show_road_between_cityes\n"
            "10 - add city in table\n"
            "11 - exit"
            )
    print(menu)
    user_choise = input("Enter an action: ")
    if user_choise == '11':
        break
    elif user_choise == '1':
        db_facade.show_all_city()
        input("\nEnter different sympol for continue.")
    elif user_choise == '2':
        print("Possible to chose next regions: 'Витебская', 'Гродненская', 'Брестская', 'Гомельская', 'Могилевская', 'Минская'")
        db_facade.show_all_city_in_region()
        input("\nEnter different sympol for continue.")
    elif user_choise == '3':
        db_facade.the_biggest_cities()
        input("\nEnter different sympol for continue.")
    elif user_choise == '4':
        db_facade.the_biggest_cities_by_population()
        input("\nEnter different sympol for continue.")
    elif user_choise == '5':
        db_facade.information_city_name()
        input("\nEnter different sympol for continue.")
    elif user_choise == '6':
        db_facade.add_attraction()
        input("\nEnter different sympol for continue.")
    elif user_choise == '7':
        db_facade.show_all_attraction_city()
        input("\nEnter different sympol for continue.")
    elif user_choise == '8':
        db_facade.add_route()
        input("\nEnter different sympol for continue.")
    elif user_choise == '9':
        db_facade.show_road_between_cityes()
        input("\nEnter different sympol for continue.")
    elif user_choise == '10':
        db_facade.add_city()
        input("\nEnter different sympol for continue.")























