from time import sleep
from threading import Thread

from game import Game
from email_watcher import Watcher

class GameManager:

    game: Game

    def __init__(self, game: Game, interval = 5):
        self.game = game
        self.interval = interval

        self.running = False
        self.update_thread = None

        self.watcher = Watcher()
    
    def update(self):
        while self.running:
            read = self.watcher.update()
            unread = self.watcher.get_unread_count()
            game.update(read, unread)
            sleep(self.interval)

    def run(self):
        self.running = True
        self.update_thread = Thread(target = self.update, daemon=True)


INTERVAL = 5
_running = True

def update_emails(game: Game):
    while(_running):
        game.update()
        sleep(INTERVAL)

def main():
    while(True):
        print("hi")
        sleep(1)

if __name__ == "__main__":
    game = Game()

    t = Thread(target = update_emails, args=(game,))
    t.start()

    main()