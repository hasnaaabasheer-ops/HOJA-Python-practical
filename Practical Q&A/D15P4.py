def show_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
show_profile(name="John", age=30, city="delhi")