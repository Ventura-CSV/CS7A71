import main
import io
import sys
import re
import math


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '10 5 20 0 40 45 50 55 9 10\n'
    sys.stdin = io.StringIO(datastr)

    main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    # regex_string = r'[\w,\W]*1'
    # regex_string += r'[\w,\W]*3'
    # regex_string += r'[\w,\W]*5'
    # regex_string += r'[\w,\W]*'
    # print(regex_string)
    # res = re.search(regex_string, main.evenlist)
    # assert res != None
    # print(res.group())
    assert math.floor(main.main.diff[0]) == 14
    assert math.floor(main.main.diff[1]) == 19
    assert math.floor(main.main.diff[2]) == 4
    assert math.floor(main.main.diff[3]) == 24
    assert math.floor(main.main.diff[4]) == 15
    assert math.floor(main.main.diff[5]) == 20
    assert math.floor(main.main.diff[6]) == 25
    assert math.floor(main.main.diff[7]) == 30
    assert math.floor(main.main.diff[8]) == 15
    assert math.floor(main.main.diff[9]) == 14


def test_main_2():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '1 2 3 4 5 6 7 8 9 10\n'
    sys.stdin = io.StringIO(datastr)

    main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    # regex_string = r'[\w,\W]*1'
    # regex_string += r'[\w,\W]*3'
    # regex_string += r'[\w,\W]*5'
    # regex_string += r'[\w,\W]*'
    # print(regex_string)
    # res = re.search(regex_string, main.evenlist)
    # assert res != None
    # print(res.group())
    assert math.floor(main.main.diff[0]) == 4
    assert math.floor(main.main.diff[1]) == 3
    assert math.floor(main.main.diff[2]) == 2
    assert math.floor(main.main.diff[3]) == 1
    assert math.floor(main.main.diff[4]) == 0
    assert math.floor(main.main.diff[5]) == 0
    assert math.floor(main.main.diff[6]) == 1
    assert math.floor(main.main.diff[7]) == 2
    assert math.floor(main.main.diff[8]) == 3
    assert math.floor(main.main.diff[9]) == 4
