# apr-3188ce3cd24561acfe6ca6827c5a0e29

import requests as rq

BASE_URL = "http://127.0.0.1:8000"
KEY = "32d174c3c51ebdf904acb4beb816c8c1a321c2ab"

# # Register
# register = rq.post(f"{BASE_URL}/api/v1/users/register/", 
# 			data={
# 				'email':'TechSarvarbek2@gmail.com',
# 				'password':'123456',
# 				'first_name':'Sarvarbek',
# 				'last_name':'Aminov',
# 				'telegram_name':'TechSarvarbek'
# 			})
# Login

# login = rq.get(f"{BASE_URL}/api/v1/users/login/asd@gmail.com/qweqweasd")

# User activete [GET, POST]
# user_activate = rq.get(f"{BASE_URL}/api/v1/users/active/31947", 
# 			headers={'Authorization':f"Token {KEY}"})


# User profile
# user_profile = rq.get(f"{BASE_URL}/api/v1/users/profile",
# 		headers={'Authorization':f'token {KEY}'})

# User update
# user_update = rq.put(f"{BASE_URL}/api/v1/users/profile/",
# 		data={
# 			'password':'123456',
# 		},
# 		headers={'Authorization':f'token {KEY}'})


# print(register, register.json())
# print(user_activate, user_activate.json())
# print(user_profile, user_profile.json())
# print(user_update, user_update.json())
# print(login, login.json())

# -------------- Company --------------------
# locations_data = [
#     {'name': 'Bukhara'},
#     {'name': 'Gijduvon'},
#     {'name': 'AQSH'},
#     {'name': 'Nyu-York'},
# ]
# keywords_data = [
#     {'keyword': 'Tech'},
#     {'keyword': 'Programming'},
# ]
# ad_data = {
    # 'headline': 'TechSarvarbek',
    # 'description': 'Tech with Sarvarbek ...',
    # 'ad_type': 'google',
    # 'price': 250,
    # 'keywords': keywords_data,
# }
# data = {
    # 'locations': locations_data,
    # 'ad': ad_data,
    # 'name': 'ProgUz',
    # 'website': 'www.proguz.com',
    # 'launge': 'English',
# }
# create_company = rq.post(f"{BASE_URL}/api/v1/company/create/",
# 		json=data,
# 		headers={'Authorization':f'token {KEY}'})

##################################################






# companies
# companies = rq.get(f"{BASE_URL}/api/v1/company/companies/",
# 			headers={'Authorization':f'token {KEY}'})

# detail company
# company = rq.get(f"{BASE_URL}/api/v1/company/detail/4",
# 			headers={'Authorization':f'token {KEY}'})

##########################################
# ad_data = {
# 	'headline':"O'zbek dasturchilar uchun",
# 	'ad_type':'twitter',
# 	'price':1000,
# 	'keywords':[
# 		{'keyword':'dev'},
# 		{'keyword':'programming'},
# 	]
# }

# update detail company
# update_company = rq.put(f"{BASE_URL}/api/v1/company/detail/5/",
# 			json={
# 				'name':'Tech',
# 				'website':'TechSarvarbek.com',
# 				'launge':'Uzbek',
# 				'ad':ad_data,
# 				'locations': [
# 					{'name': 'Bukhara'},
# 					{'name': 'Tashkent'},
# 					{'name': 'AQSH'},
# 				]
# 			},
# 			headers={'Authorization':f'token {KEY}'})
#####################################
# delete detail company
# delete_company = rq.delete(f"{BASE_URL}/api/v1/company/detail/5",
# 			headers={'Authorization':f'token {KEY}'})




# print(create_company, create_company.json())
# print(companies, companies.json())
# print(company, company.json())
# print(update_company, update_company.json())
# print(delete_company, delete_company.json())


##########################################

# payment = rq.post(f"{BASE_URL}/api/v1/payment/create/",
#         data={
#             'price':120
#         },
#         headers={'Authorization':f'token {KEY}'})


# payments = rq.get(f"{BASE_URL}/api/v1/payment/payments/",
#         headers={'Authorization':f'token {KEY}'})





# print(payment, payment.json())
# print(payments, payments.json())
