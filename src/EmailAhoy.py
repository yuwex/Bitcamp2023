from time import sleep
from threading import Thread

from game import Game
from email_watcher import Watcher

class GameManager:

    game: Game
    watcher: Watcher

    def __init__(self, game: Game, watcher: Watcher, interval = 5):
        self.game = game
        self.interval = interval

        self.running = False
        self.update_thread = None

        self.watcher = watcher
    
    def update(self):
        while self.running:
            read = self.watcher.update()
            unread = self.watcher.get_unread_count()
            self.game.update(read, unread)
            sleep(self.interval)

    def run(self):
        self.running = True
        self.update_thread = Thread(target = self.update, daemon=True)
        self.update_thread.start()

def main():
    while(True):
        print("Running")
        sleep(1)

if __name__ == "__main__":
    print("Started")

    watcher = Watcher()
    count = watcher.get_unread_count()
    game = Game(count)

    gm = GameManager(game, watcher)
    gm.run()

    game.start()
