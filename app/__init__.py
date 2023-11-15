def perform_operation(x, y, callback):
    result = x + y
    callback(result)

def callback_function(result):
    print(f"The result is: {result}")

# Gọi hàm perform_operation và truyền callback_function làm đối số
perform_operation(10, 20, callback_function)