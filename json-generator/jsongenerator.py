import json
from employee import employee_name, age, title, details

def create_dict(name, age, title):

    return {"first_name": name, "age": int(age), "title": title}

def write_json_to_file(json_obj, output_file):

    with open(output_file, "w") as f:
        f.write(json_obj)

def main():
    # Print the contents of details() -- This should print the details of an employee
    details()

    # Create employee dictionary
    employee_dict = create_dict(employee_name, age, title)
    print("employee_dict: " + str(employee_dict))

    json_object = json.dumps(employee_dict)
    print("json_object: " + str(json_object))

    # Write out the json object to file
    write_json_to_file(json_object, "employee.json")

if __name__ == "__main__":
    main()