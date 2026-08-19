# Computational Thinking Exercise

## Smart School Canteen Queue

*Name:* Yuan Ezekiel R. Ecal<br>
*Section:* Magnesium<br>
*Last Name:* Ecal<br>
*Date:* August 11, 2026

---

## Step 1: Identify the Big Problem

### Main Problem
The school vending machine is inefficient, prone to operational errors (inaccurate change and slow processing), and lacks user confirmation and automated inventory management.

---

## Step 2: Identify the Sub-Problems

1. Change Calculation Error: The system fails to consistently calculate or dispense the exact change owed (Money Inserted - Item Price).

2. Lack of Inventory Tracking: No automated monitor to track remaining stock levels or send alerts when items run out.

3. User Selection Errors: Lack of visual confirmation or intuitive interface leading to accidental item choices.

4. Slow Transaction Speed: Inefficient code structure or transaction flow causing delays during high-traffic periods.

---

## Step 3: Apply Computational Thinking Skills

| Sub-Problem | CT Skill | Proposed Solution |
| :---        | :---     | :---              |
| *1. Incorrect change* | *Algorithm Design* | Create a step-by-step mathematical logic block that subtracts the item price from the inserted cash and dispenses exact coin denominations.|
| *2. Inventory Alerts* | *Pattern Recognition* | Monitor stock counts automatically (Stock = Stock - 1). Trigger a digital alert or signal when Stock <= 2.|
| *3. User Selection Errors* | *Abstraction* | Simplify the ordering process by displaying the selected item's name and price on a screen, requiring an "OK/Confirm" press before dispensing.|
| *4. Slow Performance* | *Decomposition* | Break the vending routine into separate, optimized subroutines (Payment Processing, Item Dispensing, and Screen Reset) so the system resets quickly for the next user.|

---

## Step 4: Algorithmic Solution

### Selected Sub-Problem
Automatic Point of Sale and Payment Calculation (Sub-Problem 2)

### Pseudocode
START
    SET item_price = READ_ITEM_PRICE()
    SET current_stock = READ_ITEM_STOCK()
    
    // Check Inventory
    IF current_stock == 0 THEN
        DISPLAY "Item Out of Stock"
        SEND_ALERT_TO_STAFF()
        EXIT
    ENDIF

    // Process Payment
    DISPLAY "Insert Payment"
    INPUT inserted_amount
    
    IF inserted_amount < item_price THEN
        DISPLAY "Insufficient Funds"
        RETURN inserted_amount
    ELSE
        // Calculate Change
        SET change_due = inserted_amount - item_price
        
        // Dispense and Update
        DISPENSE_ITEM()
        DISPENSE_CHANGE(change_due)
        UPDATE_STOCK(current_stock - 1)
        
        DISPLAY "Transaction Complete"
    ENDIF
END