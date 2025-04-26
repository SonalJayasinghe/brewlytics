import sqlite3

def create_database():
    conn = sqlite3.connect('data/coffee_data.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS coffee_samples (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        country_of_origin TEXT,
        number_of_bags TEXT,
        farm_name TEXT,
        bag_weight TEXT,
        lot_number TEXT,
        in_country_partner TEXT,
        mill TEXT,
        harvest_year TEXT,
        ico_number TEXT,
        grading_date TEXT,
        company TEXT,
        owner TEXT,
        altitude TEXT,
        variety TEXT,
        region TEXT,
        status TEXT,
        producer TEXT,
        processing_method TEXT,
        aroma TEXT,
        uniformity TEXT,
        flavor TEXT,
        clean_cup TEXT,
        aftertaste TEXT,
        sweetness TEXT,
        acidity TEXT,
        overall TEXT,
        body TEXT,
        defects TEXT,
        balance TEXT,
        total_cup_points TEXT,
        moisture TEXT,
        color TEXT,
        category_one_defects TEXT,
        category_two_defects TEXT,
        quakers TEXT
    )
    ''')
    conn.commit()
    conn.close()

create_database()