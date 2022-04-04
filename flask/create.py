from app import db, Games

db.drop_all()
db.create_all()

new_game = Games(name="name_of_new_game") # to create a game entity to insert into our Games table
db.session.add(new_game)
db.session.commit() #add and commit to insert the information into the database

new_game2 = Games(name="another game") # to create a game entity to insert into our Games table
db.session.add(new_game2)
db.session.commit()

new_game3 = Games(name="Dark Souls") # to create a game entity to insert into our Games table
db.session.add(new_game3)
db.session.commit()

# Games.query.all() #retrieves all entries in a database as objects of type Games
# all_games = Games.query.all()
# print(all_games)

# first_game = Games.query.first()
# print(first_game)

# game_filter_id = Games.query.filter_by(id=1).first()
# print(game_filter_id)

# game_get = Games.query.get(3)  #seems to only do great with numbers not strings
# print(game_get)

# games_in_order = Games.query.order_by(Games.name.desc()).first()
# print(games_in_order)

# first_2_games = Games.query.limit(2).all()
# print(first_2_games)

# number_of_games = Games.query.count()
# print(number_of_games)

# first_game = Games.query.first()
# first_game.name= "New name 2"
# db.session.commit()

game_to_delete = Games.query.first()
db.session.delete(game_to_delete)
db.session.commit()