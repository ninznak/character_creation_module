def we_crash_all(name: str) -> str:    
    return 'Привет, ' + name + ', мы всё сломали!'


print(we_crash_all(55))

print(we_crash_all.__annotations__)