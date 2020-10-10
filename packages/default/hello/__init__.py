def main(request_data):
    global responseFromNimbella

    # Handle the input and configure the message
    try:
        responseFromNimbella="a Hello world Execution"
    except Exception:
        responseFromNimbella = "Exception Occured"

     # Send the message
    try:

        return {
            "body": {
                "status": (responseFromNimbella)
            }
        }

    except Exception as e:
        return {
            "statusCode": 400,
            "body": {
                "error": str(e)
            }
        }

