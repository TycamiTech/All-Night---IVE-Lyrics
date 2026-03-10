import sys
import time

def cetak_lirik():
    UNGU = '\033[95m'
    RESET = '\033[0m'

    lirik = [
        ("We always dreamed about this better life,", 0.05, 0.1),
        ("this better life...", 0.07, 0.5),
        ("We always felt it coming all along,", 0.06, 0.1),
        ("yeah all along...", 0.08, 0.2),
        ("We got the keys to open paradise,", 0.05, 0.1),
        ("yeah paradise...", 0.07, 0.6),
        ("Now let's go walking hand in hand", 0.06, 0.3),
        
        ("Come on baby we can hit the lights,", 0.08, 0.3),
        ("make the wrongs turn right", 0.07, 0.2),
        ("We can smash the clock,", 0.08, 0.2),
        ("make the pop go rock!", 0.08, 0.2),
        ("With a love this deep,", 0.07, 0.1),
        ("we don't need no sleep", 0.07, 0.3),
        ("And it feels like...", 0.09, 0.7),
        ("We could do this all night!", 0.08 , 1.9),
        
        ("We could do this all night,", 0.07, 1.0),
        ("yeah everything is alright", 0.10, 0.4),
        ("We got the keys to open paradise,", 0.06, 0.1),
        ("yeah paradise...", 0.07, 0.2),
        ("It feels like...", 0.10, 2.2),
        ("WE COULD DO THIS ALL NIGHT!", 0.10, 1.0)
    ]

    print(f"\n{UNGU}--- IVE, Saweetie - All Night ---\n")
    time.sleep(0.7)

    for baris, kecepatan, jeda in lirik:
        for karakter in baris:
            sys.stdout.write(karakter)
            sys.stdout.flush()
            time.sleep(kecepatan)
        
        print() 
        time.sleep(jeda)

    print(f"\n--- Tycami Tech ---{RESET}")

if __name__ == "__main__":
    try:
        cetak_lirik()
    except KeyboardInterrupt:
        print("\033[0m\n\nPaused.")