from flask import Flask, render_template
from flask_socketio import SocketIO, emit, join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# A dictionary to store the state of the game
game_state = {
    'players': {},
    'balls': [],
}

# Event handler for when a client connects to the server
@socketio.on('connect')
def on_connect():
    print('Client connected')

# Event handler for when a client disconnects from the server
@socketio.on('disconnect')
def on_disconnect():
    print('Client disconnected')

# Event handler for when a player joins the game
@socketio.on('join')
def on_join(data):
    # Add the player to the game state
    player_id = data['player_id']
    game_state['players'][player_id] = {
        'x': data['x'],
        'y': data['y'],
    }

    # Join the player to a room with their player ID
    join_room(player_id)

    # Send the game state to the player
    emit('game_state', game_state, room=player_id)

# Event handler for when a player moves
@socketio.on('move')
def on_move(data):
    # Update the player's position in the game state
    player_id = data['player_id']
    game_state['players'][player_id]['x'] = data['x']
    game_state['players'][player_id]['y'] = data['y']

    # Broadcast the updated game state to all players in the room
    emit('game_state', game_state, room=player_id)

# Event handler for when a player leaves the game
@socketio.on('leave')
def on_leave(data):
    # Remove the player from the game state
    player_id = data['player_id']
    del game_state['players'][player_id]

    # Leave the player from the room with their player ID
    leave_room(player_id)

    # Broadcast the updated game state to all players in the room
    emit('game_state', game_state, room=player_id)

if __name__ == '__main__':
    socketio.run(app)
