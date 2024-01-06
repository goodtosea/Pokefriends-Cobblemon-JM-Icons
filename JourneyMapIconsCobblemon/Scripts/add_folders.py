import os
import pokebase

# move directory
os.chdir('E:/Documents/GitHub/JMallsprites/JourneyMapIconsCobblemon/test')
# file with all the missing icon ids
missing_ids_file = open('../missingIDs.txt', 'r')
# json file with data on each id
# pokemon_json_raw = open('E:/Documents/Python Files/JourneyMapIconsCobblemon/pokesprite-master/data/pokemon.json')
# try:
#     pokemon_json = json.load(pokemon_json_raw, encoding='utf8')
# except UnicodeDecodeError:
#     pass
# print(type(pokemon_json))


def delete_files_in_directory(directory_path):
    try:
        files = os.listdir(directory_path)
        for file in files:
            file_path = os.path.join(directory_path, file)
            if os.path.isdir(file_path):
                os.rmdir(file_path)
        print("All files deleted successfully.")
    except OSError:
        print("Error occurred while deleting files.")


# delete_files_in_directory('E:/Documents/Python Files/JourneyMapIconsCobblemon/test')

lines = missing_ids_file.readlines()
for line in lines:
    pokemon_id = int(line.strip())
    pokemon_name = pokebase.pokemon(pokemon_id)
    try:
        os.mkdir(f'{pokemon_id:04d}_{pokemon_name}')
    except FileExistsError:
        pass
