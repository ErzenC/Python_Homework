# 7. Data Integrity Check
# accounts = [
#    {"account_id": 1, "owner": "John", "balance": 500},
#    {"account_id": 2, "owner": "", "balance": 300},
#    {"account_id": 3, "owner": "Anna", "balance": -100},
#    {"account_id": None, "owner": "Mike", "balance": 400}
# ]
# Validate:
# •	account_id must not be None 
# •	owner must not be empty 
# •	balance must be positive 
# Return:
# •	invalid records 
# •	explanation for each issue

accounts = [
    {"account_id": 1, "owner": "John", "balance": 500},
    {"account_id": 2, "owner": "", "balance": 300}, 
    {"account_id": 3, "owner": "Anna", "balance": -100},
    {"account_id": None, "owner": "Mike", "balance": 400}
]  

def validate_accounts(data): #Funksioni per validimin e llogarive, duke kontrolluar cdo kriter dhe duke mbledhur problemet ne nje liste
    invalid_records = [] #Lista per te ruajtur llogarite e pavlefshme dhe arsyet e tyre
    for account in data: #Iterimi i cdo llogarie ne liste
        issues = [] #Lista per te mbledhur problemet e cdo llogarie
        if account["account_id"] is None: #Kontrolli nese account_id eshte None dhe shtimi i problemit ne liste nese eshte e vertete
              issues.append("account_id is None") #Shtimi i problemit "account_id is None" ne liste nese account_id eshte None
        if account["owner"] == "": #Kontrolli nese owner eshte i zbrazet dhe shtimi i problemit ne liste nese eshte e vertete
            issues.append("owner is empty")#Shtimi i problemit "owner is empty" ne liste nese owner eshte i zbrazet
        if account["balance"] < 0: #Kontrolli nese balance eshte negativ dhe shtimi i problemit ne liste nese eshte e vertete
            issues.append("balance is negative")#Shtimi i problemit "balance is negative" ne liste nese balance eshte negativ
        if issues:#Nese ka probleme te gjetura per llogarine aktuale, shtimi i saj ne listen e llogarive te pavlefshme me arsyet e gjetura
            invalid_records.append({"account": account, "issues": issues})#Shtimi i llogarise aktuale dhe problemeve te saj ne listen e llogarive te pavlefshme nese ka probleme te gjetura
    return invalid_records#Kthimi i listes se llogarive te pavlefshme me arsyet e gjetura

print("Invalid accounts:")
for record in validate_accounts(accounts):
    print(record)
#OUTPUT:
# Invalid accounts:
# {'account': {'account_id': 2, 'owner': '', 'balance': 300}, 'issues': ['owner is empty']}
# {'account': {'account_id': 3, 'owner': 'Anna', 'balance': -100}, 'issues': ['balance is negative']}
# {'account': {'account_id': None, 'owner': 'Mike', 'balance': 400}, 'issues': ['account_id is None']}
