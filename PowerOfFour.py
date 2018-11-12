def isPowerOfFour(num):
    """
    :type num: int
    :rtype: bool
    """
    # exclude 0
    if num == 0:
      return False

    # get bit string of num
    bitStr = '{:b}'.format(num)

    # the bit string length of any power of 4 number is a odd number
    if not len(bitStr)%2:
      return False

    # create bit mask which is the largest power of 4 not larger than num
    mask = 1 << (len(bitStr)-1)

    # if num is a power of 4, num binary AND mask will remain num
    return num & mask == num
