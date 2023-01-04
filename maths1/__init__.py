import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
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
        return func.HttpResponse(
            "Invalid operation! Please specify a valid operation: add, multiply, divide, or subtract",
            status_code=400
        )

    # Return the result as a string
    return func.HttpResponse("Result: " + str(result))

#https://vjfunctionapp1234.azurewebsites.net/api/maths1?operation=add&num1=1001&num2=456