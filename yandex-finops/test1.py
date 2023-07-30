USER_LIMIT = 0
SERVICE_LIMIT = 0
DURATION = 0

# REQUEST_DICT = {time: {userId: nRequest}}
REQUEST_DICT = {}


def parse_init(request):
    global USER_LIMIT, SERVICE_LIMIT, DURATION
        
    USER_LIMIT = int(request[0])
    SERVICE_LIMIT = int(request[1])
    DURATION = int(request[2])


def parse_request(request):
    time = int(request[0])
    userId = int(request[1])

    REQUEST_DICT.pop(time - DURATION, None)
    numRequests = 0
    numUserRequests = 0
    for requestTime in REQUEST_DICT:
        numUserRequests += REQUEST_DICT[requestTime].get(userId, 0)

        for requestUser in REQUEST_DICT[requestTime]:
            numRequests += REQUEST_DICT[requestTime][requestUser]

    if numRequests >= SERVICE_LIMIT:
        print(503)
    elif numUserRequests >= USER_LIMIT:
        print(429)
    else:
        if REQUEST_DICT.get(time, None):
            if REQUEST_DICT[time].get(userId, None):
                REQUEST_DICT[time][userId] += 1
            else:
                REQUEST_DICT[time].update({userId: 1})
        else:
            REQUEST_DICT[time] = {userId: 1}

        print(200)


while True:
    request = input().split()
    if len(request) == 3:
        parse_init(request)
    elif len(request) == 2:
        parse_request(request)
    elif len(request) == 1 and request[0] == '-1':
        break
