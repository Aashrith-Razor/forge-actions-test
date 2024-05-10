import requests


if __name__=='__main__':

    resp = requests.request(
        method='GET',
        url='https://663dd86ce1913c4767959d4c.mockapi.io/test/v1/test1'
    )
    data = resp.json()
    test_check = data[0]['test-check']
    print("Hello from DevOps: ", test_check)

    if test_check:
        exit(0)
    else:
        exit(1)
