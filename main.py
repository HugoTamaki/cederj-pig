from client import *
from vip_client import *
from basic_client import *
from normal_client import *

john = NormalClient('John', 100, 'XPTO')
jane = NormalClient('Jane', 100, 'XPTO')

john.transfer(jane, 30)

john.describe()
jane.describe()

