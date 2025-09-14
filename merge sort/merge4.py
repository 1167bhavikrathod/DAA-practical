'''Apply Merge Sort to sort employee records
(EmployeeID, Name, Salary) by Salary in ascending
order.'''


def merge_sort(employees):
    if len(employees) <= 1:
        return employees
    
    # Divide the list into two halves
    mid = len(employees) // 2
    left = merge_sort(employees[:mid])
    right = merge_sort(employees[mid:])
    
    # Merge the sorted halves
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    # Compare employee records by Salary and merge in ascending order
    while i < len(left) and j < len(right):
        if left[i][2] >= right[j][2]:  # Compare Salary (index 2 of tuple)
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining records from left list, if any
    result.extend(left[i:])
    # Add remaining records from right list, if any
    result.extend(right[j:])
    return result

# Function to get employee records from user without validation
def get_employee_records():
    n = int(input("Enter the number of employees: "))
    employees = []
    print(f"Enter details for {n} employees (EmployeeID Name Salary):")
    for i in range(n):
        emp_id, name, salary = input(f"Employee {i+1}: ").split()
        employees.append((int(emp_id), name, float(salary)))
    return employees

# Main program
if __name__ == "__main__":
    # Get employee records from user
    employees = get_employee_records()
    """ employees = [
        (101, "Alice Smith", 55000.0),
        (102, "Bob Johnson", 72000.0),
        (103, "Carol Williams", 48000.0),
        (104, "David Brown", 65000.0),
        (105, "Emma Davis", 39000.0),
        (106, "Frank Wilson", 82000.0),
        (107, "Grace Taylor", 51000.0),
        (108, "Henry Anderson", 78000.0),
        (109, "Isabella Martinez", 60000.0),
        (110, "James Thomas", 45000.0)
    ]"""
    
    # Print original records
    print("\nOriginal employee records:")
    for emp in employees:
        print(f"ID: {emp[0]}, Name: {emp[1]}, Salary: {emp[2]}")
    
    # Sort records by Salary
    sorted_employees = merge_sort(employees)
    
    # Print sorted records
    print("\nSorted employee records by Salary (ascending):")
    for emp in sorted_employees:
        print(f"ID: {emp[0]}, Name: {emp[1]}, Salary: {emp[2]}")