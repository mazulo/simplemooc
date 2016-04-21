def format_name(name):
    if name.count('/'):
        return name.replace('/', '_').lower()
    return name.lower()
