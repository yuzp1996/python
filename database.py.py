import sys,shelve

def store_person(db):
    pid = raw_input(' please enter unique ID number: ')
    person = {}
    person['name'] =  raw_input('ENter Nmae : ')
    person['age'] = raw_input("ENter Nmae: ")
    person['phone'] = raw_input("ENter phone number: ")

    db[pid] = person

def lookup_person(db):
    pid = raw_input("Enter your ID number: ")
    field = raw_input('what would you want to know?(name,age,phone)')
    field = field.strip().lower()
    print field.capitalize()+':',\
          db[pid][field]

def print_help():
    print 'store: store Information'
    print 'lookup ; look up a person from ID from number'
    print 'quit : quit from this system'
    print '?: print this message'

def enter_command():
    cmd = raw_input('Enter command (? for help): ')
    cmd = cmd.strip().lower()
    return cmd
def main():
    database = shelve.open('D:\\database.dat')
    try:
        while True:
            cmd = enter_command()
            if cmd == 'store':
                store_person(database)
            elif cmd == 'lookup':
                lookup_person(database)
            elif cmd == '?':
                print_help()
            elif cmd == 'quit':
                return


    finally:
        database.close()

 

if (1==1): main()
