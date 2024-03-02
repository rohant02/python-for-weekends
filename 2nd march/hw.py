class AntIncident(Exception):
    
    pass

def go_to_cookies(ant_path):
    
    if ant_path == "cupboard with dishes":
        raise AntIncident("Ants went to the wrong place!")
    elif ant_path == "cookies":
        print("The ants have successfully reached the cookies!")
    else:
        print("The ants are lost.")


try:
    
    ant_destination = "cookies"  
    go_to_cookies(ant_destination)
except AntIncident as e:
    
    print(f"Ant Incident: {e}")