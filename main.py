#import azure.functions as func

def main():
    # Get the query string parameters
    num1 = req.params.get('num1')
    num2 = req.params.get('num2')
    operation = req.params.get('operation')

    # Convert the query string parameters to integers
    num1 = int(num1)
    num2 = int(num2)

    # Perform the requested operation
    if operation == 'add':
        result = num1 + num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        result = num1 / num2
    elif operation == 'subtract':
        result = num1 - num2
    else:
        return (
            "Invalid operation! Please specify a valid operation: add, multiply, divide, or subtract",
            status_code=400
        )

    # Return the result as a string
    return ("Result: " + str(result))
