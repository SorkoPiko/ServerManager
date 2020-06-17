class files(object):
    avatars = {}
    ids = {}
    
    @staticmethod
    def get_avatars():
        with open(f"infox/avatars.txt") as file:
            for line in file:
                line = line.rstrip('\n')
                username, info = line.split('/')
                avatars[username] = info
        return avatars
    
    @staticmethod
    def store_avatars(username, info):
        with open(f"infox/avatars.txt", 'a') as file:
            file.write('\n' + username + '/' + info)
            
    @staticmethod
    def get_ids():
        with open(f"infox/ids.txt") as file:
            for line in file:
                line = line.rstrip('\n')
                username, info = line.split('/')
                ids[username] = info
        return ids
    
    @staticmethod
    def store_ids(username, info):
        with open(f"infox/ids.txt", 'a') as file:
            file.write('\n' + username + '/' + info)
            