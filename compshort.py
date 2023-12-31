import openpyxl

def shorten_company_name(company_name):
    # Split company name
    words = company_name.split()

    # Check if there is two words in the company name
    if len(words) >= 2:
        # Check if the other word is "AB" (AB is like Corp in Sweden) and remove it
        if words[1].upper() == "AB":
            shortened_name = words[0].lower()
        else:
            # Take the first two words and make lowercase only
            shortened_name = ' '.join(words[:2]).lower()
    else:
        # Only take the first word and change to lowercase only
        shortened_name = words[0].lower()

    # Remove space
    shortened_name = shortened_name.replace(" ", "")

    # Replace unwanted characters
    shortened_name = shortened_name.replace("å", "a")
    shortened_name = shortened_name.replace("ä", "a")
    shortened_name = shortened_name.replace("ö", "o")
    shortened_name = shortened_name.replace("é", "e")
    shortened_name = shortened_name.replace("/", "")
    shortened_name = shortened_name.replace("´", "")
    shortened_name = shortened_name.replace("-", "")
    shortened_name = shortened_name.replace(".", "")
    shortened_name = shortened_name.replace("’", "")

    return shortened_name

# Path to Excel document
wb = openpyxl.load_workbook("companies.xlsx")
ws = wb.active

for row in ws.values:
    for company_name in row:
        shortened_name = shorten_company_name(company_name)
        print(shortened_name)

'''# For testing
company_name = input("Company name: ")
shortened_name = shorten_company_name(company_name)

print("Username: ", shortened_name)
'''