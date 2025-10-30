
def get_file_name(fn):
    #read  './config/input_adds.txt', convert the lines without '#' at the start to a list seperate by : and return the value for the key fn
    with open('./config/input_adds.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('#') or not line:
                continue
            key, value = line.split(':', 1)
            if key.strip() == fn:
                return value.strip()
    return None

def get_git_current_commit():
    import subprocess
    try:
        commit = subprocess.check_output(['git', 'rev-parse', 'HEAD']).strip().decode('utf-8')
        return commit
    except Exception as e:
        return None
