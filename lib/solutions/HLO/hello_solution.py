
class HelloSolution:
    
    # friend_name = unicode string
    # say hello to the world
    def hello(self, friend_name):
        if not isinstance(friend_name, str):
            raise TypeError("input should be string")
        
        hello = f"Hello, World!"

        return hello

        


