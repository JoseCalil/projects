import pandas as pd

def add_card(card_data, card_name, quantity, condition, value):
    # Check if card already exists in the DataFrame
    existing_card = card_data[(card_data['CardName'] == card_name) & (card_data['Condition'] == condition)]

    if not existing_card.empty:
        # Card already exists, update quantity
        card_data.loc[existing_card.index, 'Quantity'] += quantity
    else:
        # Card doesn't exist, add a new row
        card_data = card_data.append({"CardName": card_name, "Quantity": quantity, "Condition": condition, "Value": value}, ignore_index=True)

    return card_data

# Load existing data from Excel (if any)
try:
    card_data = pd.read_excel('card_collection.xlsx')
except FileNotFoundError:
    # If the file doesn't exist, create an empty DataFrame
    columns = ["CardName", "Quantity", "Condition", "Value"]
    card_data = pd.DataFrame(columns=columns)

# Sample data entry
card_name = input("Enter the card name: ")
quantity = int(input("Enter the quantity: "))
condition = input("Enter the condition: ")
value = 10  # Replace with actual value obtained from web scraping

# Update card data
card_data = add_card(card_data, card_name, quantity, condition, value)

# Export updated DataFrame to Excel
card_data.to_excel('card_collection.xlsx', index=False)