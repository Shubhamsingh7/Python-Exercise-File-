#Program for keyword argument


def address(name,pin,*var):
    print(f"name={name}")
    print(f"pin={pin}")
    print(f"Address={var}")

address("shubham",102154,"vrandavan nagri","trivedipur road","Lucknow Crossing","Pandav nagar","Delhi")