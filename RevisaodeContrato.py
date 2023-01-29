#
#beecrowd-1120
#

from sys import stdin

def decimal_case(default,digit):
    verify=digit.replace(default,'')
    if(set(verify)=={'0'}):
        return True
    else:
        return False

def main():
    for entrance in stdin.readlines():
        separate=entrance.split()
        default=separate[0]
        digit=separate[1]
        if(default=='0' and digit=='0'):
            break
        elif(decimal_case(default,digit)):
            print('0')
        else:
            newdigit=digit.replace(default,'')
            if(newdigit==''):
                print('0')
            else:
                print(newdigit)


if __name__ == '__main__':
    main()
