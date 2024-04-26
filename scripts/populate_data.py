import sys, os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'exclusive.settings'
application = get_wsgi_application()

from api.models import Category, subCategory


def populate_overall_categories():
    overall_categories = [
        "Women's Fashion",
        "Men's Fashion",
        "Electronics",
        "Home & Lifestyle",
        "Medicine",
        "Sports & Outdoor",
        "Baby's & Toys",
        "Groceries & Toys",
        "Health & Beauty"
    ]
    print("TOTAL OVERALL CATEGORIES")
    print(len(overall_categories))
    count = 0
    for cat in overall_categories:
        if Category.objects.filter(name=cat).exists():
            continue
        else:
            Category.objects.create(name=cat)
            count += 1
    print("NEWLY CREATED")
    print(count)

def populate_sub_categories():
    sub_categories = [
        "Phones",
        "Computers",
        "SmartWatch",
        "Camera",
        "HeadPhones",
        "Gaming"
    ]
    print("TOTAL SUB CATEGORIES")
    print(len(sub_categories))
    count = 0
    for cat in sub_categories:
        if subCategory.objects.filter(name=cat).exists():
            continue
        else:
            cati = Category.objects.get(name="Electronics")
            subCategory.objects.create(name=cat, category=cati)
            count += 1
    print("NEWLY CREATED")
    print(count)


def main():
    populate_overall_categories()
    populate_sub_categories()

if __name__ == "__main__":
    main()