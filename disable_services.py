import subprocess
import argparse
import os

def main(restart):
    
    if restart:
        f = open("services_down.txt","r")
        res = f.readline()

        print("Restarting Wifi and Services ...")
        os.system("sudo systemctl start " + res)
        os.system("sudo wifi on")
        print("Restart Successfull")
    else:
        #TODO: Add way to add more processes to keep alive through cmd line
        keep_alive = ['acpid',
                  'apparmor',
                  'apport',
                  'cron',
                  'dbus',
                  'gdm',
                  'irqbalance',
                  'kerneloops',
                  'kmod',
                  'plymouth-log',
                  'procps',
                  'udev']
    
        active = subprocess.check_output(
            "service --status-all | grep + | grep -oe \"[a-zA-Z\\\\-]*\"",
            shell=True
        ).decode('ascii').split()

        # string of services to kill
        to_kill = " ".join(list(filter(lambda x: x not in keep_alive, active)))

        f = open("services_down.txt","w")
        f.write(to_kill)
        f.close()

        print("Shuting Down Wifi and Services ...")
        os.system("sudo wifi off")
        os.system("sudo systemctl stop " + to_kill)
        print("Shuting Down Successfull")





if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Stop and start services")
    parser.add_argument('-r', '--restart', dest='restart', action='store_true',
                        help='Restart Services') 


    args = parser.parse_args()

    main(args.restart)
