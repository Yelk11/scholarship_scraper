from database import Database


class URL_Frontier():
    
    def get_next_url(self):
        db = Database()
        return db.select_next_url()



if __name__ == "__main__":
    frontier = URL_Frontier()
    print(frontier.get_next_url())