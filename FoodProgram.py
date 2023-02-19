import FoodClass as fc

# this dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]

dict = {
    "trans1": ["2/15/2023", "The Lone Patty", 17, 569],
    "trans2": ["2/15/2023", "The Octobreakfast", 18, 569],
    "trans3": ["2/15/2023", "The Octoveg", 16, 570],
    "trans4": ["2/15/2023", "The Octoburger", 20, 570],
}

order_total = 0
order_items = []

# create a customer instance

# Danni
# customer_id = 570
# name = "Danni Sellyar"
# address = "97 Mitchell Way Hewitt Texas 76712"
# emial = "dsellyarft@gmpg.org"
# phone = "254-555-9362"
# member_status = False

# Aubree
customer_id = 569
name = "Aubree Himsworth"
address = "1172 Moulton Hill Waco Texas 76710"
emial = "ahimsworthfs@list-manage.com"
phone = "254-555-2273"
member_status = True

customer = fc.Customer(
    customer_id,
    name,
    address,
    emial,
    phone,
    member_status,
)
for customerid, trans in dict.items():
    if trans[3] == customer.get_customerid():
        order_items.append({"name": trans[1], "cost": trans[2]})
        order_total += trans[2]

if customer.get_member_status() == True:
    discount = order_total * 0.2
    discounted_total = order_total - discount

if customer.get_member_status() == False:
    order_total = order_total

# print report
print(f"Customer Name: {customer.get_name()}")
print(f"Phone: {customer.get_phone()}")
for item in order_items:
    print(f'Order Item: {item["name"]} Price: ${item["cost"]:.2f}')

if customer.get_member_status() == True:
    print(f"Total Cost: ${order_total:.2f}")
    print(f"Member Discount: ${discount:.2f}")
    print(f"Total Cost After Discount: ${discounted_total:.2f}")


if customer.get_member_status() == False:
    print(f"Total Cost: ${order_total:.2f}")
