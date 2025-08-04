def insert_into_data(name : str,age: int):
    if type(name) is  str and type(age) is  int:
     if age < 0:
        raise ValueError("Age cannot be negative")
     else:
      print("NAME:", name)
      print("AGE:", age)
    else:  
     raise TypeError("Name must be a string and age must be an integer")

insert_into_data("John Doe", -30)
