def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    Parameters:
    - price (float): The original price of the item.
    - discount_percent (float): The discount percentage to apply.
    
    Returns:
    - float: The final price after applying the discount or the original price if no discount is applied.
    """
    if discount_percent >= 20:
        final_price = price * (1 - discount_percent / 100)
    else:
        final_price = price
    return final_price

def main():
    try:
        # Prompt the user to enter the original price
        price = float(input("Enter the original price of the item: "))
        # Prompt the user to enter the discount percentage
        discount_percent = float(input("Enter the discount percentage: "))
        
        # Calculate the final price
        final_price = calculate_discount(price, discount_percent)
        
        # Print the final price
        print(f"The final price after applying the discount is: ${final_price:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
