from selenium import webdriver

TIME_TO_WAIT = 10

DATA_FOR_EDIT = {
    'name': 'Gabi',
    'email': 'GabiDaCoder@gmail.com',
    'interests': 'Coding / Debugging'
}


class PageFactory:
    def __init__(self):
        self.driver = self.start_driver()
        self.driver.implicitly_wait(TIME_TO_WAIT)
        self.driver.get('http://localhost:3000/')

    def start_driver(self):
        driver = webdriver.Chrome()
        return driver

    def edit_profile_button(self):
        self.driver.find_element_by_xpath('//*[@id="container"]/button').click()

    def name_editor(self):
        name_obj = self.driver.find_element_by_id('input-name')
        name_obj.clear()
        name_obj.send_keys(DATA_FOR_EDIT['name'])

    def email_editor(self):
        email_obj = self.driver.find_element_by_id('input-email').clear()
        # email_obj.clear()
        email_obj.send_keys(DATA_FOR_EDIT['email'])
        return email_obj

    def interest_editor(self):
        interest_obj = self.driver.find_element_by_id('input-interest').clear()
        # interest_obj.clear()
        interest_obj.send_keys(DATA_FOR_EDIT['interests'])
        return interest_obj

    def update_profile_button(self):
        self.driver.find_element_by_xpath('//*[@id="container-edit"]/button').click()

    def get_data_from_mongo_express(self):
        self.driver.get('http://localhost:8080/')
        # click my-db button
        self.driver.find_element_by_xpath(
            '/html/body/div/div[2]/div/div[1]/div[2]/table/tbody/tr[4]/td[2]/h3/a').click()
        # click view
        self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div[1]/div[2]/table/tbody/tr/td[5]/h3/a").click()

    def mongo_name(self):
        name = self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div[5]/table/tbody/tr/td[5]/div').text
        return name

    def mongo_email(self):
        email = self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div[5]/table/tbody/tr/td[3]/div')
        return email

    def mongo_interest(self):
        interests = self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div[5]/table/tbody/tr/td[4]/div')
        return interests


