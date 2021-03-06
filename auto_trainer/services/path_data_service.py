import services.json_data_service as jds
import sys
from navigation.direction import Direction


def get_path(start, end):
    paths = __load_path()['paths']
    path_dict = list(
        filter(lambda p: p['start'] == start and p['end'] == end, paths))[0]
    path_sequence = path_dict['sequence']
    path = []
    for component in path_sequence:
        dir_str = component['direction']
        direct = Direction.from_str(dir_str)
        for _ in range(int(component['steps'])):
            path.append(direct)
    return path


def __load_path():
    return jds.load_data(_path_file_url)


def __save_path(data):
    jds.save_data(_path_file_url, data)


def __create_path_from_input():
    start = input('Start Location: ').lower()
    end = input('End location: ').lower()
    print('Input directions and num of steps, "done" to end path:')
    valid_dirs = ['up', 'down', 'left', 'right']
    path_components = []
    while True:
        direct = input('Next direction: ').lower()
        if direct == 'done':
            break
        if direct not in valid_dirs:
            print('Invalid direction')
            continue
        num_steps = input('Number of steps: ')
        component = {
            "direction": direct,
            "steps": num_steps
        }
        path_components.append(component)
    new_path = {
        'start': start,
        'end': end,
        'sequence': path_components
    }
    data = __load_path()
    data['paths'].append(new_path)
    __save_path(data)


_path_file_url = 'data/paths.json'


if __name__ == '__main__':
    if len(sys.argv) == 2:
        if sys.argv[1] == 'create':
            __create_path_from_input()
        elif sys.argv[1] == 'test':
            get_path('verdanturf town', 'route 111 left')
    else:
        raise Exception('expected 1 argument, got ' + (len(sys.argv) - 1))
