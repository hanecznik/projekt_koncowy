from selenium.webdriver.common.by import By


class Selectors:
    class MainPage:
        btn_accept = (By.XPATH, "//button[@class='sc-15ih3hi-0 sc-1p1bjrl-9 dRLEBj']")
        txt_search = (By.XPATH, "//input[@class='sc-suk8z4-0 iKWngG']")
        btn_search = (By.XPATH, "//button[@class='sc-1p0xkzn-7 isynLM']")
        logo = (By.XPATH, "//img[@src='//assets.x-kom.pl/public-spa/xkom/7cbf82dd32ab7e88.svg']")
        menu_item_logout = (By.XPATH, "//*[text()='Wyloguj się']")
        menu_dropdown = (
            By.XPATH,
            "//div[@class='sc-13bjpvm-3 iPhtsJ sc-69bo37-2 jXvzLn']//a[@class='sc-1h16fat-0 sc-fz2r3r-4 iUXNCi']")
        btn_login = (By.XPATH, "//*[text()='Zaloguj się']")
        chkbox_hide_unavailable = (
            By.XPATH, "//*[@class='sc-cs8ibv-2 gbuMcQ']//child::span[text()='Ukryj czasowo niedostępne']")
        chkbox_promotions = (By.XPATH, "//span[text()='Promocja']")
        # price_menu = (By.XPATH, "//span[@id='react-select-id3--value-item']")
        price_menu = (By.XPATH, "//span[contains(text(),'Od najtrafniejszych')]")
        price_menu_cheapest_item = (By.XPATH, "//div[@class='Select-menu-outer']//div[text()='Cena: od najtańszych']")
        btn_add_selected_product_to_cart = (By.XPATH, "//h3[contains(@title,'Etui / obudowa na smartfona Ringke Silicone do iPhone 14')]\
    //ancestor::div[@data-name='productCard']//button[@title='Dodaj do koszyka']")
        btn_go_to_cart = (By.XPATH, "//div[@class='sc-1v4lzt5-12 ctESVK']//a[text()='Przejdź do koszyka']")
        number_of_found_items = (By.XPATH, "//span[@class='sc-dntoh-3 PBpWe']")
        not_found_message = (By.XPATH, "//div[@class='sc-4t5dgr-1 eIsJYz']")
        your_account_icon = (By.XPATH, "//div[text()='Twoje konto']")

    class RegisterPage:
        email_validator = (By.XPATH, "//span[@class='sc-1nwq0d4-1 eCBqVz sc-qxbeow-0 gGHaGt']")
        first_name = (By.XPATH, "//input[@name='firstName']")
        last_name = (By.XPATH, "//input[@name='lastName']")
        email = (By.XPATH, "//input[@name='email']")
        password = (By.XPATH, "//input[@name='password']")

    class LoginPage:
        register_account = (By.XPATH, "//a[text()='Załóż konto']")
        login = (By.XPATH, "//input[@name='login']")
        password = (By.XPATH, "//input[@name='password']")
        password2 = (By.XPATH, "//div[@class='sc-14d3hma-9 bkKzJE']//input[@name='password']")
        element_login = (By.XPATH, "//span[text()='Zaloguj się']")
        btn_login = (By.XPATH, "//button[text()='Zaloguj się']")

    class BasketPage:
        btn_favourites = (By.XPATH, "//li[@data-name='basketProduct']//button[@data-action='addToWishlist']")
        btn_add_list = (By.XPATH, "//span[@class='sc-14uv5p9-3 iaPWmS']")
        btn_user_lists = (By.XPATH, "//a[@class='sc-1h16fat-0 sc-fz2r3r-4 iUXNCi']//div[text()='Twoje listy']")
        favourites_lists = (By.XPATH, "//div[@data-name='productPhotoTumbnailWrapper']//img")
        btn_basket = (By.XPATH, "//span[text()='Koszyk']")
        btn_shipment = (By.XPATH, "//button[@class='sc-15ih3hi-0 sc-pvj85d-4 cnUgwg' and text()='Przejdź do dostawy']")
        btn_pickup = (By.XPATH, "//span[text()='Odbiór w salonie x-kom']")

    class OrderPage:
        btn_pickup_location = (By.XPATH, "//button[text()='Wybierz salon']")
        btn_bielany = (By.XPATH, "//div[text()='x-kom Wrocław Bielany' and @class='sc-2jtv1t-17 ghXFDJ']\
                    //ancestor::div[@class='sc-1s1zksu-0 sc-1s1zksu-1 hHQkLn sc-2jtv1t-5 ftHARt']\
                    //span[text()='Wybierz']")
        element_bielany = (By.XPATH, "//div[@class='sc-nhgagy-17 hBxaJW']//*[text()='x-kom Wrocław Bielany']")
        btn_change_pickup_location = (
            By.XPATH, "//div[text()='Zmień' and @class='sc-fznKkj jFVPtS']")
        element_selected = (By.XPATH, "//span[text()='Wybrany']")
        txt_recipent_name = (By.XPATH, "//input[@name='recipientName']")
        txt_recipent_phone_number = (By.XPATH, "//input[@name='recipientPhoneNumber']")
        txt_phone_number = (By.XPATH, "//input[@name='phoneNumber']")
        txt_recipent_email = (By.XPATH, "//input[@name='recipientEmail']")
        txt_email = (By.XPATH, "//input[@name='email']")
        btn_change_recipent = (By.XPATH, "//div[@class='sc-go3mlb-2 kqlbAy']//div[text()='Zmień']")
        btn_new_recipent = (By.XPATH, "//div[text()='Dodaj nowe dane odbiorcy']")
        btn_save = (By.XPATH, "//button[@class='sc-15ih3hi-0 sc-sl4yii-4 dZkLBW'][text()='Zapisz']")
        btn_accept = (By.XPATH, "//div[text()='Zatwierdź']")
        element_in_pickup_location = (
            By.XPATH,
            "//label[@class='sc-116iin7-0 gvmmDx sc-nhgagy-2 bhAxwF']//following::span[text()='Przy odbiorze']")
        btn_goto_summary = (By.XPATH, "//button[text()='Przejdź do podsumowania']")
        txt_name_surname = (By.XPATH, "//p[@class='sc-1nka6h7-0 sc-1nka6h7-2 bRdujy' and text()='Noname Test']")
        txt_email_info = (By.XPATH,
                          "//p[@class='sc-1nka6h7-0 sc-1nka6h7-1 eETCwo' and text()='e-mail: testowanie.strony.2023@gmail.com']")
        txt_phone_info = (By.XPATH, "//p[@class='sc-1nka6h7-0 jEqlzJ' and text()='tel. 55 533 31 11']")
        btn_buy_and_pay = (By.XPATH, "//button[text()='Kupuję i płacę']")
        element_order_status = (By.XPATH, "//h1[@class='sc-ewx300-10 ljxnF']")
