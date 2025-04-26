def extract_and_save_coffee_data(driver):
    import sqlite3
    from selenium.webdriver.common.by import By

    conn = sqlite3.connect('data/coffee_data.db')
    cursor = conn.cursor()

    def get_text(xpath):
        try:
            return driver.find_element(By.XPATH, xpath).text.strip()
        except:
            return ""

    data = {
        'country_of_origin': get_text("//th[text()='Country of Origin']/following-sibling::td[1]"),
        'number_of_bags': get_text("//th[text()='Number of Bags']/following-sibling::td[1]"),
        'farm_name': get_text("//th[text()='Farm Name']/following-sibling::td[1]"),
        'bag_weight': get_text("//th[text()='Bag Weight']/following-sibling::td[1]"),
        'lot_number': get_text("//th[text()='Lot Number']/following-sibling::td[1]"),
        'in_country_partner': get_text("//th[text()='In-Country Partner']/following-sibling::td[1]"),
        'mill': get_text("//th[text()='Mill']/following-sibling::td[1]"),
        'harvest_year': get_text("//th[text()='Harvest Year']/following-sibling::td[1]"),
        'ico_number': get_text("//th[text()='ICO Number']/following-sibling::td[1]"),
        'grading_date': get_text("//th[text()='Grading Date']/following-sibling::td[1]"),
        'company': get_text("//th[text()='Company']/following-sibling::td[1]"),
        'owner': get_text("//th[text()='Owner']/following-sibling::td[1]"),
        'altitude': get_text("//th[text()='Altitude']/following-sibling::td[1]"),
        'variety': get_text("//th[text()='Variety']/following-sibling::td[1]"),
        'region': get_text("//th[text()='Region']/following-sibling::td[1]"),
        'status': get_text("//th[text()='Status']/following-sibling::td[1]"),
        'producer': get_text("//th[text()='Producer']/following-sibling::td[1]"),
        'processing_method': get_text("//th[text()='Processing Method']/following-sibling::td[1]"),
        'aroma': get_text("//th[text()='Aroma']/following-sibling::td[1]"),
        'uniformity': get_text("//th[text()='Uniformity']/following-sibling::td[1]"),
        'flavor': get_text("//th[text()='Flavor']/following-sibling::td[1]"),
        'clean_cup': get_text("//th[text()='Clean Cup']/following-sibling::td[1]"),
        'aftertaste': get_text("//th[text()='Aftertaste']/following-sibling::td[1]"),
        'sweetness': get_text("//th[text()='Sweetness']/following-sibling::td[1]"),
        'acidity': get_text("//th[text()='Acidity']/following-sibling::td[1]"),
        'overall': get_text("//th[text()='Overall']/following-sibling::td[1]"),
        'body': get_text("//th[text()='Body']/following-sibling::td[1]"),
        'defects': get_text("//th[text()='Defects']/following-sibling::td[1]"),
        'balance': get_text("//th[text()='Balance']/following-sibling::td[1]"),
        'total_cup_points': get_text("//th[text()='Total Cup Points']/following-sibling::td[1]"),
        'moisture': get_text("//th[text()='Moisture']/following-sibling::td[1]"),
        'color': get_text("//th[text()='Color']/following-sibling::td[1]"),
        'category_one_defects': get_text("//th[text()='Category One Defects']/following-sibling::td[1]"),
        'category_two_defects': get_text("//th[text()='Category Two Defects']/following-sibling::td[1]"),
        'quakers': get_text("//th[text()='Quakers']/following-sibling::td[1]")
    }

    placeholders = ', '.join('?' * len(data))
    columns = ', '.join(data.keys())
    sql = f"INSERT INTO coffee_samples ({columns}) VALUES ({placeholders})"
    cursor.execute(sql, list(data.values()))

    conn.commit()
    conn.close()
