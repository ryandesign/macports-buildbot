import os


def get_path(name):
    return os.path.join(os.path.dirname(__file__), name)


def merge_dicts(*dicts):
    res = {}
    for d in dicts:
        res.update(d)
    return res


def port_from_path(path, sep='/'):
    components = path.split(sep)
    try:
        if (components[0] != '_resources'
                and components[2] in ('Portfile', 'files')):
            return components[1]
    except IndexError:
        pass
    return None


def getPriority(request):
    if request.properties and request.properties.hasProperty('priority'):
        return int(request.properties.getProperty('priority'))
    else:
        return float('inf')


def getNextBuildOnPortBuilder(builder, requests):
    nextBuild = requests[0]
    for request in requests:
        if getPriority(request) < getPriority(nextBuild):
            nextBuild = request
    return nextBuild
