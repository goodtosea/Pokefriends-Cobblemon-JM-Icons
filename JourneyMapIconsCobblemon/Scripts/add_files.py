import os
import shutil
import pokebase

# for item in dir_list:
#     print(item.split('_')[1])

# for dirpath, dirnames, filenames in os.walk('E:/Documents/Python Files/JourneyMapIconsCobblemon/test'):
#     for dirname in dirnames:
#         os.rename(dirname, dirname.split('-')[0])

for dirpath, dirnames, filenames in os.walk('E:/Documents/Python Files/JourneyMapIconsCobblemon/test'):
    for dirname in dirnames:
        name = dirname.split('_')[1]
        try:
            shutil.copy(
                'E:/Documents/Python Files/JourneyMapIconsCobblemon/pokesprite-master/pokemon-gen8/shiny' + '/' + name + '.png',
                dirpath + '/' + dirname)
            os.rename(dirpath + '/' + dirname + '/' + name + '.png', dirpath + '/' + dirname + '/' + name + '_shiny.png')
            shutil.copy(
                'E:/Documents/Python Files/JourneyMapIconsCobblemon/pokesprite-master/pokemon-gen8/regular' + '/' + name + '.png',
                dirpath + '/' + dirname)
        except FileExistsError:
            pass


# get the regular and shiny sprite from each pokemon
# shutil.copyfile(src, dst)
# try gen 8 then try gen 7 before giving up

# rename them accordingly
