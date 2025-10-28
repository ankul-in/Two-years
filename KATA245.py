#kata
#https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b/train/python

def human_years_cat_years_dog_years(human_years):
    cat_years=0
    dog_years=0
    if human_years>=1:
        cat_years,dog_years=15,15
    if human_years>=2:
        cat_years, dog_years = cat_years + 9, dog_years + 9
    if human_years>=3:
        cat_years,dog_years = cat_years+(4*(human_years-2)),dog_years+(5*(human_years-2))

    return [human_years,cat_years,dog_years]

print(human_years_cat_years_dog_years(65))