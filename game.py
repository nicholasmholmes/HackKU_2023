import socket
import threading
import sys
import pygame

class GameClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))

    def send_move(self, move):
        self.sock.sendall(move.encode())

    def receive_game_state(self):
        data = self.sock.recv(1024)
        return data.decode()

    def close(self):
        self.sock.close()

class GameServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen(1)
        self.players = []
        self.connections = []
        self.game = None

    def accept_players(self):
        print("accept plyrs" + str(len(self.players)))
        while len(self.players) < 1:
            print('inside while')
            conn, addr = self.sock.accept()
            self.connections.append(conn)
            self.players.append(addr)
            print(f'Player {len(self.players)} connected from {addr}')
    
    def send_game_state(self, state):
        for conn in self.connections:
            conn.sendall(state.encode())

    def close(self):
        for conn in self.connections:
            conn.close()
        self.sock.close()

class Game:
    def __init__(self, player):
        self.player = player
        self.client = None
        self.server = None
        self.running = False

    def start_server(self):
        self.server = GameServer('', 5555)
        self.server_thread = threading.Thread(target=self.server.accept_players)
        self.server_thread.start()
        print("Server started")

    def start_client(self, host):
        print('starting connection')
        self.client = GameClient(host, 5555)
        print('connecting...')
        self.game_thread = threading.Thread(target=self.run_client)
        self.game_thread.start()
        print('starting thread')

    def run_server(self):
        print('1')
        self.server_thread.join()
        print('1.5')
        self.server.game = self
        print('2')
        self.game_loop()
        print('3')

    def run_client(self):
        while not self.running:
            print('waiting')
            pygame.time.wait(100)
        self.game_loop()

    def game_loop(self):
        while True:
            if self.player == 'server':
                self.server.send_game_state(str(self))
            elif self.player == 'client':
                game_state = self.client.receive_game_state()
                self.apply_game_state(game_state)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.apply_move()
                    self.running = True

    def apply_move(self):
        # Code to apply move here
        pass

    def apply_game_state(self, state):
        # Code to update game state here
        pass

    def quit(self):
        if self.player == 'server':
            self.server.close()
        elif self.player == 'client':
            self.client.close()
        sys.exit()

    def __str__(self):
        # Code to serialize game state as a string here
        pass

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    font = pygame.font.SysFont(None, 32)
    clock = pygame.time.Clock()

    server_button = font.render('Host Game', True, (255, 255, 255))
    client_button = font.render('Join Game', True, (255, 255, 255))
    button_rect = server_button.get_rect
    server_button_rect = server_button.get_rect(center=(320, 200))
    client_button_rect = client_button.get_rect(center=(320, 300))

    game = None
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if server_button_rect.collidepoint(event.pos):
                    game = Game('server')
                    print('hooray')
                    game.start_server()
                    print('waahoo')
                    game.run_server()
                    print('yipee')
                elif client_button_rect.collidepoint(event.pos):
                    host = input('Enter server IP address: ')
                    game = Game('client')
                    game.start_client(host)
                    game.running = True
        screen.fill((0, 120, 0))
        screen.blit(server_button, server_button_rect)
        screen.blit(client_button, client_button_rect)
        pygame.display.update()
        clock.tick(60)
        if game is not None and game.player == 'server' and game.server.game is not None:
            break
    while True:
        print("working")
        # Main game loop here
        pass

main()