import requests
import sys

def get_employee_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com/'
    
    # Fetch employee information
    response = requests.get(f'{base_url}users/{employee_id}')
    user_data = response.json()
    employee_name = user_data.get('name')
    
    # Fetch employee's todo list
    response = requests.get(f'{base_url}todos?userId={employee_id}')
    todos = response.json()
    
    # Calculate progress
    total_tasks = len(todos)
    done_tasks = sum(1 for todo in todos if todo['completed'])
    
    # Display progress
    print(f'Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):')
    
    for todo in todos:
        if todo['completed']:
            print(f'\t{todo["title"]}')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
