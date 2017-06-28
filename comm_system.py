#communication systems


from sys import exit

class Comm_system(object):
    def run(self):

        comm_directory = ["net_link", "tsfa_run", "j_link"]
        print("When the system rebooted, some files necessary for")
        print("communicating with the mainland got lost in the directory.")
        print("The files were poorly labeled as a result of sloppy")
        print("programming on the staff's part. You must locate the")
        print("the file and contact the rescue team before the dinosaurs")
        print("surround the visitor's center. You were also notified the")
        print("generators were shorting out, and the mainframe will lose")
        print("power at any moment. Which directory will you search in?")
        print("you don't have much time! Option 1: cd /comm_sys/file")
        print("Option 2: cd /comm_sys/dis")
        print("Option 3: cd /comm_sys/comm")

        dir_choice = input("jpark_edwin$ ")

        if dir_choice == "/comm_sys/file" or dir_choice == "/comm_sys/dis":
            print("misc.txt" )
            print("You couldn't locate the file!")
            print("The system lost power and your computer shut down on you!")
            print("You will not be able to reach the mainland until the system")
            print("comes back online, and it will be too late by then.")
            return 'death'

        if dir_choice == "/comm_sys/comm":
            comm_directory.append("comm_link")
            print(comm_directory)
            print("You found the right file and activated it!")
            print("Just in time too, because the computers shut down on you.")
            print("The phonelines are radios are still online.")
            print("You and the other survivors quickly call the mainlane")
            print("and help is on the way. You all run to the roof and wait")
            print("until the helocopter picks you up. You win!")
a_game = Comm_system()
a_game.run()