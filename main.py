import platform
import Parser
import os, time, sys
import playsound
import combine

import multiprocessing
    
native = "russian" # select your native language

def clear_terminal():
    # Check for the OS and clear the terminal accordingly
    if platform.system == 'Windows':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')

clear_terminal()
playing = 1
folder_path = os.getcwd()

def commands(word):
    global playing
    if word == '/m':
        playing = 1 - playing


        if playing:
            print("\033[92mSuccefuly \033[96mturned on")
        else:
            print("\033[92mSuccefuly \033[96mturned off")
    elif word == '/r':
        mp3_files = [f for f in os.listdir(folder_path) if f.endswith('.mp3')]  # Get all MP3 files in the folder
        
        for mp3_file in mp3_files:
            print(f'\033[96m{mp3_file}\033[96m\033[92m was succefuly removed')
            os.remove(folder_path + '\\' + mp3_file)
            # os.remove(os.path.join(folder_path, mp3_file))  # Remove the MP3 file

        print("\033[93mAll MP3 files in the folder have been removed.\033[93m\n")
    elif word == '/q':
        sys.exit()
    else:
        print("\033[91mOdd command\033[91m")

    Start()
    return 0


def Start():
    global playing
    word = input('\033[95mEnter the word you wish to load here: \033[91m').strip()

    start = time.time()

    for ele in '''!()[]{};:'",<>.?@#$%^&*_~''':
        word = word.replace(ele, "")

    if(len(word) == 0):
        clear_terminal()
        Start()

    if word[0] == '/':
        commands(word)

    clear_terminal()
    print(word)
    
    save_path = f"{folder_path}/{word}.mp3" #Generating of file name
    
    print("\033[92mDownloading..\033[92m")
    
    

    Parser.define(word, save_path, 0, 1, 'english')

    if os.path.exists(save_path):
        if playing:
            p = multiprocessing.Process(target=playsound.playsound, args=(save_path,))
            p.start()
            input("press ENTER to stop playback")
            p.terminate()
    else:
        print("\033[91mSuch word wasn't found\033[91m")
        
        if (combine.comb(word) and playing):
            
            p = multiprocessing.Process(target=playsound.playsound, args=(save_path,))
            p.start()
            input("press ENTER to stop playback")
            p.terminate()


    try:
        print('\033[94m\033[94m')
        Parser.define(word, save_path, 1, 1, f"english-{native}")
    except KeyboardInterrupt:
        # quit
        sys.exit()
    except Exception as err:
        print(err)

    print("\n\033[93m{:.2f}".format(time.time() - start) + " sec")
    print('\n')

    Start()

if __name__ == "__main__":
    Start()
