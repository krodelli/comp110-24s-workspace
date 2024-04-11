"""Practice writing class called Profile."""

class Profile: 

    username: str 
    private: bool 

    def __init__(self, username_input: str):
        """Create a new Profile object."""
        self.username = username_input 
        self.private = True 

    def tweet(self, msg: str) -> None:
        """If profile is public, print msg."""
        if self.private is False:  # this means not self.private
            print(msg)


# instantiation 
user1: Profile = Profile("110_rulez") # construct by calling the constructor. calling the name of the class instead of init...this calls init, creates user1 object where 110 rules is input, and user.private is True. 
user1.private = False  # updating user1 to be False
user1.tweet("OOP is cool!") # for method, first argument comes in front then a period, then the method name, and rest of objects in ()
