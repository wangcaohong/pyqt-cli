import os

def ui_change(target_name):
    ui_path = '../ui/'
    signal = os.system('pyuic5 -o ' + ui_path + target_name + '.py ' + ui_path + target_name + '.ui')
    if (signal == 0):
        print('ui change succeeded.')
    else:
        os.system('rm -f ' + ui_path + target_name + '.py')

if __name__ == '__main__':
    target = input('Please enput target ui file name:')
    ui_change(target)
