class Utility:
    
    @staticmethod
    def is_integer(num):
        try:
            if (int(num) - num) == 0:
                return True
        except:
            return False